import numpy as np
import pandas as pd
import os
import itertools
from settings import Settings

#imports for nesting the dataframe
from sktime.datatypes._panel._convert import (
    from_2d_array_to_nested,
    from_nested_to_2d_array,
    is_nested_dataframe,
)

settings = Settings()

def _xls_to_df(path):
    """When provided with our .xls file produces a dataframe with only one row of lists in each column.
    Columns' names stay the same."""
    #prepare starter dataframe
    df = pd.read_excel(path)
    df.drop([0], inplace=True)
    df.reset_index(inplace=True)
    df.drop(['index'],axis=1, inplace=True)
    df.drop(['Unnamed: 0'], axis =1, inplace =True)
    #make it of a standard length
    df = df[0:settings.standard_length]
    #fill columns which have less nans than amount stated in Settings
    for column in df.columns:
        if (df[column].isna().sum() <= settings.nan_limit) and (df[column].isna().sum()>0):
            df[column].ffill(inplace=True)
            #dealing with the eventual nans on the top of the columns
            df[column].bfill(inplace=True)
    #change data type to float64 in every column
    df = df.astype(np.float64)

    #start making the wanted nested dataframe
    X_nested = from_2d_array_to_nested(df.transpose())
    X_nested = X_nested.transpose()
    #test the nesting of the dataframe
    # print(f"X_nested is a nested DataFrame: {is_nested_dataframe(X_nested)}")
    # print(f"The cell contains a {type(X_nested.iloc[0, 0])}.")
    # print(f"The nested DataFrame has shape {X_nested.shape}")
    X_nested.columns = df.columns

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
    for a in X_nested.columns:
        new_columns.append(a)
    X_nested['ID'] = n
    X_nested=X_nested.reindex(columns = new_columns)

    return X_nested


#dealing with large NaNs
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
            if number_of_nans[column] > settings.nan_limit:
                columns_to_ditch.append(column)
        columns_to_ditch_multiple.append(columns_to_ditch)
    merged = list(itertools.chain.from_iterable(columns_to_ditch_multiple))
    merged_set = set(merged)
    merged_list = list(merged_set)
    return merged_list


def ditch_columns(df, columns_to_ditch):
    """ditches columns from provided list"""
    df.drop(columns_to_ditch, axis=1, inplace=True)


def make_dataframes(directory_path):
    """given directory path with xls files, creates a list of dataframes using _xls_to_df() function"""
    dataframes = []
    files_list = os.listdir(directory_path)
    for f in files_list:
        df = _xls_to_df(directory_path+'/'+f)
        dataframes.append(df)

    return dataframes


def merge_dataframes(dataframes):
    """provided a list of dataframes and name of target variable creates one concated dataframe with additional column target"""
    new_df = pd.concat(dataframes, ignore_index = True)
    new_df.sort_values(by=['ID'], inplace=True)
    new_df = new_df.reset_index()
    new_df.drop(['index'], axis=1, inplace=True)
    return new_df

def _create_target_var_df(path):
    """creates target var dataframe from which one can later pick the target he wants and merge it to final df"""
    data_id = pd.read_excel(path)
    #dropping completely empty rows
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
    data_id['Alter>median'] = data_id['Alter '] >= settings.age_median
    data_id['Weight>median'] = data_id['Gewicht'] >= settings.weight_median
    return data_id

def pick_target(df, target):
    """creates a small df with only one column from id file which will serve as a target variable"""
    target_var_df = df[['ID', target]]
    return target_var_df


def create_X_y(data_directory_path, ID_file_path, target_var):
    """given data directory path returns a data set in form of X and y variables, where X is the big Dataframe with
     independent variables and y is a Series with target variables"""
    #create one colum of target variable
    df_2 = _create_target_var_df(ID_file_path)
    target_df = pick_target(df_2, target_var)
    #find which columns to ditch
    columns_to_ditch = find_columns_to_ditch(data_directory_path)
    #create many one liners dataframes
    dataframes = make_dataframes(data_directory_path)
    #merge the dataframes with each other
    df_1 = merge_dataframes(dataframes)
    #ditch the columns from df_1
    ditch_columns(df_1, columns_to_ditch)
    #concat big dataframe with dataframe containing target variables
    big_df = df_1.merge(target_df, on='ID')
    #define what is indpendent what is target variables
    y = big_df[target_var]
    X = big_df.drop([target_var, 'ID'], axis=1)

    return X,y

