from operator import irshift


print ("Hello World!!")

# 3.2.4 Lists

my_list = list() #declaring an empty list that will be filled later

counties = ["Arapahoe", "Denver", "Jefferson"]
counties[0]

#bottom print statements refer to same element in list
print (counties[2])
print(counties[-1])

len(counties) #length of list

##Slicing

## Add items to list
#to end -> use append
counties.append("El Paso")
#to specific location -> use listname.insert(index, obj)
counties.insert(2, "El Paso")

##Remove items from a list
counties.remove("El Paso") #removes first matching item

counties.pop(2)#removes at index passed

#Change an Element in a List
counties[2]="El Paso"

#question
counties.insert(2, "El Paso")
counties.pop(0)

##### 3.2.5 Tuples

counties_tuple = ("Arapahoe","Denver","Jefferson")
len(counties_tuple)
print(counties_tuple)

### 3.2.6 Dictionaries
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

len(counties_dict)

print(counties_dict)
counties_dict.items()  # gets all dictionary, no indexing
counties_dict.keys()   # gets the keys only, no indexing
counties_dict.values() # gets the values only, no indexing

counties_dict.get("Denver") # method 1: get(pass key) a specific value by passing key
# method 2: get a specific value 
counties_dict['Arapahoe']
counties_dict["Arapahoe"]

##List of Dictionaries

#[{key1:value1, key2:value2}, {key1:value3, key2:value4}]

voting_data = [] # declare the empty list

# add each dictionary to the list usin append
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

len(voting_data)
voting_data.insert(2, {"county":"El Paso", "registered_voters": 4161149})

voting_data.pop(0) # remove is too complicated use pop


##### 3.2.8 Decision Statements

# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print(percentage_votes)
print("I received " + str(percentage_votes)+"% of the total votes.")

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver': #list accessed using an index
    print(counties[1])


temp = int(input("What's the temp?"))

if temp > 80:
    print ("HOT!")
else:
    print ("Cool")


#What is the score?
score = int(input("What is your test score? "))

# Determine the grade. if-else
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')


# What is the score?
score = int(input("What is your test score? "))

# Determine the grade. if-elif-else
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')


##### 3.2.9 

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

##and
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

##or
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")


##3.2.10 While loops

x = 0

while x <= 5:
    print(x)
    x = x + 1

#for lists
counties = ["Arapahoe","Denver","Jefferson"]

for county in counties:
    print(county)


numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

#range() does above
for num in range(5):
    print(num)

#get the length of the list as an integer for the range()
for i in range(len(counties)):
    print(counties)[i]


#for dict
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county]) #prints values

for county in counties_dict:
    print(counties_dict.get(county)) #prints values

for county, voters in counties_dict.items():
    print(county, voters)

##### 3.4.1

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)