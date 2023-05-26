import functions as f
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import os
import itertools

file = "../01-Data/new data's IDs.xlsx"
interesting_variables = ['Alter ', 'Gewicht', 'Größe']

df = f._create_target_var_df(file)
df_2 = df[interesting_variables]
median = df_2['Gewicht'].median()
print(median)


# df_2['Alter>49'] = df_2['Alter '] >= median
# # if [df_2['Alter '] > median]:
# #     df_2['Alter>49'] =1
#
# print(df_2['Alter>49'])
# df_2['Alter>49']
# print(df_2['Alter>49'])
# for x in df_2['Alter ']:
#     if x >= median:
#         df_2['Alter>49'] = 1
# df_2['age_decade'] = (df_2['Alter ']//10)*10
# df_2['weight_decade'] = (df_2['Gewicht']//10)*10

# df = f._xls_to_df("../01-Data/new_data/P1.xlsx")
# for type in df.dtypes:
#     print(type)
# for c in df.columns:
#     print(f'{c}={c.d_type()}')

# print(f._create_target_var_df("../01-Data/new data's IDs.xlsx")['Alter '])
print(f.find_columns_to_ditch('../01-Data/new_data'))