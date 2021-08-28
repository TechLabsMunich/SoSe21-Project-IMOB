import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os


def xls_to_df(path):
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
            df = xls_to_df(file_path)
            dataframes.append(df)
        except OverflowError:
            continue
        #print function just for debugging purposes to see which files are going through and which do not
        print(filename)
    return dataframes