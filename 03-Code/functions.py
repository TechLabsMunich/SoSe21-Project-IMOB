import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os

# target_var_file_path = "../01-Data/new data's IDs.xlsx"
def create_target_var_df(path):
    """creates target var df from which one can later pick the target he wants and merge it to final df"""
    data_id = pd.read_excel(path)
    data_id.dropna(subset=['ID'], inplace=True)
    # dealing with dumb P's
    better_ids = []
    for x in data_id['ID']:
        l = list(x)
        del l[0]
        s = ('').join(l)
        n = int(s)
        better_ids.append(n)
    data_id['ID'] = better_ids
    # sorting the table
    data_id.sort_values(by=['ID'], inplace=True)
    data_id = data_id.reset_index()
    data_id.drop(['index'], axis=1, inplace=True)

    return data_id


def _xls_to_df(path):
    """When provided with our .xls file produces a dataframe with only one row of lists in each column.
    Columns' names stay the same."""
    #prepare starter dataframe
    df = pd.read_excel(path)
    df.drop([0], inplace=True)
    df.reset_index(inplace=True)
    df.drop(['index'],axis=1, inplace=True)
    #start making the wanted dataframe
    d = {}
    for c in df.columns:
        #this is a weird way of getting to the goal. It is a list in a list but it does not work otherwise for me.
        l = []
        l.append(df[c].tolist())
        d[c] = l
    df2 = pd.DataFrame(d)
    df2.columns = df.columns
    #dropping the time column
    df2.drop(['Unnamed: 0'], axis =1, inplace =True)

    #putting in ID column from name of the file
    path_list = path.split('/')
    filename = path_list[-1]
    p= filename.split('.')
    p_number = p[0]
    l=list(p_number)
    del l[0]
    s = ('').join(l)
    n=int(s)
    new_columns = ['ID']
    for a in df2.columns:
        new_columns.append(a)
    df2['ID'] = n
    df2=df2.reindex(columns = new_columns)

    return df2


def make_dataframes(directory_path):
    """given directory path with xls files, creates a list of dataframes that we need"""
    dataframes = []
    files_list = os.listdir(directory_path)
    files_list.sort()
    for filename in files_list:
        file_path = directory_path+'/'+filename
        df = _xls_to_df(file_path)
        dataframes.append(df)
    return dataframes


def merge_dataframes(dataframes, target_var_df, target_var):
    """provided a list of dataframes and name of target variable creates one concated dataframe with additional column target"""
    new_df = pd.concat(dataframes, ignore_index = True)
    small_target_var_df = target_var_df[['ID', target_var]]
    new_df = new_df.merge(small_targer_var_df, on='ID')
    return new_df


# def merge_sets(dataframes):
#     """concats dataframes from different drug groups"""
#     new_df = pd.concat(dataframes, ignore_index = True)
#     return new_df


def create_X_y(directory_path):
    """given data directory path returns a data set in form of X and y variables, where X is the big Dataframe with
     independent variables and y is a Series with target variables"""
    folder_list = os.listdir(directory_path)
    merged_dataframes =[]
    for folder in folder_list:
        #in case there are some normal or hidden files in the data_directory
        try:
            small_dataframes = make_dataframes(directory_path+'/'+folder)
            merged_dataframe = merge_dataframes(small_dataframes, folder)
            merged_dataframes.append(merged_dataframe)
        except NotADirectoryError:
            continue
    big_df = merge_sets(merged_dataframes)
    y = big_df['Target']
    X = big_df.drop(['Target'], axis=1)

    return X, y

z = make_dataframes('../01-Data/new_data')
print(z)