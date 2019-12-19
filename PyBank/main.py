# import the os, csv and statistics modules
import os
import csv
from statistics import mean as avg

# Create a file path for the budget_data csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Read in the csv file

with open(csvpath, newline='') as csvfile:

    # Using the csvfile object create csvreader variable identifying the delimiter
    csvreader = csv.reader(csvfile, delimiter=',')

    #Set variable to capture header if there is one, and a list for month data and P&L data
    headerval = []
    months = []
    pAndL = []

    # Read each row of data after the header
    for row in csvreader:
        # Check if the first row is a header with the label "Date" in the first position
        if row[0] == "Date":
            #Store the header in a list variable
            headerval = row
            #print(f'headerval found: {headerval}')
        else:
            months.append(row[0])
            pAndL.append(int(row[1]))

#Print results to the terminal
results = []

results.append(f'Financial Analysis')
results.append(f'------------------------------')
results.append(f'Total Months: {len(months)}')
results.append(f'Total: ${(sum(pAndL)):,}')
results.append(f'Average Change: ${round(avg(pAndL),2):,}')
results.append(f'Greatest Increase in Profits: {months[(pAndL.index(max(pAndL)))]} ${max(pAndL):,}')
results.append(f'Greatest Decrease in Profits: {months[(pAndL.index(min(pAndL)))]} ${min(pAndL):,}')

for result in results:
    print(result)

#Print results to a file named pybank_results
# Set variable for output file
output_file = os.path.join('Resources','pybank_results.csv')

#print(f'headerval: {headerval}')
#for k in headerval:
#    print(k)
#print(f'results: {results}')

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the result as a separate line from the list results (each element is a string) 
    # so we need to use a nested list to write each string as a separate line
    for result in results:
        writer.writerows([[result]])
