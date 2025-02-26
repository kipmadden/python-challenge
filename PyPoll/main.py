# import the os, csv modules
import os
import csv

# Create a file path for the election_data csv file
csvpath = os.path.join('Resources', 'election_data.csv')

# Read in the csv file
with open(csvpath, newline='') as csvfile:

    # Using the csvfile object create csvreader variable identifying the delimiter as a comma
    csvreader = csv.reader(csvfile, delimiter=',')

    # Set variable to capture two columns of data VoterID and Candidate name
    idList = []
    canList = []
    canDict = {}
    
        # Read each row of data and capture VoterID and Candidate name into a lists
    for row in csvreader:
        # Check if the line read in is the header - if it isn't add it to the idList and canList
        if row[0] != "Voter ID":
               
            idList.append(row[0])
            canList.append(row[2])

# Check if there is more than one occurence of the VoterID (this would be voter fraud) 
if len(idList) != len(set(idList)):
    print(f'Looks like there is voter fraud!')
else:
    # Determine the total votes by looking at the length of the list idList
    totalVotes = len(idList)
    # Store the unique list of candidate names by taking a set of canList list
    candidatesVoted = (list(set(canList)))
    
    winner = ''
    winvotes = 0
    
    # Store the number of votes each candidate received and the percentage of the total votes as values in a dictionary
    # with the candidate name as the key
    for cand in candidatesVoted:
        canDict[cand] = [canList.count(cand),round(canList.count(cand)/totalVotes*100,3)]
        # Check if the number of votes the current candidate has is greater than the current winvotes variable
        # If it is then replace the value of winvotes with the new higher count and set the winner variable to the
        # name of the current candidate
        if int(canList.count(cand)) > winvotes:
            winvotes = int(canList.count(cand))
            winner = cand

# create an empty list to store output f strings for results
results = []

# Append each result string to the results list
results.append(f'Election Results')
results.append(f'------------------------------')
results.append(f'Total Votes: {totalVotes:,}')
results.append(f'------------------------------')
# Iterate through the canDict dictionary and print out the results to the screen
for candidate in canDict.keys():
    results.append(f'{candidate}: {canDict[candidate][1]}% {canDict[candidate][0]:,}')
results.append(f'------------------------------')
results.append(f'Winner: {winner}')
results.append(f'------------------------------')

# Iterate through the list of strings and print each one to the terminal
for result in results:
    print(result)

# Print results to a file named pyPoll_results.csv

# Set variable for output file path
output_file = os.path.join('Resources','pyPoll_results.csv')

#  Open the output file path using a context manager
with open(output_file, "w", newline="") as datafile:
    # pass the datafile object to the writer
    writer = csv.writer(datafile)

    # Write the result as a separate line from the list results (each element is a string) 
    # so we need to use a nested list to write each string as a separate line because the
    # .writerows method takes an iterable and uses each element of that iterable for each column
    for result in results:
        writer.writerows([[result]])
        #print([[result]])