import pandas as pd
import matplotlib.pyplot as plt 
from snippet import render_mpl_table
import seaborn as sns
import numpy as np
import datetime
#adding operator to add up values 
from operator import add








#function to create a custom date to ad a label to the graph
def return_current_week_year():
    wn = datetime.datetime.today().isocalendar()[1] 
    year = datetime.datetime.now().year
    week_year = str(wn) + " " + str(year)
    return week_year 
    
#function to create a custom date to ad a label to the graph
def return_current_previous_week_year():
    wn = datetime.datetime.today().isocalendar()[1] - 1
    year = datetime.datetime.now().year
    week_year = str(wn) + " " + str(year)
    return week_year

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
    

#i generate here the first two elements , that is a the graph and the table for the first 4 weeks 
#the report will be generated on a weekly basis so i will have the first week as teh frozen previous week , the frozen week is retrieved from the dataset initial status tab
#mpoting all the necessary  
df_result = pd.read_excel(r"C:\Users\cavazluca1\OneDrive - Ferrero Ecosystem\Desktop\projects\andres coca butter\siloses_all\result_max_loading_4_siloses.xlsx", sheet_name="Sheet1")
df_initial = pd.read_excel(r"C:\Users\cavazluca1\OneDrive - Ferrero Ecosystem\Desktop\projects\andres coca butter\siloses_all\common datasets\datasets.xlsx", sheet_name = "4 silos initial status")
df_all_consumption = pd.read_excel(r"C:\Users\cavazluca1\OneDrive - Ferrero Ecosystem\Desktop\projects\andres coca butter\siloses_all\common datasets\datasets.xlsx", sheet_name = "4 silos")#requires update in consumption and arrival values, ask anna
df_remains_initial = pd.read_excel(r"C:\Users\cavazluca1\OneDrive - Ferrero Ecosystem\Desktop\projects\andres coca butter\siloses_all\common datasets\datasets.xlsx", sheet_name = "initial rest 4 silos")
#removing doubles 

def removeduplicate(data):
    countdict = {}
    for element in data:
        if element in countdict.keys():
            # increasing the count if the key(or element)
            # is already in the dictionary
            countdict[element] += 1
        else:
            # inserting the element as key  with count = 1
            countdict[element] = 1
    data.clear()
    for key in countdict.keys():
        data.append(key)
    return data



#needs some modification in the visual elements
def create_first_visual():
    #slicing for the first 4 weeks
    df_res_4_weeks =  removeduplicate(list(df_result["week"].to_list()))[:4]
    #isolating the first 4 weeks
    df_result_skimmed_4 = df_result[df_result["week"].isin(df_res_4_weeks) & (df_result["cycle_name"] == "unloading")]#["week", "siloses_numbers", "current_filling"] #finding the first four weeks values 
    #create graph with df 
    df_result_skimmed_4_cols = df_result_skimmed_4[["week", "siloses_numbers", "current_filling"]]#isolating teh columns only to include the first week
    #should isolate the first week and then add it to the df , uses week, silos number , current filling
    #generate previous week and year
    number_of_siloses = len( list(df_initial["silos"]))#getting the number of siloses from initial status  
    week_cols = [return_current_previous_week_year() for i in range(number_of_siloses)]

    df_initial_skimmed = df_initial[["silos", "current"]]#only unloading
    #rename columns 
    df_initial_skimmed = df_initial_skimmed.rename(columns={'silos': 'siloses_numbers', 'current': 'current_filling'})
    df_initial_skimmed["week"] = week_cols
    #uniting the two dfs
    union_df = pd.concat([df_initial_skimmed,df_result_skimmed_4_cols])
    
    #graph with teh current filling here , creating a pivot table and then creating a graph on the obtained df 
    #including current week (loading week ) and successive 4
    #    table = pd.pivot_table(df,index=['Description','supplier_code'],values=[col], 'aggfunc='sum, sort=True, margins=True, margins_name='Grand Total')
    pivot_graph = pd.pivot_table(union_df , index = ["week"] ,columns=  ["siloses_numbers"] , values=["current_filling"], aggfunc='sum').reset_index()#values='current_filling', index='week', columns='siloses_numbers'

    #pivot_graph.set_axis(["week", "siloses_numbers", "current_filling"], axis=1)


    ax = pivot_graph.plot(kind='bar', figsize=(12, 6) , width = 0.75)
    plt.title('Current and Expected Utilization per silo')
    #plt.xlabel('Week')
    plt.ylabel('Current Filling (Tons)')
    plt.xticks(rotation=0)  # Keep x-axis labels horizontal
    handles, labels = ax.get_legend_handles_labels()
    custom_labels = [i[1] for i in list(pd.DataFrame(pivot_graph).columns)[1:]]  # Adjust as necessary
    
    plt.legend(handles, custom_labels,title='Silo Number', bbox_to_anchor=(1.05, 1), loc='upper left')
    #custom labels needs to adjust to the weeks 
    #needs the firsat week added 
    custom_labels = [return_current_previous_week_year()[:2]] + [i[:2] for i in df_res_4_weeks]  # Adjust as necessary, using the df_res_4_weeks i get the following ['24_2024', '25_2024', '26_2024', '27_2024']
    #should take the first two letters of each element in the list to create the weeks
    ax.set_xticklabels(custom_labels, rotation=0)
    max_value = 550
    for p in ax.patches:
        height = p.get_height()
        if height > 0:  # Only annotate non-zero bars
            percentage = f'{(height / max_value) * 100:.1f}%'
            ax.annotate(percentage,
                        (p.get_x() + p.get_width() / 2., height),
                        ha='center', va='center', 
                        xytext=(0, 5),  # 5 points vertical offset
                        textcoords='offset points')
    plt.tight_layout()
    #saving fig
    plt.savefig('first_4_weeks_silose.png', bbox_inches='tight', pad_inches=0.1)


