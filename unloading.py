#unloading is till 


from dataset import ex, dict_consumption_arrival
#188 empty rest  - 132




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
       
def change_loading_unloading_status(dict_input, key,index_value,  changing_string):
    #changing chosen key processed loading
    dict_input[key][index_value] = changing_string
    
    pass
    
    

def getting_ordered_list_un(dict_input, check):
    
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
rest_needs = 0



def increasing_counter_full(dict_input):
    #
    #increasing the dict input, which is the variable to change
    # ex = {"188":["loading", 411.6, 550, "unprocessed loading", "unprocessed unloading", 0],
    #                      "190":["empty", 0, 550,"unprocessed loading", "unprocessed unloading", 0],
    #                       "191":["full", 550, 550,"unprocessed loading", "unprocessed unloading", 0]}
    #getting statuses In order
    for i in dict_input:
         #if the status is full
        if dict_input[i][0] == "full":
            #getting whatever is there
            count_so_far = dict_input[i][5]
            dict_input[i][5] = count_so_far + 1
        else:next
    #returning modified dict
    #to be used to overwrite old one 
    # dict_input = increasing_counter_full(dict_input)
    print("dict input", dict_input)
    return dict_input

#adding a function that orders in case there are two fulls
#gets the input and returns a corrected list based on 
#full count or the same list 
def ordering_full(found_match_input):
     #i know there is more than one here 
    if len(found_match_input)>1:
         #ordering based on the full count
#[['190', ["loading", 310, 550, "unprocessed loading", "unprocessed unloading", 0]],
        #['191', ["loading", 310, 550, "unprocessed loading", "unprocessed unloading", 0]]]
        #get max of the two
        all_counts = [i[1][5] for i in found_match_input]
        #ordering all_counts
        all_counts_ordered = sorted(all_counts, reverse = True)
        # creating ending list
        result = []
        for i in all_counts_ordered:
            for j in found_match_input:
                if j[1][5]==i:
                    result.append(j)
                else:next
    else:
        result = found_match_input
    return result
                





def processing_unloading(dict_input, week, dict_consumption_arrival, rest_needs, check):
    #rest needs should be 0 at the beginning when the function is called 
    total_consumption = dict_consumption_arrival[week][0] + rest_needs
    rest_needs = 0
   

    #adding the counter 
    dict_input = increasing_counter_full(dict_input)


    #i have an ordered list of values that represent my processed statuses [0, 1, 2], unloading, full, empty
    sorted_statuses = getting_ordered_list_un(dict_input, check)
    
 
    #([0, 2, 3, 3], ['unloading', 'empty', 'loading', "loading"]) --> ex of what we could get

    #start unloading according to algorithm , if the first is unloading
    #sorted statuses ([0, 1, 2], ['loading', 'empty', 'unloading'])
    #getting the relevant phases 
    found_match_unloading =  find_value_for_loading(dict_input, "unloading")
    found_match_full = ordering_full(find_value_for_loading(dict_input, "full"))

    if len(found_match_unloading)>0 :
        for i in range(len(found_match_unloading)):
            #the quantity in silos is bigger than needs 
            if  (found_match_unloading[i][1][1] - total_consumption) > 0 and   total_consumption>0:
                #changing key to processed loading
                change_loading_unloading_status(dict_input, found_match_unloading[i][0],4, "processed_unloading")
                change_loading_unloading_status(dict_input, found_match_unloading[i][0],1,found_match_unloading[i][1][1] - total_consumption )

                #erasing the status  
                total_consumption = 0 
            #here i satisfy needs and then erase the consumption 
            elif  (found_match_unloading[i][1][1] - total_consumption) == 0 and total_consumption > 0:
                #changing key to processed loading
                change_loading_unloading_status(dict_input, found_match_unloading[i][0],4, "processed_unloading")
                #keeo status to loaded 
                #erasing_total_arrival 
                total_consumption = 0
                #changing the status
                change_loading_unloading_status(dict_input, found_match_unloading[i][0],0, "empty")
                change_loading_unloading_status(dict_input, found_match_unloading[i][0],1, 0)
        #we cannot cover everything  with unloading, will look for other unloadings or 
            elif (found_match_unloading[i][1][1] - total_consumption) <0 and total_consumption > 0:
                #changing key to processed loading
                change_loading_unloading_status(dict_input, found_match_unloading[i][0],4, "processed_unloading")
                #keeo s in in silos - need - x)=  -in silos + need
                unloaded  =  found_match_unloading[i][1][1]
                #total consumption is now the rest so i shpuld decrease it
                total_consumption -= unloaded
                #erasing_total_arrival 
                #change status to full
                change_loading_unloading_status(dict_input, found_match_unloading[i][0],0, "empty")
                #changing the value in the value slot
                change_loading_unloading_status(dict_input, found_match_unloading[i][0],1, 0)
                #looking for loading in the second iteration 
    if len(found_match_full)>0 and   total_consumption>0:
        print("found match full in the unloading  ------------->  ", found_match_full)
        for i in range(len(found_match_full)):
            #total consupltion is now the rest needs 
            if 0 < total_consumption < found_match_full[i][1][2]:
                change_loading_unloading_status(dict_input, found_match_full[i][0],4, "processed_unloading")
                #changing the status to full 
                change_loading_unloading_status(dict_input, found_match_full[i][0],0, "unloading")
                #change the value to the max
                change_loading_unloading_status(dict_input, found_match_full[i][0],1,  found_match_full[i][1][2] - total_consumption)
                #resetting rest needs
                total_consumption = 0
                #resetting the counter as it is now unloading
                change_loading_unloading_status(dict_input, found_match_full[i][0],5, 0)
            elif total_consumption == found_match_full[i][1][2]:
                change_loading_unloading_status(dict_input, found_match_full[i][0],4, "processed_unloading")
                #changing the status to full 
                change_loading_unloading_status(dict_input, found_match_full[i][0],0, "empty")
                #change the value to the max
                change_loading_unloading_status(dict_input, found_match_full[i][0],1, 0)    
                #rest_needs to 0 as everything was loaded
                #resetting the counter as it is now unloading
                change_loading_unloading_status(dict_input, found_match_full[i][0],5, 0)
                total_consumption = 0
                #here i am needing more than 550 so i take all
            elif total_consumption > found_match_full[i][1][2]:
                total_consumption -= found_match_full[i][1][2]
                #2 now as we are going one iteration down 
                change_loading_unloading_status(dict_input, found_match_full[i][0],4, "processed_unloading")
                #changing the status to full 
                change_loading_unloading_status(dict_input, found_match_full[i][0],0, "empty")
                #change the value to the max
                change_loading_unloading_status(dict_input, found_match_full[i][0],1, 0)
                #case in which the first is empty
                #resetting the counter as it is now empty
                change_loading_unloading_status(dict_input, found_match_full[i][0],5, 0)
    else:
        #here we do not process anything , should keep things as they are
        pass
    print("in unloading the dict input ----> ", dict_input)
    return total_consumption, dict_input







