# import the os, csv modules
import os
import csv
import re

# Create a file path for the paragraph text file
csvpath = os.path.join('raw_data', 'paragraph_1.txt')

# Read in the csv file
with open(csvpath, newline='') as csvfile:

    # Using the csvfile object create csvreader variable identifying the delimiter as a comma
    csvreader = csv.reader(csvfile, delimiter=',')

    # Initialize variable to capture concatanated list of strings into one giantString
    giantString = ''
    
    # Set variable for output file path
    output_file = os.path.join('raw_data','paragraphOutput.txt')
    
    # iterate throught the list 
    for row in csvreader:
        string = ' '.join(row)
        giantString = giantString + string

    # Count the number of words by splitting on spaces
    numWords = len(giantString.split()) 
    print(f'Number of words: {numWords}')

    # Count sentences by enumerating period characters
    sentenceSplit = re.split("(?<=[.!?]) +", giantString)
    numSentence = len(sentenceSplit)
    print(f'Sentence List: {sentenceSplit}')
    print(f'Approximate Sentence Count:{numSentence}')



    # Calculate the average sentence length by dividing the number of Words by the number of sentences
    sentenceLength = numWords / numSentence
    print(f'Average Sentence Length: {sentenceLength}')
        # Check if the row read in is the header - if it isn't process the row
        # if row[0] != "Emp ID":
        #     # Assign the strings in the list to variables
        #     empId,name,dob,ssn,state = [elem for elem in row]
        #     # Split the name field into firstName and lastName 
        #     firstName,lastName = name.split(' ')
        #     # Split the dob field into year, month and day
        #     year,month,day = dob.split('-')
        #     # format the dobNew using f-string
        #     dobNew = f'{month}/{day}/{year}'
        #     # Split the SSN by the '-' into three parts
        #     ssn1,ssn2,ssn3 = ssn.split('-')
        #     # Obfuscate the first 5 digits of the SSN and only show the last 4 digits
        #     ssnNew = f'***-**-{ssn3}'
        #     # Use us_state_abbrev dict to transform the fully spelled state name into 2 letter code
        #     stateNew = us_state_abbrev[state]
        #     # Form a new list of strings and append it to the list of lists employeeList
        #     newRow = [empId,firstName,lastName,dobNew,ssnNew,stateNew]
        #     employeeList.append(newRow)
        # # Check if the firstRow variable is True - meaning we haven't written the header line
        # if firstRow:
        #     # initialize the employeeList with the newHeader list and set firstRow variable to False
        #     employeeList.append(newHeader)
        #     firstRow = False
    # Print results to a file named employee_data_new.csv
    #  Open the output file path using a context manager
    # with open(output_file, "w", newline="") as datafile:
    #     # pass the datafile object to the writer
    #     writer = csv.writer(datafile)

    #     # The .writerows method takes an iterable and uses each element of that iterable for each column
    #     # employeeList is a list of lists, therefore result is a list (iterable)
    #     for result in employeeList:
    #         writer.writerows([result])


# Iterate through the list of strings and print each one to the terminal
#for result in employeeList:
#    print(result)