create_first_visual()



#the table creation is already done, need to retrieve the necessary info 
def create_second_visual():
    #horizon in weeks is the same, list as the first column 
    df_res_4_weeks =  [return_current_previous_week_year()]+ removeduplicate(list(df_result["week"].to_list()))[:4]
    print(df_res_4_weeks)
    #creating two dfs here for the chosen weeks for loading and unloading
    df_result_skimmed_4_un = df_result[df_result["week"].isin(df_res_4_weeks) & (df_result["cycle_name"] == "unloading")]
    #loading 
    df_result_skimmed_4_loa = df_result[df_result["week"].isin(df_res_4_weeks) & (df_result["cycle_name"] == "loading")]
    #adding the current week 
    #should add a custom line with the vlues representing the curren tweek in both with the same results 

    #@create the new dfs 
    #create a df for loading with relevant columns --> values in df initial status 
    number_of_siloses = len( list(df_initial["silos"]))#getting the number of siloses from initial status  
    week_cols = [return_current_previous_week_year() for i in range(number_of_siloses)]
    silos = list(df_initial["silos"])
    current_filing =  list(df_initial["current"])
    max_col = list(df_initial["max"])
    rest_genova_loading =  [list(df_remains_initial["initial_remaining"])[0] for i in range(number_of_siloses)]
    replacement_cols = [0 for i in range(number_of_siloses)] #column to fill in dummy data 
    cicle_col_load = ["loading" for i in range(number_of_siloses)]
    #adding the columns 
    loading_current_df = {
            "siloses_numbers" : silos,
            "current_status": replacement_cols ,
            "current_filling":  current_filing ,
            "total_filling": max_col,
            "week": week_cols,
            "df_rest_genova": rest_genova_loading,
            "df_rest_needs": replacement_cols,
            "cycle_name": cicle_col_load,
            "loading_counter  " : replacement_cols,
            "unloading_counter":replacement_cols,
            "loaded_current": replacement_cols}

    unloading_current_df = {
            "siloses_numbers" : silos,
            "current_status": replacement_cols ,
            "current_filling":  current_filing ,
            "total_filling": max_col,
            "week": week_cols,
            "df_rest_genova": rest_genova_loading,
            "df_rest_needs": replacement_cols,
            "cycle_name": cicle_col_load,
            "loading_counter  " : replacement_cols,
            "unloading_counter":replacement_cols,
            "loaded_current": replacement_cols}
    
    df_loading = pd.DataFrame(loading_current_df)
    df_unloading = pd.DataFrame(unloading_current_df)
    #adding them together 
    df_result_skimmed_4_unloading = pd.concat([ df_unloading,df_result_skimmed_4_un] )
    df_result_skimmed_4_loading = pd.concat( [df_loading ,df_result_skimmed_4_loa ])


    # creating the series with genova remainings , take full column and then skiop some vvalues
    all_rest = [int(i) for i in list(df_result_skimmed_4_loading["df_rest_genova"])[0:15:3]]
    
    #occupancy column, list comprehension with a simple division creating values
    #creating sum of the capacity using the first df
    all_capacity = sum(list(df_initial["max"]))#should be one single value
    #summing all the values per week in unloading df
    all_weeks_loaded = []
    for i in df_res_4_weeks:
        #all weeks
        current_week = sum(list(df_result_skimmed_4_unloading[df_result_skimmed_4_unloading["week"]==i]["current_filling"])) #should be 3 lines 
        all_weeks_loaded.append(current_week)
    

    #for now i just add a simple list with the numbers to make sure all are covered
    occupancy_column = [i for i in all_weeks_loaded]#['{:.1%}'.format(i/all_capacity) for i in all_weeks_loaded]#4 things here 
    #coverage columns that uses the same current filling 
    all_consumption = list(df_all_consumption["consumption"])
    coverage_column  = []
    #create a dict with the values and the weeks considered 
    all_weeks_loaded_list =list(map(add, all_rest, occupancy_column))#make this a list and sum genova and isotanks
    counter_outer = 0#cover outer is used to update the inside counter  
    #replicating formula COVERWEEKS 
    for i in all_weeks_loaded_list:
        res = coverweek( i, all_consumption, counter_outer)
        coverage_column.append(res)
        counter_outer +=1

    #modifying columns as it couldn t be done before
    df_res_4_weeks_c = [i.replace("_", "-") for i in df_res_4_weeks ]
    #creating a list for teh isotanks quantities, so all in all rest but divided by isotanks quantities 
    all_rest_iso = [int(i/19.4) for i in all_rest ]#i as already integer , we make this an integer so that it is rounded 
    #builing the df for the table ->  DataFrame(dict(s1 = s1, s2 = s2)).reset_index()
    print( "all df columns ", df_res_4_weeks_c, all_rest , all_rest_iso , occupancy_column , coverage_column)
    res_df = pd.DataFrame({"weeks" : df_res_4_weeks_c, "Tons in Genova" : all_rest , "Isotanks" : all_rest_iso ,"In silos (Tons)" : occupancy_column , "Weeks Coverage" : coverage_column})
    #setting index to remove the index column 
   # res_df.set_index(, inplace = True)
    # Apply some styling
    styled_df = res_df.style.background_gradient(cmap='viridis').set_caption('Student Scores')#styling here and then writing later on
    # Render and save the DataFrame as an image
    ax = render_mpl_table(res_df, header_columns=0, col_width=3, row_height=.3)
    plt.savefig('styled_dataframe.png', bbox_inches='tight', pad_inches=0.1)
    
