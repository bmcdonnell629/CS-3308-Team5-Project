# Scrabble for the Rabble :  Documentation  
<hr>

### Introduction 

<hr>
    
### About

Basic website application using the flask framework to search scrabble words form letter inputs and track user scores.

### Basic Set Up

Access web app via https://scrabble-for-the-rabble.onrender.com/  
Updates to app need to be pushed to Github repository for auto updates  

#### Directory Folder Layout
App - Contains base python app  
Databases - Contains python files for creation and deletion of database tables  
Documentation - Contains project documentation      
flask env - contains virtual environment for running flask    
HTML - Contains html templates  
images - Contains any linked images  
static - contains any static files used for webpage construction    
Milestone 4 Web Testing - Contains proposal write up for web page ideas  
Milestone 5 SQL design - Contains proposal for database structure and set up  
Render - Contains pictures of render settings for linking github and sql dtabase connection urls  
static - Contains css, javascript, images  
templates - contains html templates for web page rendering    
User Stories - Contains ratings of user stories for some tasks of app development   

<hr>

### Functions/Web Pages 

<hr>

### Scrabble for the Rabble Functions

<hr>

#### search() 
 Search/home page displaying a search bar and advanced filters that can be applied to the 
 search results.
 Returns the search page template.

<hr>

#### login() 
Login page with the fields of username and password where a registered user can type in the correct username/password and then is starts a login session to be used throughout the application. It runs a query against the database to make sure that the username and password is correct. 
Returns "Logged in Succesful" if username and password are correct. Returns "USERNAME/PASSWORD IS INCORRECT" if some information is incorrect. 

<hr>

#### logout() 
Logout page that runs a pop in the session id and the session name for the user to end the user's current session and log the user out of the application. 
Returns the login template so another user can log in. 

<hr>

#### register()
Register user page with fields of Name, Username, and Password. Where a user can input these fields and create a user record in the user table using a dbinsert function, it fills in the fields of Name, Username, Password, and UserID. The userid is automatically calculated as the next number based on the highest userid that currently exists. Once the user record is added the user can then login. 
Returns "User Added Successfully" if user record is created. Returns "USERNAME ALREADY EXISTS, PLEASE USE A DIFFERENT USERNAME" if username already exists. 

<hr>

#### about() 
About page communicating the purpose of the site, including a link for the user to try out the search function. 

<hr>

#### show_results() 
Search results page showing the input from the user, search filters applied by the user, 
the legal Scrabble Words matching the search input, and the scores for those words.
Parameters are provided in the URL.
Returns the search results template, as well as a list of word/score tuples, sorted 
primarily by Scrabble score in descending order, then alphabetically.

<hr>

#### history()
Search history page listing user's last 5 searches and top 5 scoring words from searches      
history function takes no funciton inputs / calls searchInsert function from dbInsert        
Returns search history template with list of top 5 searches  and top 5 words placed on page   

<hr>

#### score() 
Score page listing users top 10 submitted scores      
score function takes no funciton inputs / calls scoreInsert function from dbInsert   
Returns a user score template with list of top 10 scores and dates score was achieved on  

<hr>

### dbInsert Functions

<hr>

#### searchInsert(id, words, letters)
searchInsert function takes 3 inputs id:integer, words:list of tuples of words and matching scores, letters:string of charaters used for search  
Updates searchHistory database table and tracks last 5 searches  

<hr>

#### scoreInsert(id, score)
scorehInsert function takes 2 inputs id:integer, score:int
Updates scorehHistory database table and tracks top 10 user scores submitted
