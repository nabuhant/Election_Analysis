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
from functools import total_ordering
import os #import the module

# os.path.join explanation: https://www.geeksforgeeks.org/python-os-path-join-method/
# Assign a variable to load the csv results file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the results file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initializa a total vote counter
total_votes = 0

# Initialize candidate list
candidate_options = []

# Declare the empty dictionary (names and votes will be stored there)
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and the read the file
with open(file_to_load) as election_data:
        # To do: read and analyze the data here.
        file_reader = csv.reader(election_data)
        # Print each row in the CSV file.
        #for row in file_reader:
                #print(row) #headers and columns not seen when printed (too quick) & each row is a list

        # Read and print the header row
        headers = next(file_reader) # next returns the next item/row/iterator in the list (comment out for and print)
        # print(headers)

        # Add each row to the total vote count after skipping the header
        for row in file_reader:
                total_votes += 1
                
                # Print the candidate name from each row
                candidate_name = row[2]
                
                # If the candidate does not match any existing candidate (unique names)
                if candidate_name not in candidate_options:
                        # Add the candidate name to the candidate list
                        candidate_options.append(candidate_name)

                        # Begin tracking that candidate's vote count
                        candidate_votes[candidate_name] = 0  ## dictionary_name[key]

                # Add a vote to that candidate's count
                candidate_votes[candidate_name] += 1
        

# Print the total votes
print("The total votes are "+str('{:,}'.format(total_votes))) #369,711
# Print the candidate options
print(candidate_options)
# Print the candidate vote dictionary
print(candidate_votes)
        ## {'Charles Casper Stockham': 85213, 'Diana DeGette': 272892, 'Raymon Anthony Doane': 11606}

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list
for candidate_name in candidate_options:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = (float(votes)/float(total_votes)) * 100
        #vote_percentage = "{:.1f}".format(vote_percentage)
        # 4. Print the candidate name and percentage of votes.
        #print(f"{candidate_name}: received {vote_percentage}% of the vote.")
        # To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
                # If true then set winning_count = votes and winning_percent = vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage
                # And, set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name
candidate_votes[candidate_name] += 1

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)