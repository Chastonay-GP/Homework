# Create a main script and 1 functions
# The function: it should read a precipitation file (path provided as an argument),
# extract the data and return only the precipitation data as a list or Numpyarray.
# The script: it should call the function and display to the user:
# The min precipitation
# The max precipitation
# The mean precipitation

import pandas as pd
import numpy as np

# Open the file

def precifun():
    df = pd.read_table("C:/Users/jonas/PycharmProjects/data/precip_data.txt",sep=" ")
    print(df)
    percip_list = df["rre150d0"].tolist()
    print(percip_list)

precifun()
