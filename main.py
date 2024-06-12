from loading import processing_loading, process_second_loading
from unloading import processing_unloading
from dataset import ex, dict_consumption_arrival,initial_remaining, initial_needs, all_weeks
from writing import creating_list_values, purify_the_df
import sys, os

#flow
#process loading returns a tuple with item number 1 being the rest in genova and the item number 2 being the updated siloses
#process unloading uses the updated siloses for the next allocation 

#HOW IS LOADED IN CURRENT ADAPTED TO THE WRAPPING AROUND OF TEH MODEL 




#first_loading = processing_loading(ex, "48", dict_consumption_arrival, 0,  check = {"loading":0 , "empty":1, "unloading":2,"full":3})
#creating_list_values(first_loading,"loading", "48")
#first_unloading = processing_unloading(first_loading[1], "48", dict_consumption_arrival, 0,  check = {"loading":3 , "empty":2, "unloading":0,"full":1})
# now the rest in genova become the first_loading[0]
#creating_list_values(first_unloading,"unloading", "48")
# then rest needs are the first unloading[0] 
#second_loading = processing_loading(ex, "49", dict_consumption_arrival,0 ,  check = {"loading":0 , "empty":1, "unloading":2,"full":3})
#creating_list_values(second_loading,"loading", "49")
#second_unloading = processing_unloading(second_loading[1], "49", dict_consumption_arrival, 0,  check = {"loading":3 , "empty":2, "unloading":0,"full":1})
#creating_list_values(second_unloading,"unloading", "49")
#first loading adjusted manually

#first_loading = processing_loading(ex, "50", dict_consumption_arrival, 368.6 ,  check = {"loading":0 , "empty":1, "unloading":2,"full":3})
#first_unloading = processing_unloading(first_loading[1], "50", dict_consumption_arrival, 0,  check = {"loading":3 , "empty":2, "unloading":0,"full":1})
#for i in dict_consumption_arrival:
    #looping over the keys = weeks, ex needs to be changed, rest needs to be changed as well
#    second_loading = processing_loading(ex, i, dict_consumption_arrival, 368.6 ,  check = {"loading":0 , "empty":1, "unloading":2,"full":3})
#    second_unloading = processing_unloading(first_loading[1], "50", dict_consumption_arrival, 0,  check = {"loading":3 , "empty":2, "unloading":0,"full":1})
if __name__ == "__main__":
    try:
        for i in all_weeks:
            #if we are in the first instance
            if i == all_weeks[0]:
                first_element_loading = processing_loading(ex, i, dict_consumption_arrival,initial_remaining ,  check = {"loading":0 , "empty":1, "unloading":2,"full":3})
                creating_list_values(first_element_loading,"loading", i, "")#adding empty values 
                first_element_unloading = processing_unloading(first_element_loading[1], i, dict_consumption_arrival,  initial_needs,  check = {"loading":3 , "empty":2, "unloading":0,"full":1})
                creating_list_values(first_element_unloading,"unloading", i, "")
                #defining the new variables
                ex = first_element_unloading[1]
                #representing the third loading remainings
                initial_remaining = first_element_loading[0]
                #representing the unloading remains S
                initial_needs =  first_element_unloading[0]
                print( "initial remains week 1", initial_remaining, "initial needs week 1", initial_needs , "week ",  i)
            else:
                print("initial remains going in ", initial_remaining, "initial needs going in", initial_needs , "week going in ",  i)
                #initial remaining here should be the what was calculated in the first instance
                not_first_elements_loading = list(processing_loading(ex, i, dict_consumption_arrival, initial_remaining, check = {"loading":0 , "empty":1, "unloading":2,"full":3}))
                creating_list_values(not_first_elements_loading,"loading", i, "")
                not_first_elements_unloading = list(processing_unloading(not_first_elements_loading[1], i, dict_consumption_arrival, initial_needs,  check = {"loading":3 , "empty":2, "unloading":0,"full":1}))
                creating_list_values(not_first_elements_unloading,"unloading", i, "")
                # need to define the new ex
                ex = not_first_elements_unloading[1]
                #defining initial remains
                initial_remaining = not_first_elements_loading[0]
                #defining initial needs 
                initial_needs = not_first_elements_unloading[0]
                #print the remainings after each iteration 
                print( "initial remains", initial_remaining, "initial needs", initial_needs , "week ",  i)
                print("what entering into teh second loading ",not_first_elements_loading,  type(not_first_elements_loading[2]) ,not_first_elements_loading[2] , not_first_elements_loading[0],  type(not_first_elements_loading[0]))
                #initial values, 
                
                if not_first_elements_loading[3] - not_first_elements_loading[0] < 194:
                    #create a ccutom function 
                    print("not_first_elements_loading not working --> ", not_first_elements_loading)
                    to_load = 194 - (not_first_elements_loading[3] - not_first_elements_loading[0])
                    print("to load should be differentce between the 194 and what we were able to load--------------------------->  ", "ex----> " ,i,  ex, to_load, initial_needs,initial_remaining ,  not_first_elements_loading )
                    
                    #should modify iteratively here 
                    exceptions_elements_loading = list(process_second_loading(ex, to_load, initial_remaining, not_first_elements_loading, check = {"loading":0 , "empty":1, "unloading":2,"full":3}))
                    print("exceptions_elements_loading --> ", exceptions_elements_loading)
                    #EX IS EQUAL to not first oading so i can just modify it 
                    #not sending the rest needs 
                    # exceptions_elements_loading[0]  = rest_needs
                    creating_list_values(not_first_elements_loading, "xxx", i,"" )
                    ex = exceptions_elements_loading[1]
                    initial_remaining = exceptions_elements_loading[0]
                    print("789463514321354362103 -->"  , not_first_elements_loading[2],exceptions_elements_loading[2], "all stop")
                    not_first_elements_loading[2] = exceptions_elements_loading[2]#substituting the dict 
                    

                    pass

                else:pass
        #add function here 
        purify_the_df(r"C:\Users\cavazluca1\OneDrive - Ferrero Ecosystem\Desktop\projects\andres coca butter\siloses_all\result_max_loading_4_siloses.xlsx")



    except Exception as e :
        print(e)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)

        




