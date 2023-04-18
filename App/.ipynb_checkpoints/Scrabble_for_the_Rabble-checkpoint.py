from flask import Flask
import psycopg2

app = Flask(__name__)


@app.route('/')
def login():
    return 'Login Page'

@app.route('/sign_up')
def register():
    return "Sign Up"

@app.route('/about')
def about():
    return "About Page"

@app.route('/search')
def search():
    return "Search Page"

@app.route('/search_history')
def history():
    #open connection to db
    conn = psycopg2.connect("postgres://scrabble_db_user:2JjvW1gU3XXmBbtU3ranf8JX7WBoGfeo@dpg-cgv0079euhlk3uujt5q0-a/scrabble_db")
    cur = conn.cursor()
    
    id = 1
    cur.execute('SELECT letters, word, score FROM SearchHistory WHERE userID = %s;', [id])
    search = cur.fetchall()
    
    conn.close()
    
    return render_template('SearchHistory.html')

@app.route('/user_score')
def score():
    return "Score Page"



