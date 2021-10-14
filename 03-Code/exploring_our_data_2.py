import functions as f
import pandas as pd
import numpy as np


from sktime.datatypes._panel._convert import (
    from_2d_array_to_nested,
    from_nested_to_2d_array,
    is_nested_dataframe,
)

print(f._xls_to_df('../01-Data/sample_data/P1.xlsx'))