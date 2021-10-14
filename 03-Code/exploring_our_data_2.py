import functions as f
import pandas as pd
import numpy as np


from sktime.datatypes._panel._convert import (
    from_2d_array_to_nested,
    from_nested_to_2d_array,
    is_nested_dataframe,
)

# df = f._xls_to_df("../01-Data/new_data/P1.xlsx")
# for type in df.dtypes:
#     print(type)
# for c in df.columns:
#     print(f'{c}={c.d_type()}')

# print(f._create_target_var_df("../01-Data/new data's IDs.xlsx")['Alter '])
print(f.find_columns_to_ditch('../01-Data/new_data'))
