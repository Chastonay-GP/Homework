# Create a main script and 1 functions
# The function: it should read a precipitation file (path provided as an argument),
# extract the data and return only the precipitation data as a list or Numpyarray.
# The script: it should call the function and display to the user:
# The min precipitation
# The max precipitation
# The mean precipitation

#Open the file
file = open("C:/Users/jonas/PycharmProjects/data/V3_precip_data.txt", "r") # 'r' says we are opening the file to read, infile is the opened file object that we will read from

#Store the data from the file in a variable
precipitation_data = file.read()

#Print the data in the file
print(precipitation_data)

#close the file
file.close()

