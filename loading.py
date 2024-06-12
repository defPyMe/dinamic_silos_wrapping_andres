#from dataset import ex, dict_consumption_arrival




#starting with rest needs at 0


def find_value_for_loading(dictionary, look_word):
    res = []
    for key, values in dictionary.items():
        if len(values[0]) == len(look_word):
            res_pre = [key, values]
            # Check if there is a value next to "loading" in the list
            res.append(res_pre)
        else:
            next
    #this returns a list if the look word is found in values
    #runs only if the first condition is met
    return res
       
def change_loading_unloading_status( dict_input, key,index_value,  changing_string):
    #changing chosen key processed loading
  
        dict_input[key][index_value] = changing_string

    
    

def getting_ordered_list(dict_input, check):
    check = {"loading":0 , "empty":1, "unloading":2,"full":3}
    #getting the values 
    dict_input_statuses = [dict_input[i][0] for i in dict_input]
    #ordering them according to plan so they are executed first 
    sorted_statuses  = sorted([check[i] for i in  dict_input_statuses])#[0, 1, 2]
    #getting teh statuses ordered  
    ordered_values = []
    #getting a list of statuses in correct order 
    #['loading', 'empty', 'unloading'])
    for value in sorted_statuses:
        ordered_values.append([i for i in check if check[i]==value][0])

    return sorted_statuses, ordered_values

#max is 228 , we return the rotal arrival corrected as a value
def calculate_max_loadable(total_arrival):
    print("total arrival in the algorithm, should be rest genova + arrival ", total_arrival)
    if total_arrival == 0:
         loadable = 0
    elif total_arrival < 213.4:
         loadable = total_arrival
         #erasing total arrival
         total_arrival = 0
    else:
         loadable = 213.4
         
         # taking out the loadable from total arrival
         total_arrival = total_arrival - loadable
    print("total arrival in the algorithm after subtraction loadable", loadable)
    #returning a tuple with total arrival and loadable
    return [total_arrival, loadable]






def increasing_counter_empty(dict_input):
    #
    #increasing the dict input, which is the variable to change
    # ex = {"188":["loading", 411.6, 550, "unprocessed loading", "unprocessed unloading", 0],
    #                      "190":["empty", 0, 550,"unprocessed loading", "unprocessed unloading", 0],
    #                       "191":["full", 550, 550,"unprocessed loading", "unprocessed unloading", 0]}
    #getting statuses In order
    for i in dict_input:
         #if the status is full
        if dict_input[i][0] == "empty":
            #getting whatever is there
            count_so_far = dict_input[i][6]
            dict_input[i][6] = count_so_far + 1
        else:next
    #returning modified dict
    #to be used to overwrite old one 
    # dict_input = increasing_counter_full(dict_input)
    return dict_input



def ordering_empty(found_match_input):
     #i know there is more than one here 
    if len(found_match_input)>1:
         #ordering based on the full count
#[['190', ["loading", 310, 550, "unprocessed loading", "unprocessed unloading", 0]],
        #['191', ["loading", 310, 550, "unprocessed loading", "unprocessed unloading", 0]]]
        #get max of the two
        all_counts = [i[1][6] for i in found_match_input]
        #ordering all_counts
        all_counts_ordered = sorted(all_counts, reverse = True)
        # creating ending list
        result = []
        for i in all_counts_ordered:
            for j in found_match_input:
                if j[1][6]==i:
                    result.append(j)
                else:next
    else:
        result = found_match_input
    return result
                