create_second_visual()



def create_quality_table():
    #getting unloading only and ful only 
    df_result_skimmed_4_unloading_all= df_result[(df_result["cycle_name"] == "unloading") & (df_result["current_status"] == "full")]
    #getting unique lists of the siloses 
    all_silos = list(set(df_result_skimmed_4_unloading_all["siloses_numbers"]))
    all_dfs = []
    for i in all_silos:
        df_filtered_silos = df_result_skimmed_4_unloading_all[df_result_skimmed_4_unloading_all["siloses_numbers"]==i]
        #isolate current filling max 
        max_loadingweeks_current = max(list(df_filtered_silos["loading_counter"]))
        print(max_loadingweeks_current, i)
        #isolate rows with max value
        df_filtered_silos_max = df_filtered_silos[df_filtered_silos["loading_counter"] == max_loadingweeks_current]
        #can have a df with different rows , should save it in one list of dicts and then addin all toghether 
        all_dfs.append(df_filtered_silos_max)

    final_df = pd.concat(all_dfs, axis=0, ignore_index=True)[["siloses_numbers", "week", "loading_counter"]]

    # modifying the week format to make it more user friendly 
    week_corrected = [i.replace("_", "-") for i in list(final_df["week"])]
    final_df["week"] = week_corrected 
    #rename teh columns after all
    final_df.rename(columns={'siloses_numbers': 'Silos', 'week': 'Week-Year', 'loading_counter': 'Weeks full'}, inplace=True)

    styled_df = final_df.style.background_gradient(cmap='viridis').set_caption('Student Scores')#styling here and then writing later on
    # Render and save the DataFrame as an image
    ax = render_mpl_table(final_df, header_columns=0, col_width=4.3,row_height=.3)
    plt.savefig('styled_quality.png', bbox_inches='tight', pad_inches=0.1)
    
