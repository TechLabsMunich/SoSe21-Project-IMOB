import os
import pandas as pd
import numpy as np

import functions as f
path = '/Users/Mikolaj/PycharmProjects/SoSe21-Project-IMOB/01-Data/no_drug'




#test - how to build a DataFrame with a list as a cell
# list_1 = [['a','b','c','d']]
# list_2 = [['e','f','g','h']]
# df2 = pd.DataFrame({'list_1':list_1, 'list_2':list_2})
# print(df2)

print(f.make_dataframes(path))

