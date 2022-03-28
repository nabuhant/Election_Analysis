# Election_Analysis
Module3_Python

# Overview of Election Audit
## Background
Tom, a Colorado Board of Elections employee, needs assistance auditing the tabulated results for U.S Congressional elections. In the audit, the following data needs to be reported:  
**1 -** Total number of votes cast in the election.  
**2 -** A complete list of candidates who received votes, total of number of votes received, and percentage out of total votes.  
**3 -** A complete list of counties where voting occurred, total number of votes from the county, and percentage out of total votes.  
**4 -** The county with the largest voter turnout.  
**5 -** The winner of the election based on popular vote, winning vote count and percentage.  

## Purpose
The purpose of carrying out this project using Python is to automate the auditing process for this election and other elections with the same data format. To automate the process, Python is used to open and read from a file (a CSV file specifically), create dictionaries and list to hold county and candidate names and their respective counts accounted for in for loops and conditional statements with logical/membership operators, and finally, the results are printed to the terminal and written/saved to a text file.


# Election-Audit Results
Using a bulleted list, address the following election outcomes. Use images or examples of your code as support where necessary.
* In total, 369,711 votes were cast in this congressional election. The code below was used to open the election_results.CSV file, count the number of rows in the file skipping the header row.
```python
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    # Read the header
    header = next(reader)
    # For each row in the CSV file.
    for row in reader:
        # Add to the total vote count
        total_votes = total_votes + 1
```
* The number of votes and the percentage of total votes for each county in the precinct is: 
  * Jefferson: 10.5% (38,855)
  * Denver: 82.8% (306,055)
  * Arapahoe: 6.7% (24,801)  

The code below was used to obtain the county names list (step 3 & 4). It also counted the total votes for each county (step 5)  
```python
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # For each row in the CSV file.
    for row in reader:
        # 3: Extract the county name from each row.
        county_name = row[1]

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:
            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)
            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0
            
        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1
```
The code below was used to obtain the vote count and calculate the percentage for each county. Then it saved the results to a text file.
```python
    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_options:
        # 6b: Retrieve the county vote count.
        cvotes = county_votes[county_name]
        # 6c: Calculate the percentage of votes for the county.
        cvotes_percentage = float(cvotes) / float(total_votes) * 100

         # 6d: Print the county results to the terminal.
        county_results = (
            f"{county_name}: {cvotes_percentage:.1f}% ({cvotes:,})")
        print(county_results)
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results + "\n")
```
* The county with the largest number of votes is Denver with 306,055 votes (82.8% of total voter turnout).
* The number of votes and the percentage of total votes for each candidate in the election is: 
  * Charles Casper Stockham: 23.0% (85,213)
  * Diana DeGette: 73.8% (272,892)
  * Raymon Anthony Doane: 3.1% (11,606)  
The code used to obtain these results is similar in logic as the code used to obtain the county results.
* The winner of the election is Diane DeGette with a vote count of 272,892 and a percentage of the total votes of 73.8%.

The images below are screenshots of the terminal and saved text results
| Terminal Results | Text File Results |
| :---: | :---:|
|![image1](/TerminalResults.PNG) | ![image2](/TextResults.PNG) |

# Election-Audit Summary
This script can be used for any election with some modifications. For example, one can include more counties (or any other area type) and candidate names in the raw data and the script will still present the same results and breakdown. Also, this script can be modified to demonstrate the vote count for every candidate within an area along with the overall count in the election. This will demonstrate the area's political inclinations and views which will be useful for future elections.
