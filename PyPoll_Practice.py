#Star at 3.3.3
# The data we need to retrieve:
"""
1 - Total number of votes cast
2 - A complete list of candidates who received votes
3 - Total number of votes each candidate received
4 - Percentage of votes each candidate won
5 - The winner of the election based on popular vote
"""


""" import csv #Import csv module
dir(csv)   #Display functions under csv module

file_to_load = 'Resources\election_results.csv'

# Method 1: open() and read data then close it
# Open the election results and read the file.
#election_data = open(file_to_load, 'r')

### Perform Analysis Here

# Close the file
#election_data.close()


## Method 2: use with which does not recquire clsoing the file after
with open(file_to_load) as election_data:
        ### Perform Analysis Here
        print(election_data)
 """

## Indirect path to the file usin import os

import csv
import os #import the module
# dir(os)   #path is a submodule of os
# dir(os.path) #look at path functions

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file
with open(file_to_load) as election_data:
        # Print the file object
        print(election_data)


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysispp.txt")

# Using the open() function with the "w" mode we will write data to the file.
outfile = open(file_to_save, "w")

# Write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close()


##using with
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
     # Write three counties to the file.
     #txt_file.write("Arapahoe, ")
     #txt_file.write("Denver, ")
     #txt_file.write("Jefferson")
     txt_file.write("Counties in the Election\n")
     txt_file.write("-------------------------\n")
     txt_file.write("Arapahoe\nDenver\nJefferson")
