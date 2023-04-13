#!/usr/bin/env python
#Python script that takes command line input input of letters and number of free letters and produces a list of all possible scrabble words with scores
#usage ./wordScript.py <letters> <# of free letters>

import sys

def characterCount(word):
    #declare empty dictionary
    charDict = {}
    #iterate through letter in word 
    for letter in word:
        #increase the count of letter by 1, if letter not present set to 0 and increase by 1
        charDict[letter] = charDict.get(letter, 0) + 1
    return charDict

def scrabbleScore(word):
    #initialze score to 0
    score = 0
    #dict of scrabble scores per letter
    scores = {"A": 1, "C": 3, "B": 3, "E": 1, "D": 2, "G": 2, 
          "F": 4, "I": 1, "H": 4, "K": 5, "J": 8, "M": 3, 
          "L": 1, "O": 1, "N": 1, "Q": 10, "P": 3, "S": 1, 
          "R": 1, "U": 1, "T": 1, "W": 4, "V": 4, "Y": 4, 
          "X": 8, "Z": 10}
    #iterate by letter through word
    for letter in word:
        #add score of current letter to total score
        score = score + scores[letter]
    return score


if __name__ == "__main__":
    #empty letter list 
    letterList = []
    #check length of command line arg
    if len(sys.argv) != 3:
        print("Incorrect Usage: ", sys.argv[0], " <letter input> <# of free letters>")
        sys.exit()
    #Error for incorrect usage of script
    try:
        #cmd line input of available letters
        letterInput = sys.argv[1].upper()
        #add letters from input to list of letters
        for letter in letterInput:
            letterList.append(letter)
        #set number of blank tiles equal to input
        blankTiles = int(sys.argv[2])
    except:
        print("Incorrect Usage: ", sys.argv[0], " <letter input> <# of blank tiles>")
        sys.exit()
        
#wordList to have dictionary read into
    wordList = []
#scrabble result dictionary with word as key and scabble score as value ex. {'are': '3'...}
    scrabbleList = {}
#open scrabble dictionary and read each word into list
    with open('testDictionary.txt') as file:
        for line in file:
            wordList.append(line.rstrip())
    #iterate through list one word at a time
    for word in wordList:
        #set flag to 1
        flag = 1
        #set # of free letters = blank tiles
        freeLetters = blankTiles
        #call characterCount which returns a dictionary with a key of letter and a vallue of the number of times letter in word
        #ex word = hello charCount = {'h':'1', 'e':1, 'l':'2', 'o':1}
        charCount = characterCount(word)
        #key = letter
        for key in charCount:
            #if key/letter not in Scrabble letter list
            if key not in letterList:
                #if free letters remaining 
                if freeLetters > 0:
                    #subtract the number letters in word not present in input from free letters
                    freeLetters = freeLetters - charCount[key]
                    #if free letters is not less than 0 set flag to 0
                    if freeLetters < 0:
                        #set flag to 0
                        flag = 0
                else:
                    flag = 0
            else:
                #if the count of letters in the word is greater than the count of letters in the Scrabble letter list
                if charCount[key] > letterList.count(key):
                    #if no free letters remaining set flag to 0
                    if freeLetters <= 0:
                        flag = 0
                    else:
                        #subtract the difference in letters from the word
                        diff = charCount[key] - letterList.count(key)
                        freeLetters = freeLetters - diff
                        #if free letters not remaining set flag to 0
                        if freeLetters < 0:
                            #set flag to 0
                            flag = 0
        #if flag was not set to 0 then letter list can form that word
        if flag == 1:
            #call funciton to tally word score 
            score = scrabbleScore(word)
            #store {word : score} as key value pair in dictionary ex. {'hello' : 8, etc} 
            scrabbleList[word] = score
    #sort list by score descending order
    sortedList = sorted(scrabbleList.items(), key=lambda x:x[1], reverse=True)
    #convert back to dictionary //may change
    sortedScrabbleList = dict(sortedList)
    print(sortedScrabbleList)
    
    
    
    
    

