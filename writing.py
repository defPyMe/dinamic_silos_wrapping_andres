# just writing to an aoutput file some values , the final iteration at the end of the week 
# using an excel file as container with some premade columns 
import pandas as pd
#i write both first loading and then unloading to track the whole process
#input is a tuple 
#(rest_needs/rest_genova , {dict modified})
import os, sys




# (369.8, {190: ['full', 550, 550, 'processed_loading', 'unprocessed unloading', 0, 0], 191: ['unloading', 69.0, 550, 'unprocessed loading', 'unprocessed unloading', 0, 0], 
#189: ['full', 550.0, 550, 'unprocessed loading', 'unprocessed unloading', 0, 0]}, {190: 135.39999999999998, 191: 0, 189: 0})

#need to create here the loading odf the loading dict created 
#input tuple now has three elements i should consider 

#creating list vaòlues is teh last function called so i should use it to purify the df 
#reading the df and get the last part of the loading 
#



#create key week cycle name and remove duplicatres and keep last 
def purify_the_df(path):
    df = pd.read_excel(path)
    #adding the key column
    #typecasting the coumn before
    df = df.astype({'siloses_numbers':'string'})
    df["key_week"] = df["week"] + df["cycle_name"] + df["siloses_numbers"]
    df.drop_duplicates(subset = ["key_week"], keep = "last", inplace = True)
    #delete the extra column after elaboration 
    df.drop(["key_week"], axis = 1, inplace = True)
    #writing to excel 
    df.to_excel(path, index = False)
    
    

    
    
    pass







def creating_list_values(input_tuple, cycle_name, week, remains):
    

    df_result = pd.DataFrame()
    #will use input tuple 1 as a flag of the lenght --> len(input_tuple[1])
    print("input tuple in writing -----> ", input_tuple, "    " , cycle_name)
    
    #input tuple = (0, {188: ['loading', 271.6, 550, 'processed_loading', 'processed_unloading', 0, 0], 190: ['empty', 0, 550, 'processed_loading', 'processed_unloading', 
    #0, 2], 191: ['loading', 35.0, 550, 'processed_loading', 'processed_unloading', 0, 0]})
    #getting the siloses from dict in second tuple place
    list_siloses = list(input_tuple[1].keys())
    #getting current status after loading/unloading
    current_status = [input_tuple[1][i][0] for i in  list(input_tuple[1].keys())]
    #getting the current filling 
    current_filling= [input_tuple[1][i][1] for i in  list(input_tuple[1].keys())]
    #getting the total filling
    total_filling = [input_tuple[1][i][2] for i in  list(input_tuple[1].keys())]
    #df week . with week being a string
    week = [[week]* len(total_filling)][0]
    if cycle_name=="loading":#using loading to flag the  loaded current
        #making this dinamic
        rest_genova = [input_tuple[0] for i in range(len(input_tuple[1]))]
        rest_needs = [0 for i in range(len(input_tuple[1]))]
        loaded_current = list(input_tuple[2].values()) #should be in order with the keys , i need to take the values only 
        print("loaded_current ---> ", loaded_current)
       
        cycle = [cycle_name for i in range(len(input_tuple[1]))]


        #should add the unloaded current here , skipping the loading altogether
    #different cycle
    elif cycle_name=="xxx":#using loading to flag the  loaded current
        #making this dinamics
        print("entering here ------------------------------------------------------------------------------------------------------------------------------------------->", input_tuple)
        rest_needs = [0 for i in range(len(input_tuple[1]))]
        rest_genova = [remains for i in range(len(input_tuple[1]))]
        loaded_current = list(input_tuple[2].values()) #should be in order with the keys , i need to take the values only 
        print("loaded_current ---> ", loaded_current, input_tuple)
        
        #unloading hardcoded

        cycle = ["unloading" for i in range(len(input_tuple[1]))]#unloading before, loading for andres to make it work   <---------------------------------------
    #unloading
    else:
        print("entering here unoading")
        rest_needs =  [input_tuple[0] for i in range(len(input_tuple[1]))]
        rest_genova =  [0 for i in range(len(input_tuple[1]))]
        #fake loaded with all zeroes to match the loading , shouldn t be the 
      #should be in order with the keys , i need to take the values only 
        #here we record what was loaded into each silo
        cycle = [cycle_name for i in range(len(input_tuple[1]))]
        loaded_current =   [0 for i in range(len(input_tuple[1]))]
    
    
    
   
    #getting counters 
    loading_counter = [input_tuple[1][i][5] for i in  list(input_tuple[1].keys())]
    unloading_counter = [input_tuple[1][i][6] for i in  list(input_tuple[1].keys())]
    
    



    #adding the values to dfs
    df_result["siloses_numbers"] = list_siloses
    df_result["current_status"] = current_status
    df_result["current_filling"] = current_filling
    df_result["total_filling"] =  total_filling
    df_result["week"] =  week
    df_result["rest_genova"] =  rest_genova
    df_result["rest_needs"] =  rest_needs
    df_result["cycle_name"] = cycle
    #unloading and loading
    df_result["loading_counter"] =  loading_counter 
    df_result["unloading_counter"] =  unloading_counter 
    df_result["loaded_current"] = loaded_current

    with pd.ExcelWriter(r"C:\Users\cavazluca1\OneDrive - Ferrero Ecosystem\Desktop\projects\andres coca butter\siloses_all\result_max_loading_4_siloses.xlsx",mode="a",engine="openpyxl",if_sheet_exists="overlay") as writer:
        df_result.to_excel(writer, sheet_name="Sheet1",header=None, startrow=writer.sheets["Sheet1"].max_row,index=False)
    return "written to file"




