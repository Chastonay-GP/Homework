# Create a main script and 1 functions
# The function: it should read a precipitation file (path provided as an argument),
# extract the data and return only the precipitation data as a list or Numpyarray.
# The script: it should call the function and display to the user:
# The min precipitation
# The max precipitation
# The mean precipitation

import pandas as pd


# Open the file

def precifun():
    df = pd.read_fwf("C:/Users/jonas/PycharmProjects/data/precip_data.txt")
    print(df)
    precip_list = df["rre150d0"]
    print(precip_list)

precifun()

precip_max = max(precip_list)
precip_min = min(precip_list)
precip_mean = np.mean(precip_list)
print(precip_max)
print(precip_min)
print(precip_mean)
