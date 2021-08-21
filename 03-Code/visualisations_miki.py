import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import datetime

import functions as f

file = '../01-Data/XLS.xls'
# df = f.make_df(file)


# mask = (df['Timepoint'] == 'Gesamt')




#doing z-score normalization on breathing (frequency) (/Min) and Breath depth
# breathing_freq_norm = ((df['Breathing (frequency) (/Min)'] - df['Breathing (frequency) (/Min)'].mean())/df['Breathing (frequency) (/Min)'].std())
# breathing_depth_norm = ((df['Breath depth'] - df['Breath depth'].mean())/df['Breath depth'].std())
#
# df['Breathing Freq norm'] = pd.Series(breathing_freq_norm)
# df['Breathing depth norm'] = pd.Series(breathing_depth_norm)

# plotting nromalized breathing rate and breathing depth to time
# df.plot('Timepoint',['Breathing depth norm', 'Breathing Freq norm'])
# print(df['Breathing depth norm'].max())
# print(df['Breathing Freq norm'].max())

#plotting timepoint to heartrate
# print(df.columns)
# figure, axes = plt.subplots(nrows=1, ncols=2)
# axes[0].plot(df['Timepoint'],df['Ø(RR) (ms)'])
# axes[1].plot(df['Timepoint'],df['Breathing (frequency) (/Min)'])
# fig1 = df.plot('Timepoint', 'Ø(RR) (ms)')
# plt.title('R-R')
# fig2 = df.plot('Timepoint','Breath depth')
# fig3 = df.plot('Timepoint', 'QTc (ms)')
# fig4 = df.plot('Timepoint', 'Steps (/Min)')
# f.z_normalize(df['Steps (/Min)'], df)

# fig5 = df.plot('Timepoint', ['Breathing Freq norm', 'Steps (/Min) norm'])
# df.plot('Timepoint','Activity')

# fig, ax = plt.subplots()
# ax.plot(df['Timepoint'], df['HRV Index'], color = "red")
# ax.set_xlabel("tempus fugit")
# ax.set_ylabel("HRV Index", color = "red")
# ax2=ax.twinx()
# ax2.set_ylabel("Activity", color = "blue")
# ax2.plot(df['Timepoint'], df['Activity'], color="blue")

# f.plot_two('QTc (ms)', 'Breath depth', df)
# f.plot_two('Activity','Steps (/Min)', df)
# plt.show()

df = pd.read_excel(file)
for column in df.columns:
    print(column)