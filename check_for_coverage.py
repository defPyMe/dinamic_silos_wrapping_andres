#file to get the total weeks of coverage of a particular week 
#weeks will be removed manially so i can have the cleaned fiel in teh next 
import pandas as pd 







#check for the cover weeks
def coverweek(value, range_list, counter_outer):#value as the value to be taken and the range as the list of values
    #defining subtot
    subtot = 0
    counter = 0
    for i in range(len(range_list)):
        if value <= subtot + range_list[i + counter_outer]:
            coverage = counter + (value - subtot) / range_list[i + counter_outer]
            subtot += range_list[i + counter_outer]
            print(range_list[i +  counter_outer], value)
            break
        else: 
            counter +=1
            subtot += range_list[i +  counter_outer] 
            print(range_list[i +  counter_outer], value)   
    if subtot < value:
        coverage = counter
    return round(coverage, ndigits=1)




def main_elaboration(file):
    #reading the input file 
    #columns of input --> week num	consumption	arrival
    df_input = pd.read_excel(file) 
    #weeks are already removed when imorting so i can start to calculate from there 
    # adding quantities to the list of consumption so that the everything is covered 
    #adding the last month two times to make sure, should be enough
    all_consumption = df_input["consumption"]
    #current columns in the output are -->[ siloses_numbers	current_status	current_filling	total_filling	week	df_rest_genova	df_rest_needs	cycle_name	loading_counter	unloading_counter	loaded_current	unloaded_current]
    all_consumption_aug = []#addding 
    
    
    
    
    
    pass