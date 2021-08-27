import os
import pandas as pd
import numpy as np



path = '/Users/Mikolaj/PycharmProjects/SoSe21-Project-IMOB/01-Data/euthyrox'
files_list = os.listdir(path)
path_1 = path +'/M1.xls'
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

print(xls_to_df(path_1))
#test - how to build a DataFrame with a list as a cell
# list_1 = [['a','b','c','d']]
# list_2 = [['e','f','g','h']]
# df2 = pd.DataFrame({'list_1':list_1, 'list_2':list_2})
# print(df2)


