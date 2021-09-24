import numpy as np
import pandas as pd
import os

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

def pick_target(df, target):
    """creates a small df with only one column from id file which will serve as a target variable"""
    target_var_df = df[['ID', target]]
    return target_var_df


def create_X_y(data_directory_path, ID_file_path, target_var):
    """given data directory path returns a data set in form of X and y variables, where X is the big Dataframe with
     independent variables and y is a Series with target variables"""
    df_2 = create_target_var_df(ID_file_path)
    target_df = pick_target(df_2, target_var)
    dataframes = make_dataframes(data_directory_path)
    df_1 = merge_dataframes(dataframes)
    big_df = df_1.merge(target_df, on='ID')

    y = big_df[target_var]
    X = big_df.drop([target_var, 'ID'], axis=1)
    return X,y

