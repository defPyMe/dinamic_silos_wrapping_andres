#import quantity input
#need to check what is done in the other df in the second_first df 






















import pandas as pd


#coverweeks 
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





# aim is to create a new loading plan 

def create_consumption(quantity_target, flag_month):#flag month tells us how many months to project into the future
    # importing the first iteration result and doimg some analysis 
    df_result = pd.read_excel(r"C:\Users\cavazluca1\OneDrive - Ferrero Ecosystem\Desktop\projects\andres coca butter\siloses_all\result_max_loading_4_siloses.xlsx", sheet_name= "Sheet1")
    #importing the consumption df 
    df_consumption_arrivals = pd.read_excel(r"C:\Users\cavazluca1\OneDrive - Ferrero Ecosystem\Desktop\projects\andres coca butter\siloses_all\common datasets\datasets.xlsx", sheet_name= "4 silos")
    #read once the conpumtion df, the other needs to be recalculated
    #filtering the unloading cycle which is the last 
    df_result_unloading = df_result[df_result["cycle_name"] == "unloading"]#just the second and last cycle
    #isolating the values in keys , unique values 
    all_weeks_loaded_list = list(set(df_result["week"]))
    #calculating the result list 
    summed_current_filling = []#list with the values in order
    print(df_result_unloading.columns)
    for i in all_weeks_loaded_list:#all the weeks 
        df_result_unloading_week = sum(list(df_result_unloading[df_result_unloading["week"]==i]["current_filling"]))#filtering per week in iteration, creating a list with the values and summing , result = integer
        summed_current_filling.append(df_result_unloading_week)
    #adding the week and its values
    week_full_filling = {k:v for k,v in zip(all_weeks_loaded_list, summed_current_filling)}
    #or list 

    #needs to take into consideration if there are enough values or not to cover for the projection
    #this month is already in transit so it shouldn t be considered as it was shipped the previous month 
    #should project the next two months , check if the list is long enough and if the conditions are there we proceed (1 or two months)
    if flag_month == 1: #project one month 
        all_weeks_loaded_list_sliced =  summed_current_filling[5:10]#here needs to start as well as the slicing in consumption
    elif flag_month == 2:
        all_weeks_loaded_list_sliced =  summed_current_filling[5:15]
    #calculating the coverages for the weeks in the sliced weeks
    
    counter_outer = 0 
    coverage_column_dict = {}#coverage column to store teh necessary values
    all_consumption =  list(df_consumption_arrivals["consumption"])
    coverage_column = []

    
    for i in all_weeks_loaded_list_sliced:
        res = coverweek( i, all_consumption, counter_outer)
        coverage_column.append(res)
        counter_outer +=1
        coverage_column_dict[i] = res

    print(coverage_column_dict)
    d

    








    
    
    #add a column calculating the coverage 
    all_arrival = list(df_consumption_arrivals["arrivals"])#arrivals in projection
    all_consumption =  list(df_consumption_arrivals["consumption"]) #consumption in projection
    

    counter_outer = 0 
    coverage_column = []#coverage column to store teh necessary values

    for i in all_weeks_loaded_list:
        res = coverweek( i, all_consumption, counter_outer)
        coverage_column.append(res)
        counter_outer +=1
    
    #once added the column i have to calculate the average of the added values 
    #assuming the column name is coveage_weeks
    df_result["coverage_weeks"] = coverage_column
    average_column = list(df_result["coverage_weeks"])
    
    average = sum(average_column)/len(average_column)#maybe / 3 here? depends how much i consider
    
     
    if average < quantity_target: # + arrivals to expand the average next iteration 
        
        
        
        
        pass
    else:#bigger or 0
        
        
        
        
        
        
        pass
    
    
    
    
    
    
    
    
    pass

create_consumption(5, 1)


























