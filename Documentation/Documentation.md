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
 

<hr>

#### login() 

<hr>

#### logout() 

<hr>

#### register()
 

<hr>

#### about() 
 

<hr>

#### show_results() 


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
