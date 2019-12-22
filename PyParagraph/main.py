# import the os, csv modules
import os
import csv
import re
import nltk

# Ask for user input to run file 1, file 2
userInput = input(f'Please enter a number to analyze (1) paragraph_1.txt (2) paragraph_2.txt :   ')

# Parse userInput and create filepath accordingly
if int(userInput) == 1:
    csvpath = os.path.join('raw_data', 'paragraph_1.txt')
elif int(userInput) == 2:
    csvpath = os.path.join('raw_data', 'paragraph_2.txt')
else:
    print(f'You entered an invalid entry so we will just pick paragraph_1.txt')  
    csvpath = os.path.join('raw_data', 'paragraph_1.txt')


directoryPath,filePath = csvpath.split('\\')
# Read in the csv file
with open(csvpath, newline='') as csvfile:

    # Using the csvfile object create csvreader variable identifying the delimiter as a comma
    csvreader = csv.reader(csvfile, delimiter=',')

    # Initialize variable to capture concatanated list of strings into one giantString
    giantString = ''
    
    # Set variable for output file path
    output_file = os.path.join('raw_data','paragraphOutput.txt')
    
    #Print the first line to the terminal
    print()
    print(f'Paragraph Analysis for the file: {filePath} in the folder: {directoryPath}')
    print('---------------------------------------------------------------------------')
    # iterate through the list 
    for row in csvreader:
        string = ' '.join(row)
        giantString = giantString + string

    # Count the number of words by splitting on spaces
    numWords = len(giantString.split()) 
    print(f'Approximate Word Count separating on spaces: {numWords}')

    # Alternate method using regex
    wordRegex = r'\w+'
    wordList = re.findall(wordRegex,giantString)
    numRegexWords = len(wordList)
    print(f'Approximate Regex "\w+" Word Count: {numRegexWords}')

    # Alternate method using regex2 expression to not count contractions as a separate word
    # For example the \w+ method will count "Can't" as two separate words because it sees the "'" as the end of
    # the words "Can" because of the "'" then it counts the "t" as a separate word
    # Using the regex expression (?<!\S[\w\'])\w+?(?=\b|n\'t) we eliminate counting contractions as two distinct words
    wordRegex2 = r'(?<!\S[\w+\'])\w+?(?=\b|n\'t)'
    wordList2 = re.findall(wordRegex2,giantString)
    numRegex2Words = len(wordList2)
    print(f'Approximate Regex2 "(?<!\S[\w\'])\w+?(?=\b|n\'t)" Word Count: {numRegex2Words}')
    

    # Count sentences by enumerating period characters
    sentenceSplit = re.split("(?<=[.!?]) +", giantString)
    numSentence = len(sentenceSplit)
    #print(f'Sentence List: {sentenceSplit}')
    print(f'Approximate Sentence Count: {numSentence}')

    # Use the nltk module to get sentences
    #nltk.download('punkt')
    nltk_tokens = nltk.sent_tokenize(giantString)
    print (f'Approximate nltk Sentence Count: {len(nltk_tokens)}')
    
    # Count the Average Letter Count by only considering characters A-Z and a-z (no letters from other languages)
    # and dividing by the Regex Word count
    letterRegex = r'[A-Za-z]'
    letterRegexList = re.findall(letterRegex,giantString)
    letterRegexCount = len(letterRegexList)
    letterCountRegexAvg = round(letterRegexCount/numRegexWords,2)
    letterCountRegex2Avg = round(letterRegexCount/numRegex2Words,2)
    print(f'Total Letter Count "[A-Za-z]: {letterRegexCount}')
    print(f'Average Letter Count using Regex : {letterCountRegexAvg}')
    print(f'Average Letter Count using Regex2 : {letterCountRegex2Avg}')

    # Calculate the average sentence length by dividing the number of Words by the number of sentences
    sentenceLength = numRegexWords / numSentence
    print(f'Average Sentence Length: {sentenceLength}')


    

