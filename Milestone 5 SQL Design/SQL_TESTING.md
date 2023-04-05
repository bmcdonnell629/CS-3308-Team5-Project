<div align="center">Table 1</div>

Table Name: 
Table Description
For each field of the table, provide name and short description.
List of tests for verifying each table

<div align="center">Table 2</div>

Table Name: User Search History  

Table Description:  

* Table contains users last five scrabble word searches, the letters input for the search, and the top five scoring words frmo the search  
  
For each field of the table, provide name and short description.

* UserID: Integer Foreign Key referencing Users table primary id key

* searchNum: Integer from 1 to 5, refers to last 5 searches. 1 is the most recent search 5 being the least recent stored

* wordNum: Integer from 1 to 5, refers to top 5 words one of 5 most recent searches. 1 is the highest scoring word of that search 5 is the 5th highest scoring word of search. ex searchNum 2  wordNum 3 refers to the 2nd most recent search 3rd highest scoring word

* word: varchar that contains single word from search

* score: integer that contains scrabble score for the word in row

List of tests for verifying each table 

* (UserID searchNum wordNum) combined must be unique 

* searchNum and wordNum must be integers between 1 and 5

* UserID must exist in Users table

Data Access Tests  

<div align="center">Test 1</div>

Name: Scrabble Word Search History Request  

Description:  
    Test the Search Results History Page provides correct results  
  
Pre-conditions:  
    User has valid user name and password  
    User logged into user name  
    User has conducted at least one word search
    
Test steps:    
    1. Navigate to login page  
    2. Provide valid user name  
    3. Provide valid password  
    4. Click login button  
    5. Navigate to Results History page  

Expected result:  
    User should see top 5 words from their past 5 searches. If less than 5 words in search or less than 5 searches in history display none in place of missing results or words.  
            
Actual result:  
    User sees top 5 words from past 5 searches  
            
Status (Pass/Fail):  
    Pass  
           
Notes:  
    N/A  
            
Post-conditions:
  
    
<div align="center">Test 2</div>

Name: Scrabble Word Search History Insert

Description:  
    Test the Search Page inserts correct results  
  
Pre-conditions:  
    User has valid user name and password  
    User logged into user name  
    User conducts a valid scrabble word search
    
Test steps:    
    1. Navigate to login page  
    2. Provide valid user name  
    3. Provide valid password  
    4. Click login button  
    5. Navigate to Search Page
    6. Enter letter input and select search button
    7. Navigate to Results History Page

Expected result:  
    User should see top 5 words from their past 5 searches. If less than 5 words in search or less than 5 searches in history display none in place of missing results or words.  
            
Actual result:  
    User sees top 5 words from past 5 searches  
            
Status (Pass/Fail):  
    Pass  
           
Notes:  
    N/A  
            
Post-conditions: Top 5 words from search result are stored in the User Search History table within database replacing 5th oldest search results
    
    


<div align="center">Table 3</div>

Table Name: User Score History  

Table Description:  

* Table contains users top 10 scrabble game scores  
  
For each field of the table, provide name and short description.

* UserID: Integer Foreign Key referencing Users table primary id key

* date: Date game score was entered dd-mm-yyyy

* scoreNum: Integer from 1 to 10, refers to top 10 game scores. 1 is the highest score 10 is the 10th highest score

* score: integer that contains scrabble game score

List of tests for verifying each table 

* (UserID scoreNum) combined must be unique 

* scoreNum must be integers between 1 and 10

* UserID must exist in Users table

Data Access Tests

<div align="center">Test 1</div>

Name: Scrabble User Score History Request

Description:  
    Test the user score history page renders correct results 
  
Pre-conditions:  
    User has valid user name and password  
    User logged into user name
    User has entered at least one scrabble game score
    
Test steps:    
    1. Navigate to login page  
    2. Provide valid user name  
    3. Provide valid password  
    4. Click login button  
    5. Navigate to Score History page  

Expected result:  
    User should see top 10 scrabble game scores previously entered. If less than 10 scores in score history then display available scores and display none for remaining missing scores.  
            
Actual result:  
    User sees top 10 scrabble game scores  
            
Status (Pass/Fail):  
    Pass  
           
Notes:  
    N/A  
            
Post-conditions:  

<div align="center">Test 2</div>

Name: Scrabble User Score Insert

Description:  
    Test the user score history page inserts correct results 
  
Pre-conditions:  
    User has valid user name and password  
    User logged into user name
    User has entered at least one scrabble game score
    
Test steps:    
    1. Navigate to login page  
    2. Provide valid user name  
    3. Provide valid password  
    4. Click login button  
    5. Navigate to Search Page
    6. Input valid game score
    5. Navigate to Score History page  

Expected result:  
    User should see top 10 scrabble game scores previously entered. If less than 10 scores in score history then display available scores and display none for remaining missing scores.  
            
Actual result:  
    User sees top 10 scrabble game scores  
            
Status (Pass/Fail):  
    Pass  
           
Notes:  
    N/A  
            
Post-conditions:  If user entered score greater than 10th highest user score User Score History is updated with new score value and 10th highest value is removed

If user score is lower than 10th highest score value then no update to table occurs