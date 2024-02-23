

import dataiku
from dataiku import pandasutils as pdu
import pandas as pd

# Example: load a DSS dataset as a Pandas dataframe
mydataset = dataiku.Dataset("mydataset")
mydataset_df = mydataset.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Recipe outputs
test_output = dataiku.Dataset("test_output")
test_output.write_with_schema(pandas_dataframe)