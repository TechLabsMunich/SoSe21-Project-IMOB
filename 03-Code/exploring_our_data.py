import functions as f
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import os
import itertools

file = '../01-Data/new_data/P1.xlsx'



#problem 1:
#finding out how much of nan we have in various columns what to do with particular columns - drop completely or fill  with values
#finding out timepoint where all patients are actually doing measurements - some started at 12 and some started at 9 - how to

df = pd.read_excel(file)
df.drop([0], inplace=True)
df.reset_index(inplace=True)
df.drop(['index'], axis=1, inplace=True)
df.drop([0], inplace=True)
df.reset_index(inplace=True)
df.drop(['index'], axis=1, inplace=True)

number_of_nans = {}
columns_to_ditch = []
for column in df.columns:
    number_of_nans[column] = df[column].isna().sum()
    if number_of_nans[column] >500:
        columns_to_ditch.append(column)
    print(f'{column} = {df[column].isna().sum()}')

#shows nicely peaks where we have to much NA
# plt.bar(number_of_nans.keys(), number_of_nans.values())
# plt.show()
print(columns_to_ditch)

#check if in other files these would be the same columns
def find_columns_to_ditch(directory):
    """depending on the files there will be different columns to ditch. It filters for names of any column in the
    folder where NaN was above 300"""
    columns_to_ditch_multiple = []
    folder_path = '../01-Data/'+'/'+directory
    files = os.listdir(folder_path)
    for file in files:
        filepath = folder_path +'/'+ file

        df = pd.read_excel(filepath)

        df.drop([0], inplace=True)
        df.reset_index(inplace=True)
        df.drop(['index'], axis=1, inplace=True)
        df.drop([0], inplace=True)
        df.reset_index(inplace=True)
        df.drop(['index'], axis=1, inplace=True)

        number_of_nans = {}
        columns_to_ditch = []
        for column in df.columns:
            number_of_nans[column] = df[column].isna().sum()
            if number_of_nans[column] >300:
                columns_to_ditch.append(column)
        columns_to_ditch_multiple.append(columns_to_ditch)
    merged = list(itertools.chain.from_iterable(columns_to_ditch_multiple))
    merged_set = set(merged)
    merged_list = list(merged_set)
    return merged_list

columns_to_ditch = find_columns_to_ditch('sample_data')

def ditch_columns(df, columns_to_ditch):
    df.drop(columns_to_ditch, axis=1, inplace=True)
    return df
# print(df.shape)
# print(ditch_columns(df, columns_to_ditch).shape)

#find out which columns have also missing values:
df_2 = ditch_columns(df, columns_to_ditch)
for c in df_2.columns:
    if df_2[c].isnull().values.any():
        print(c)

#next step fill them from the bottom up with the same value as before measured and check if the ML algorithm works afterwards