import psycopg2
#conncet to db and create cursor
conn = psycopg2.connect("postgres://scrabble_db_user:2JjvW1gU3XXmBbtU3ranf8JX7WBoGfeo@dpg-cgv0079euhlk3uujt5q0-a/scrabble_db")
cur = conn.cursor()
#execute create table if it doesnt already exist
cur.execute('''
        DROP TABLE IF EXISTS ScoreHistory;
    ''')
cur.execute('''
        DROP TABLE IF EXISTS SearchHistory;
    ''')
cur.execute('''
        DROP TABLE IF EXISTS Users;
    ''')
#commit and close db connection
conn.commit()
conn.close()