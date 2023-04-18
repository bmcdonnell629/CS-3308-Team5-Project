<img src="milestone5_table.PNG">

<div align="center">Table 1 : User Info</div>

Table Name: Users, User Info

Table Description:

* Table contains username and password info that is required for login. When a user signs up, then they will be added to this table. 

Table Fields: 

* UserID: Primary key that is used to identify a unique user. 

* Username: Unique varchar that the user will use to login.

* Name: This is a varchar that is the name of the user. 

* Password: This is a varchar that will be used to identify it is the user at login. 

List of tests for verifying each table

* UserID will be unique to each user. 

* Username must be unique to each user. 

* Password must be related to a specifc username for login. 

* Name must be related to a specific username. 

Data Access Tests for Table 1  

<div>Test 1 for Table 1</div>

Name: Verify Login with Username and Password

Description:  
    Test the Login Page for Scrabble for the Rabble 
  
Pre-conditions:  
    Username and Password is Valid
    
Test steps:    
    1. Navigate to login page  
    2. Provide valid user name  
    3. Provide valid password  
    4. Click login button  

Expected result:  
    User login should be successful. Login will be successful on the user side if they are taken to the home/search page. If the login is succesful, it query the database and find the username and password linked together under a UserID. This will then trigger the login to be successful and the user will be taken to the home/seach page. 
            
Actual result:  
    User is taken to the home/search page. 
            
Status (Pass/Fail):  
    Pass  
           
Notes:  
    N/A  
            
Post-conditions:
    User is found in the database and signs into their account successfully. 
    
<div>Test 2 for Table 1</div>

Name: User signs up with username, name, and password

Description:  
    Tests the sign up page for Scrabble for the Rabble
  
Pre-conditions:  
    User does not exist in the table
    Username does not exist in the table
    
Test steps:    
    1. Navigate to sign up page  
    2. Provide a new unique user name  
    3. Enter name
    4. Provide valid password  
    5. Click Sign Up button  

Expected result:  
    User sign up is successful and new record is created in table. Once the sign up is complete, the user will be taken to the login page where they can then use their new creditials to login. When the user successfully signs up, it will then create a new record in the table, it will make sure that the username does not exist already and it will create a new unique UserID. If the username already exists, then it will return an error stating "username exists please choose another username". 
            
Actual result:  
    User is taken to the login page to login with newly created credentials.  
            
Status (Pass/Fail):  
    Pass  
           
Notes:  
    N/A  
            
Post-conditions: New user record is created in the table with a new unique primary key of UserID and the user is now able to login through the login page with correct credentials. 

<div align="center">Table 2</div>

Table Name: searchHistory, User Search History  

Table Description:  

* Table contains users last five scrabble word searches, the letters input for the search, and the top five scoring words from the search 
* Links to user table with UserID Foreign Key that is UserID Primary key in Users table
  
For each field of the table, provide name and short description.

* UserID: Integer Foreign Key referencing Users table primary id key

* searchNum: Integer from 1 to 5, refers to last 5 searches. 1 is the most recent search 5 being the least recent stored

* wordNum: Integer from 1 to 5, refers to top 5 words one of 5 most recent searches. 1 is the highest scoring word of that search 5 is the 5th highest scoring word of search. ex searchNum 2  wordNum 3 refers to the 2nd most recent search 3rd highest scoring word

* letters: varchar, refers to the the letters input by the user for that word search

* word: varchar that contains single word from search

* score: integer that contains scrabble score for the word in row

List of tests for verifying each table 

* (UserID searchNum wordNum) combined must be unique 

* searchNum and wordNum must be integers between 1 and 5

* UserID must exist in Users table

Data Access Tests  

<div align="center">Test 1 for Table 2</div>

Name: Word Search History Request  
searchHistoryRequest(userID)  

Description:  
    Test the Search Results History Page provides correct results    
    Requires parameter of userID or sessionID of user to search table for correct results
  
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
    * When user navigates to the Results History Page user should see top 5 words from their past 5 searches. If less than 5 words in search or less than 5 searches in history display none in place of missing results or words.   
    * The function will select search history for user:   
        SELECT * FROM  User Search History WHERE userID = ?, (userID)   

Actual result:  
    User sees top 5 words from past 5 searches    
            
Status (Pass/Fail):    
    Pass: The function returns the last 5 searches with the top 5 words of those searches   
          If less than 5 searches the function returns the total number of searches completed so far   
    Fail: The function fails to return the past 5 searches   
          The function fails to return the top 5 words from searches  
          
           
Notes:   
            
Post-conditions: The search history page will be populated with the return values of this function.   
The search history table will not be altered when this function is used. Only select statements utilized.   
  
    
<div align="center">Test 2 for Table2</div>

