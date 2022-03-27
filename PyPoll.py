#Start at 3.4.4
# The data we need to retrieve:
"""
1 - Total number of votes cast
2 - A complete list of candidates who received votes
3 - Total number of votes each candidate received
4 - Percentage of votes each candidate won
5 - The winner of the election based on popular vote
"""

# Add our dependencies.

import csv
import os #import the module

# os.path.join explanation: https://www.geeksforgeeks.org/python-os-path-join-method/
# Assign a variable to load the csv results file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the results file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")


# Open the election results and the read the file
with open(file_to_load) as election_data:
        # To do: read and analyze the data here.
        file_reader = csv.reader(election_data)
        # Print each row in the CSV file.
        for row in file_reader:
                print(row) #headers and columns not seen when printed (too quick) & each row is a list

                # Read and print the header row
                headers = next(file_reader) # next returns the next item/row/iterator in the list (comment out for and print)
                print(headers)