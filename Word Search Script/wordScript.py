#Python script that takes input of letters and produces a list of all possible scrabble words

def characterCount(word):
    #declare empty dictionary
    charDict = {}
    #iterate through letter in word 
    for letter in word:
        #increase the count of letter by 1, if letter not present set to 0 and increase by 1
        charDict[letter] = charDict.get(letter, 0) + 1
    return charDict


if __name__ == "__main__":
#available letter list 
    letterList = ['A', 'B', 'E', 'E', 'I', 'N', 'Q', 'W', 'O', 'T']
#wordList to have dictionary read into
    wordList = []
#open scrabble dictionary and read each word into list
    with open('testDictionary.txt') as file:
        for line in file:
            wordList.append(line.rstrip())
    #iterate through list one word at a time
    for word in wordList:
        #set flag to 1
        flag = 1
        #call characterCount which returns a dictionary with a key of letter and a vallue of the number of times letter in word
        #ex word = hello charCount = {'h':'1', 'e':1, 'l':'2', 'o':1}
        charCount = characterCount(word)
        #key = letter
        for key in charCount:
            #if key/letter not in Scrabble letter list
            if key not in letterList:
                #set flag to 0
                flag = 0
            else:
                #if the count of letters in the word is greater than the count of letters in the Scrabble letter list
                if charCount[key] > letterList.count(key):
                    #set flag to 0
                    flag = 0
        #if flag was not set to 0 then letter list can form that word
        if flag == 1:
            print(word)
    
    
    
    
    

