import functions as f

#GETTING THE X AND Y PART:

data_path = '../01-Data/sample_data'
id_path = "../01-Data/new data's IDs.xlsx"
target_variable = 'Ruhepuls'

X, y = f.create_X_y(data_path, id_path, target_variable)

#MACHINE LEARNING PART:


