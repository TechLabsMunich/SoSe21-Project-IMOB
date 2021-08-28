import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os


def _xls_to_df(path):
    """When provided with our .xls file produces a dataframe with only one row of lists in each column.
    Columns' names stay the same."""
    #prepare old the starter dataframe
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
    return df2



def make_dataframes(directory_path):
    """given directory path with xls files, creates a list of dataframes that we need"""
    dataframes = []
    files_list = os.listdir(directory_path)
    files_list.sort()
    for filename in files_list:
        #no idea why it does not work. gives OverflowError
        try:
            file_path = directory_path+'/'+filename
            df = _xls_to_df(file_path)
            dataframes.append(df)
        except OverflowError:
            continue
        #print function just for debugging purposes to see which files are going through and which do not
        # print(filename)
    return dataframes

def merge_dataframes(dataframes, target_var):
    """provided a list of dataframes and name of target variable creates one concated dataframe with additional column target"""
    new_df = pd.concat(dataframes, ignore_index = True)
    new_df['Target'] = target_var
    return new_df

def merge_sets(dataframes):
    """concats dataframes from different drug groups"""
    new_df = pd.concat(dataframes, ignore_index = True)
    return new_df



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