create_quality_table()


#only lines on the result silos 
def create_andres_graph():
    #isolate loading as the rest is there after loading on the full result
    # the loading is the only one with values  

    loading_only_df = df_result[df_result["cycle_name"] == "loading"]

    l1 = list(loading_only_df["week"])
    l2 = list(loading_only_df["df_rest_genova"])

    res_dict = {k:v for k,v  in zip(l1,l2)}

    #getting the lists back
    all_weeks_single = [i.replace("_", " ") for i in list(res_dict.keys())]#cleaned for output
    all_remains_single = list(res_dict.values())
    # two of the series needed are now created , need for the siloses
    #getting the unoading part 
    unloading_only_df = df_result[df_result["cycle_name"] == "unloading"]
    # unloading has the last pic, so i can create series byu sicing the unloading full df for each silos
    #getting all the siloses numbers 
    all_siloses = list(set(unloading_only_df["siloses_numbers"])) #all siloses tha are unique
    values_list = {}
    for i in all_siloses:
        series_values = unloading_only_df[unloading_only_df["siloses_numbers"]==i]["current_filling"]
        values_list[i]=series_values #it is now a dict

    #plotting all
    #x_labels as the values on the x    
    #the list of series is series values 
#   Create a plot
    fig, ax = plt.subplots(figsize=(20, 12))    

    # Plot each series in the series_dict
    for name, series in values_list.items():
        ax.plot(all_weeks_single, series, label=name)

    # Plot the additional series with area fill
    ax.fill_between(all_weeks_single, all_remains_single, color='sandybrown', alpha=0.4, label='Quantity at Genova (Tons)')

    # Set x-axis labels
    ax.set_xticks(range(len(all_weeks_single)))
    ax.set_xticklabels(all_weeks_single)

    # Rotate x-axis labels to be vertical
    plt.xticks(rotation=90)

    # Set labels and title
    ax.set_xlabel("Weeks considered")
    ax.set_ylabel("Tons")
    ax.set_title("Siloses Cycles Projection")

    # Show legend with series names
    ax.legend(prop={'size': 17})
 # Choose the week to highlight
    highlight_week = return_current_week_year()  # Example week to highlight, replace with your desired week
    highlight_index = all_weeks_single.index(highlight_week.replace("_", " "))

    # Add a vertical line at the chosen week
   # Define the limits for the vertical line
    y_min, y_max = ax.get_ylim()
    line_start = y_min + 50
    line_end = y_max * 0.9  # Adjust the 0.9 value to stop the line sooner

    # Add a vertical line at the chosen week with adjusted height
    ax.vlines(x=highlight_index, ymin=line_start, ymax=line_end, color='red', linestyle='--', linewidth=2)

    # Add annotation pointing out the chosen week
    ax.annotate('Current Week', xy=(highlight_index, max(max(all_remains_single), max([max(series) for series in values_list.values()]))),
                xytext=(highlight_index, max(max(all_remains_single), max([max(series) for series in values_list.values()])) + 10),
                #arrowprops=dict(facecolor='black', shrink=0.05),
                fontsize=12, color='red', ha='center')

    # save the plot
    plt.savefig('Andres_graph.png', bbox_inches='tight', pad_inches=0.1)


create_andres_graph()


