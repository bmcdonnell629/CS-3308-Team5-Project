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

* UserID searchNum wordNum must be unique 

* searchNum and wordNum must be integers between 1 and 5

* UserID must exist in Users table

Data Access Tests

Name: Scrabble Word Search History Request

Description:  
    Test the Search Results History Page provides correct results  
  
Pre-conditions:  
    User has valid user name and password  
    User logged into user name  
    
Test steps:    
    1. Navigate to login page  
    2. Provide valid user name  
    3. Provide valid password  
    4. Click login button  
    5. Navigate to Results History page  

Expected result:  
    User should see top 5 words from their past 5 searches. If less than 5 words in search or less than 5 searches in history display none.  
            
Actual result:  
    User sees top 5 words from past 5 searches  
            
Status (Pass/Fail):  
    Pass  
           
Notes:  
    N/A  
            
Post-conditions:  
    


<div align="center">Table 3</div>

Table Name: 
Table Description
For each field of the table, provide name and short description.
List of tests for verifying each table