
'''
Modified from free_letter_wordScript.py (original author: Brendan McDonnell, modified by: Nathaniel Mutkus)
'''

def characterCount(word):
    '''
    takes input of word and returns a dictionary with keys of letters and integer value of count of that letter within word
    '''
    #declare empty dictionary
    charDict = {}
    #iterate through letter in word 
    for letter in word:
        #increase the count of letter by 1, if letter not present set to 0 and increase by 1
        charDict[letter] = charDict.get(letter, 0) + 1
    return charDict

def search_word_scores(search_word_letters, result_word):
    letter_scores = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1,
                     "F": 4, "G": 2, "H": 4, "I": 1, "J": 8,
                     "K": 5, "L": 1, "M": 3, "N": 1, "O": 1,
                     "P": 3, "Q":10, "R": 1, "S": 1, "T": 1,
                     "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4,
                     "Z":10, "?": 0}
    
    word_score = 0
    search_dict = search_word_letters
    
    for letter in result_word:
        if letter not in search_dict:
            if search_dict["?"] > 0:
                search_dict["?"] = search_dict["?"] - 1
        elif search_dict[letter] > 0:
            word_score = word_score + letter_scores[letter]
            search_dict[letter] = search_dict[letter] - 1
        elif search_dict["?"] > 0:
            search_dict["?"] = search_dict["?"] - 1
        else:
            print("Letter count is incorrect")
    
    return word_score


def find_anagrams(user_input):
    '''
    main function for script
    takes one argument: user_input, a string of letters and '?'.
    returns anagrams and sub-anagrams from user_input and free tiles and values of scrabble scores
    '''
    #empty letter list 
    letterList = []
    blankTiles = 0

    #add letters from input to list of letters
    for character in user_input:
        if character == "?":
            blankTiles = blankTiles + 1
        else:
            letterList.append(character)
        
    #wordList to have dictionary read into
    wordList = []
    #scrabble result dictionary with word as key and scabble score as value ex. {'are': '3'...}
    scrabbleList = {}
    #open scrabble dictionary and read each word into list
    with open('finalWordList.txt') as file:
        for line in file:
            wordList.append(line.rstrip())
    #iterate through list one word at a time
    for word in wordList:
        #set flag to 1
        flag = 1
        #set # of free letters = blank tiles
        freeLetters = blankTiles
        #call characterCount which returns a dictionary with a key of letter and a value of the number of times letter in word
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
            score = search_word_scores(characterCount(user_input), word)
            #store {word : score} as key value pair in dictionary ex. {'hello' : 8, etc} 
            scrabbleList[word] = score
    #sort list by score descending order
    sortedList = sorted(scrabbleList.items(), key=lambda x:x[1], reverse=True)
    
    return sortedList