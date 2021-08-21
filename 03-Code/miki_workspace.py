import os
import pandas as pd
import numpy as np

path = '/Users/Mikolaj/PycharmProjects/SoSe21-Project-IMOB/01-Data'
files_list = os.listdir(path)
heart_rate_series = []

for file_name in files_list:
    f_path = path+"/"+file_name
    dfx = pd.read_excel(f_path)
    wanted_column = 'Ø(rr-HR)'
    series = dfx[wanted_column]
    heart_rate_series.append(series)
print(heart_rate_series)


