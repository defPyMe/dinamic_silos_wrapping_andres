import pandas as pd

#consumption arrival values 
df_cons_arr = pd.read_excel(r"C:\Users\cavazluca1\OneDrive - Ferrero Ecosystem\Desktop\projects\andres coca butter\siloses_all\common datasets\datasets.xlsx", sheet_name="4 silos")
#initial status values
df_initial_statuses = pd.read_excel(r"C:\Users\cavazluca1\OneDrive - Ferrero Ecosystem\Desktop\projects\andres coca butter\siloses_all\common datasets\datasets.xlsx", sheet_name="4 silos initial status")
#getting the rest
df_rest = pd.read_excel(r"C:\Users\cavazluca1\OneDrive - Ferrero Ecosystem\Desktop\projects\andres coca butter\siloses_all\common datasets\datasets.xlsx", sheet_name="initial rest 4 silos")
# calculating the cons arrival
all_weeks = [str(i) for i in df_cons_arr["week num"].to_list()]
all_cons = df_cons_arr["consumption"].to_list()
all_needs = df_cons_arr["arrival"].to_list()
zipped = zip(all_cons, all_needs)
#final result
dict_consumption_arrival = { k:v for (k,v) in zip(all_weeks, zipped)} 
#calculating the initial stauts 


all_siloses_values = [df_initial_statuses.loc[i].to_list()[1:] for i in range(df_initial_statuses.shape[0])]#, df_initial_statuses.loc[1].to_list()[1:], df_initial_statuses.loc[2].to_list()[1:],df_initial_statuses.loc[3].to_list()[1:]  ]


all_siloses_numbers = df_initial_statuses["silos"].to_list()

#result initial status 
ex =  { k:v for (k,v) in zip(all_siloses_numbers,all_siloses_values)} 
#results initial remainings
initial_remaining = df_rest.loc[0][0]
initial_needs = df_rest.loc[0][1]









