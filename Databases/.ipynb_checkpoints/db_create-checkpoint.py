import psycopg2
#conncet to db and create cursor
try:
    conn = psycopg2.connect("postgres://scrabble_db_user:2JjvW1gU3XXmBbtU3ranf8JX7WBoGfeo@dpg-cgv0079euhlk3uujt5q0-a.oregon-postgres.render.com/scrabble_db")
    cur = conn.cursor()
except: 
    print("Failure to connect")
#execute create table if it doesnt already exist
cur.execute('''
    CREATE TABLE IF NOT EXISTS Users(
        userID int,
        Username varchar(255) NOT NULL,
        password varchar(255) NOT NULL,
        PRIMARY KEY(userID)
        );
    ''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS SearchHistory(
        userID int,
        searchNum int CHECK (searchNum > 0 AND searchNum <= 5),
        wordNum int CHECK (wordNum > 0 AND wordNum <= 5),
        word varchar(30),
        score int,
        UNIQUE (userID, searchNum, wordNum),
        FOREIGN KEY (userID) REFERENCES Users(userID)
        );
    ''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS ScoreHistory(
        userID int,
        date Date,
        scoreNum int CHECK (scoreNum > 0 AND scoreNum <= 10),
        score int,
        UNIQUE (userID, scoreNum),
        FOREIGN KEY (userID) REFERENCES Users(userID)
        );
    ''')
#commit and close db connection
conn.commit()
conn.close()

