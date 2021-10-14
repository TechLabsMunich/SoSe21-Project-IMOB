







# import pandas as pd
# import numpy as np
# "../01-Data/new data's IDs.xlsx"
# data_id = pd.read_excel("../01-Data/new data's IDs.xlsx")
# data_id.dropna(subset = ['ID'], inplace=True)
# #dealing with dumb P's
# better_ids = []
# for x in data_id['ID']:
#     l=list(x)
#     del l[0]
#     s = ('').join(l)
#     n=int(s)
#     better_ids.append(n)
# data_id['ID']=better_ids
#
# #sorting the table
# data_id.sort_values(by=['ID'], inplace=True)
# data_id = data_id.reset_index()
# data_id.drop(['index'], axis=1, inplace=True)
# pd.set_option("display.max_rows", None, "display.max_columns", None)
# print(data_id)



## GOOD BUT UNUSED CODE IF WE WERE TO COME BACK TO PREVIOUS CONCEPT WITH FOLDER NAMES
# files_list.sort()
# for filename in files_list:
#     file_path = directory_path+'/'+filename
#     df = _xls_to_df(file_path)
#     dataframes.append(df)

# return big_df
# folder_list = os.listdir(directory_path)
# merged_dataframes =[]
# for folder in folder_list:
#     #in case there are some normal or hidden files in the data_directory
#     try:
#         small_dataframes = make_dataframes(directory_path+'/'+folder)
#         merged_dataframe = merge_dataframes(small_dataframes, folder)
#         merged_dataframes.append(merged_dataframe)
#     except NotADirectoryError:
#         continue
# big_df = merge_sets(merged_dataframes)