def processing_loading(dict_input, week, dict_consumption_arrival, rest_genova, check):

    #defining a new variable here to see the what is loaded wher exactly, write it to the output might be nice 
    #expected outputn should  be a dict that is something like loaded_off = {188 : 0, 189 : 0, 191 : 235}
    # the dict input is as follows -->  {190: ['loading', 414.6, 550, 'unprocessed loading', 'unprocessed unloading', 0, 0], 191: ['unloading', 69.0, 550, 'unprocessed loading', 'unprocessed unloading', 0, 0],
    # 189: ['full', 550.0, 550, 'unprocessed loading', 'unprocessed unloading', 0, 0]}
    #the created dict should have all 0 
    list_of_values = [(i, 0) for i in dict_input]#create lists with zeroes 

    dict_loading = {k:v for (k,v) in list_of_values}
    total_arrival_original =  dict_consumption_arrival[week][1] + rest_genova



    #rest needs should be 0 at the beginning when the function is called 
    #ex total_arrival = 550
    total_arrival = dict_consumption_arrival[week][1] + rest_genova #
    print("dict cons arrival", dict_consumption_arrival[week], rest_genova, "week ", week)
    rest_genova = 0
    
    #tuple with teh following 
    tot_load = calculate_max_loadable(total_arrival)
    #total_load[1] == 194
    #tot_load[1] = 228 - tot_load[0] = 322
    
    #i have an ordered list of values that represent my processed statuses [0, 1, 2], loading , empty , unloading
    dict_input = increasing_counter_empty(dict_input)
    sorted_statuses = getting_ordered_list(dict_input, check)
    print("sorted statuses of the dicts --->  ", sorted_statuses)
    #start loading according to algorithm , if the first is loading
    #need to add a case here 
    #sorted statuses ([0, 1, 2, 2], ['loading', 'empty', 'unloading', "unloading"])
    #should remove all keys that are not valuable for us , so keep only 0 and 1
    #removing could be a problem in terms of indexes 
    #looking for the found matches both for laoding and unloading
    found_match_loading =  find_value_for_loading(dict_input, "loading")
    found_match_empty = ordering_empty(find_value_for_loading(dict_input, "empty"))
    #print(len(found_match_loading), found_match_loading[0][0])
    #loading --> [[191, ['loading', 194, 550, 'unprocessed loading', 'unprocessed unloading', 0, 0]]]
    #empty ---> [[188, ['empty', 0, 550, 'unprocessed loading', 'unprocessed unloading', 0, 1]], [199, ['empty', 0, 550, 'unprocessed loading', 'unprocessed unloading', 0, 1]]]

    #i have something to load here, loads every time o i update my check dict every time 
    if len(found_match_loading) > 0:
        for i in range(len(found_match_loading)):
            #i am in the first one
            #to load - found_match first one, should be one here  
            if tot_load[1] + found_match_loading[i][1][1] < found_match_loading[i][1][2]:
                print("loadable + already loaded is less than teh full silos as total loadable --> ",  tot_load[1], " and the already loaded ", found_match_loading[i][1][1]  )
                #changing key to processed loading
                change_loading_unloading_status(dict_input, found_match_loading[i][0],3, "processed_loading")
                #keeo status to loaded 
                change_loading_unloading_status(dict_input, found_match_loading[i][0],1,  tot_load[1] + found_match_loading[i][1][1])
                #loaded is the key chosen dso dict_loading[found_match_loading[i][0]]  +  tot_load[1]
                dict_loading[found_match_loading[i][0]] = tot_load[1]#UPDATING THE DICT LOADING STUFF
                #erasing the tuple
                tot_load[1] = 0 
                #erasing total arrival, rest = 0 
                #rest_genova = total_arrival - loaded
                #erasing_total_arrival 
                #total_arrival = 0
                rest_genova = tot_load[0] #it is zero here anyway + tot_load[1]
                #print("loading found, total arrivallower than loaded + arrival in dict values",  tot_load[1]  + found_match[0][1][1]  )
                #loadable here is enough to get to 550
            elif tot_load[1] + found_match_loading[i][1][1] == found_match_loading[i][1][2]:
                #changing key to processed loading
                change_loading_unloading_status(dict_input, found_match_loading[i][0],3, "processed_loading")
                #setting to max
                change_loading_unloading_status(dict_input, found_match_loading[i][0],1, found_match_loading[i][1][2])#changing here with the max used 
                #erasing the loaded
                tot_load[1] = 0 
                change_loading_unloading_status(dict_input, found_match_loading[i][0],0, "full")
                print("loadable + already loaded is equal to full silos as total loadable -->  ",  tot_load[1], " and the already loaded ", found_match_loading[i][1][1]  )
                dict_loading[found_match_loading[i][0]] = tot_load[1]#here we have the max written but we record only what was loaded 
                #should be 0 anyway
                rest_genova = tot_load[0] 
                #here loadable is higher 
            elif tot_load[1] + found_match_loading[i][1][1] > found_match_loading[i][1][2]:
                #changing key to processed loading
                change_loading_unloading_status(dict_input, found_match_loading[i][0],3, "processed_loading")
                
                #keeo status to loaded 
                #maximum loading is tot_load[1]
                loaded_current = found_match_loading[i][1][2] - found_match_loading[0][1][1]
                #rest to load if poossinle, loaded current always less than tot_load[1]
                #changing the tuple including the loaded
                dict_loading[found_match_loading[i][0]] = loaded_current #As here we go over the max, we load only what was actually loadable
                
                
                
                tot_load[1] -= loaded_current
                rest_genova = tot_load[0]
                #change status to full
                change_loading_unloading_status(dict_input, found_match_loading[i][0],0, "full")
                #changing the value in the value slot
                change_loading_unloading_status(dict_input, found_match_loading[i][0],1, found_match_loading[i][1][2])
                print("loadable + already loaded is more than teh full silos as total loadable --> ",  tot_load[1], " and the already loaded ", found_match_loading[i][1][1]  )
                #looking for loading in the second iteration 
                #there is loading here so we have it also in the match on top
    #adding if there are any leftover
    #new checking in the function
    found_match_empty = ordering_empty(find_value_for_loading(dict_input, "empty"))
    rest_to_load =  tot_load[1]#assigning value to variable
    print("rest to loadddddddddddd bvefore function, should b equal to tot_load[1]","rest_to_load ", rest_to_load, "tot_load[1] ", tot_load[1])



    if len(found_match_empty) > 0 and rest_to_load>0:
        for i in range(len(found_match_empty)):
            if rest_to_load>0:#first time will be bigger than ex 700
                print("entering the empty cycle as the loading couldn t absord all with dict input equal to , ",dict_input,  " found match empty equal to ", found_match_empty,  " and rest to load equal to ", rest_to_load)
                loadable = min(550,rest_to_load)
                change_loading_unloading_status(dict_input, found_match_empty[i][0],3, "processed_loading")
                #put total arrival here so we need to allocate all
                print("loadable is equal to ", loadable, " as it is the min between 550 and  ", loadable)
                #keeo status to loaded 
                
                #resetting total arrival
                rest_to_load = rest_to_load -  loadable#could be zero or more 0 = 127 - 127
               
                #erasing total arrival, rest = 0 
                if  rest_to_load>0:#here i still have something to allocate 
                    status = "full"
                    value = found_match_empty[i][1][2]
                    print("rest to load bigger than zero after subtraction  ", rest_to_load)

                else:
                    status = "loading"
                    value = loadable#here should be equal to 0
                    print("entered status loading ", rest_to_load)
                change_loading_unloading_status(dict_input, found_match_empty[i][0],1, value)
                #here process is iterative so we add teh dict update inside the loop 
                dict_loading[found_match_empty[i][0]] = value
                change_loading_unloading_status(dict_input, found_match_empty[i][0],0, status)
                #resetting counter
                change_loading_unloading_status(dict_input, found_match_empty[i][0],6, 0)
                
                rest_genova = tot_load[0] 
            else:pass
    else:
        rest_genova = tot_load[1] +  tot_load[0]#becomes here rest to load
        #passed on to the next cycle
    print("week "+ week + "rest genova "+ str(rest_genova),  " the dict input we will push into the nex  itertaion is ", dict_input)
    
    return rest_genova, dict_input, dict_loading, total_arrival_original#adding dict loading return here 



