# import the os, csv modules
import os
import csv

# Create a file path for the election_data csv file
csvpath = os.path.join('Resources', 'employee_data.csv')

# Read in the csv file
with open(csvpath, newline='') as csvfile:

    # Using the csvfile object create csvreader variable identifying the delimiter as a comma
    csvreader = csv.reader(csvfile, delimiter=',')

    # Set variable to capture two columns of data EmpID and Candidate name
    employeeList = []
    us_state_abbrev = {
        'Alabama': 'AL','Alaska': 'AK','Arizona': 'AZ','Arkansas': 'AR','California': 'CA','Colorado': 'CO',
        'Connecticut': 'CT','Delaware': 'DE','Florida': 'FL','Georgia': 'GA','Hawaii': 'HI','Idaho': 'ID',
        'Illinois': 'IL','Indiana': 'IN','Iowa': 'IA','Kansas': 'KS','Kentucky': 'KY','Louisiana': 'LA',
        'Maine': 'ME','Maryland': 'MD','Massachusetts': 'MA','Michigan': 'MI','Minnesota': 'MN','Mississippi': 'MS',
        'Missouri': 'MO','Montana': 'MT','Nebraska': 'NE','Nevada': 'NV','New Hampshire': 'NH','New Jersey': 'NJ',
        'New Mexico': 'NM','New York': 'NY','North Carolina': 'NC','North Dakota': 'ND','Ohio': 'OH',
        'Oklahoma': 'OK','Oregon': 'OR','Pennsylvania': 'PA','Rhode Island': 'RI','South Carolina': 'SC',
        'South Dakota': 'SD','Tennessee': 'TN','Texas': 'TX','Utah': 'UT','Vermont': 'VT','Virginia': 'VA',
        'Washington': 'WA','West Virginia': 'WV','Wisconsin': 'WI','Wyoming': 'WY',
    }
    # Set variable for output file path
    output_file = os.path.join('Resources','employee_data_new.csv')
    
    # Make a list of dictionaries 
    for row in csvreader:

        # Check if the line read in is the header - if it is don't add it to the idDict
        if row[0] != "Emp ID":
            empId,name,dob,ssn,state = row.strip().split(',')
            firstName,lastName = name.split(' ')
            year,month,day = dob.split('-')
            dobNew = f('{month}/{day}/{year}')
            ssn1,ssn2,ssn3 = ssn.split('-')
            ssnNew = f('***-**-{ssn3}')

            data = values.split(',')
            # Print results to a file named pyPoll_results.csv



            #  Open the output file path using a context manager
            with open(output_file, "w", newline="") as datafile:
                # pass the datafile object to the writer
                writer = csv.writer(datafile)

                # Write the result as a separate line from the list results (each element is a string) 
                # so we need to use a nested list to write each string as a separate line because the
                # .writerows method takes an iterable and uses each element of that iterable for each column
                for result in results:
                    writer.writerows([[result]])

# Check if there is more than one occurance of the EmpID (this would be voter fraud) 
if len(employeeList) != len(set(employeeList)):
    print(f'Looks like there is voter fraud!')
else:
    # Determine the total votes by looking at the length of the list employeeList
    totalVotes = len(employeeList)
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


# Iterate through the list of strings and print each one to the terminal
for result in results:
    print(result)