Name: Word Seach History Insert  
searchHistoryInsert(userID, letters, wordList)   

Description:  
Test the Search Page inserts correct results   
Function takes parameters of a userID, string of user input letters, and a word list of tuples with word and score ex wordlist = [('are', 3), ....]  
  
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
    6. Enter valid letter input and select search button  

Expected result:  
    * When User submits a letter search then the insert function should be called to insert top 5 scoring words into Search History Table from search  
    * Function will take parameter inputs of user id, string of letters, and a list of the top 5 words and scores from current search  
    * The Function will delete 5th oldest search if there are 5, update remaining 4 searches, and insert latest search into table:  
        if there are 5 searches in the search history table:  
            DELETE FROM searchHistory WHERE userID = ? AND searchNum = 5, (userID)  
            Iterate from 4 to 1 updating previous seaches increasing searchNum by 1  
            UPDATE table_name SET searchNum = 5 WHERE searchNum = 4;   
            ...  
            INSERT INTO searchHistory VALUES word='', score=# ,...., letters ='', searchNum = 1, userID = ? (userID)  
        if less than 5 searches:  
            UPDATE table_name SET searchNum = #+1 WHERE searchNum = #;   
            ...   
            INSERT INTO searchHistory VALUES word='', score=# ...., letters ='' searchNum = 1, userID = ? (userID)  
            
Actual result:  
    User sees top 5 words from past 5 searches  
            
Status (Pass/Fail):  
    Pass: Table succesfully removes 5th oldest search and updates remaining 4 searches before inserting the newest search  
          When navigating to search history page user will see updated history page populated  
    Fail: Function fails to remove oldest search  
          Function fails to update previous searches  
          Function fails to insert most recent search  
           
Notes:  
            
Post-conditions: Table is changed via a delete statememt, update statement, and insert statement  
5th oldest search is removed from database. Remaing 4 searches are increased in age by 1. New search inserted inthe 1 position  
Insert only seen if user navigates to search history page following search  
    
    
<div align="center">Table 3</div>

Table Name: scoreHistory, User Score History  

Table Description:  

* Table contains users top 10 scrabble game scores  
* Table linked to User table via userID foreign key which is primary key of Users table
  
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

<div align="center">Test 1 for Table 3</div>

Name: Scrabble User Score History Request
scoreRequest(userID)

Description:  
    Test the user score history page renders correct results 
    Function has parameter of userID, returns the top 10 user scores for that userID
  
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
    Function returns top 10 scores from table when page is visited or refreshed:
    Select * FROM User Score History WHERE userID = ?, (userID)
    User should see top 10 scrabble game scores previously entered. If less than 10 scores in score history then display available scores and display none for remaining missing scores.  
            
Actual result:  
    User sees top 10 scrabble game scores  
            
Status (Pass/Fail):  
    Pass: Function returns a list of the top 10 user scores
    Fail: Function fails to return top 10 user scores
          Function returns wrong user scores
           
Notes:   
            
Post-conditions: User score table is not updates as a result of this function, only select statements used  
User Score History web page is populated with the results of the function  

<div align="center">Test 2 for Table 3</div>

Name: Scrabble User Score Insert  
userScoreInsert(userID, userScore)  

Description:  
    Test the user score history page inserts correct results 
    Function has parameters of userID and userScore both integers, inserts score into user history if score is one of the top 10
  
Pre-conditions:  
    User has valid user name and password  
    User logged into user name
    User has entered at least one scrabble game score
    
Test steps:    
    1. Navigate to login page  
    2. Provide valid user name  
    3. Provide valid password  
    4. Click login button  
    5. Navigate to Score History Page
    6. Input valid game score  
    

Expected result:  
    Function starts with submission of user score on user score history webpage
    Function selects all user scores that are less than entered score: Select * FROM userScores WHERE userID = ? AND score < ?; (userID, userScore)
    If there are scores less than user input:
        Delete 10th highest score: DELETE FROM userScore WHERE userID = ? AND scoreNum = 10; (userID) 
        Update scoreNum of scores less than user input by 1  
        Insert newest score into table
    If score is less than previous 10 do not update table  
    User should see top 10 scrabble game scores previously entered. If less than 10 scores in score history then display available scores and display none for remaining missing scores.  
            
Actual result:  
    User sees top 10 scrabble game scores  
            
Status (Pass/Fail):  
    Pass: User sees 10 highest entered scrabble scores  
    Fail: Table does not update with new top 10 score input   
    Fail: Table does update when score is not a top 10 score  
    Fail: Function does not return top 10 user scores  
           
Notes:  
            
Post-conditions:  If user entered score greater than 10th highest user score User Score History is updated with new score value and 10th highest value is removed  

If user score is lower than 10th highest score value then no update to table occurs  