#getting the values working 
#second loading to be added into the loading function

#HERE WE SHOULD UPDATE WHAT IS LOADED , IN THE CHOSEN 

def process_second_loading(dict_input,to_load,rest_genova ,not_first_elements,  check):
    #takes dict input, loadable after loading , 
    #looks for empty , if there is then we load the remaining else we exit
    #not sure we should increament counter 
    sorted_statuses = getting_ordered_list(dict_input, check)
    #looking for empty
    found_match_empty = ordering_empty(find_value_for_loading(dict_input, "empty"))
    #the total load should be above anyway 
    if len(found_match_empty) > 0:
        for i in range(len(found_match_empty)):
            
            change_loading_unloading_status(dict_input, found_match_empty[i][0],3, "processed_loading")
            #put total arrival here so we need to allocate all
            print("entering the empty cycle !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            change_loading_unloading_status(dict_input, found_match_empty[i][0],1,to_load)
            #keeo status to loaded 
            #resetting total arrival
            #erasing total arrival, rest = 0 
            change_loading_unloading_status(dict_input, found_match_empty[i][0],0, "loading")
            #resetting counter
            change_loading_unloading_status(dict_input, found_match_empty[i][0],6, 0)
            #change the dict loaded 
            not_first_elements[2][found_match_empty[i][0]] = to_load
            #is this changing or not ? hould i increment it 
            rest_genova = rest_genova - to_load
            #calculating the rest needs 
    else:
        
        rest_genova = rest_genova 
        #passed on to the next cycle

    


    return rest_genova, dict_input, not_first_elements[2]