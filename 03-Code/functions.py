import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def make_df(file):
    """accepts the xLs file and transforms it into a tidy dataframe with undestandable variables"""
    df = pd.read_excel(file)

    wanted = ['Unnamed: 0', 'Aktivität', 'Schritte', 'Regulärer Rhythmus', 'Sinusrhythmus', '∆(NN)', 'Ø(RR)',
              'HRV Index', 'QTc',
              'Schlafphase', 'Atemfrequenz', 'Atemtiefe']

    translation = ['Timepoint', 'Activity', 'Steps', 'Regular Heartrythm', 'Sinusrythm', '∆(NN)', 'Ø(RR)', 'HRV Index',
                   'QTc',
                   'Sleep-phase', 'Breathing (frequency)', 'Breath depth']

    df2 = df[wanted]
    df2.columns = translation
    # saving units from first row and getting rid of them
    units = df2.iloc[0]
    df2 = df2.drop([0])
    # creating column names with units next to them where possible
    new_translation = []
    counter = 0
    units = units.fillna(0)
    for t in translation:
        if units[counter] != 0:
            new_t = t + ' ' + '(' + str(units[counter]) + ')'
            new_translation.append(new_t)
        else:
            new_translation.append(t)
        counter += 1
    df2.columns = new_translation
    df2.reset_index(inplace=True)
    df2.drop([0], inplace=True)
    df2.reset_index(inplace=True)
    df2.drop(['level_0', 'index'], axis=1, inplace=True)

    df2['Timepoint'] = pd.to_datetime(df2['Timepoint'], format='%H:%M:%S')
    return df2

def z_normalize(series, df):
    """does Z-Score normalization on a series and adds this column to df"""
    n = (series - series.mean()) / series.std()
    df[f'{series.name} norm'] = n

def plot_two(var1, var2, df, color1='red', color2='blue'):
    """plots 2 variables with different scales, against time, on the same plot"""
    fig, ax = plt.subplots()
    ax.plot(df['Timepoint'], df[var1], color=color1)
    ax.set_xlabel("tempus fugit")
    ax.set_ylabel(var1, color=color1)
    ax2 = ax.twinx()
    ax2.set_ylabel(var2, color=color2)
    ax2.plot(df['Timepoint'], df[var2], color=color2)