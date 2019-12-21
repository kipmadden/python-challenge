# import the os, csv and statistics modules
import os
import csv
from statistics import mean

# Create a file path for the budget_data csv file
csvpath = os.path.join('Resources', 'budget_data.csv')
print(csvpath)
# Read in the csv file
with open(csvpath, newline='') as csvfile:

    # Using the csvfile object create csvreader variable identifying the delimiter as a comma
    csvreader = csv.reader(csvfile, delimiter=',')

    # Set variable to capture header if there is one, and a list for month data and P&L data
    headerval = []
    months = []
    pAndL = []
    pAndLDiffList = []
    priorVal = 0
    firstVal = True
    # Read each row of data after the header
    for row in csvreader:
        # Check if the first row is a header with the label "Date" in the first position
        if row[0] == "Date":
            # Store the header in a list variable
            headerval = row
            # if not the header row then append the values to the appropriate list
        else:
            months.append(row[0])
            pAndL.append(int(row[1]))
            # Calculate the difference between the current profit and loss and the prior profit and loss
            # Don't caluclate a difference if we are on the first value
            if firstVal:
                # Set the priorVal to the current P&L value for use in calculating the P&L difference for the second P&L value in the data
                priorVal = int(row[1])
                # We've dealt with the first P&L difference value so set the firstVal state variable to False
                firstVal = False
            else:
                # Caluculate the first P&L difference
                pAndLDiff = int(row[1]) - int(priorVal)
                # Add the P&L difference to the pAndLDiffList
                pAndLDiffList.append(int(pAndLDiff))
                # Increment the priorVal to the current P&L value for use in the next iteration of the P&L difference calculation
                priorVal = int(row[1])

    
# Save the results as a list of strings so we can both print to the terminal and to a file
# without having to write out all the lines explicitly twice

# create an empty list to store output f strings for results
results = []

# Append each result string to the results list
results.append(f'Financial Analysis')
results.append(f'------------------------------')
results.append(f'Total Months: {len(months)}')
results.append(f'Total: ${(sum(pAndL)):,}')
results.append(f'Average Change: ${round(mean(pAndLDiffList),2):,}')
results.append(f'Greatest Increase in Profits: {months[(pAndLDiffList.index(max(pAndLDiffList)))+1]} ${max(pAndLDiffList):,}')
results.append(f'Greatest Decrease in Profits: {months[(pAndLDiffList.index(min(pAndLDiffList)))+1]} ${min(pAndLDiffList):,}')

# Iterate through the list of strings and print each one to the terminal
for result in results:
    print(result)

# Print results to a file named pybank_results.csv

# Set variable for output file path
output_file = os.path.join('Resources','pybank_results.csv')

#  Open the output file path using a context manager
with open(output_file, "w", newline="") as datafile:
    # pass the datafile object to the writer
    writer = csv.writer(datafile)

    # Write the result as a separate line from the list results (each element is a string) 
    # so we need to use a nested list to write each string as a separate line because the
    # .writerows method takes an iterable and uses each element of that iterable for each column
    for result in results:
        writer.writerows([[result]])
