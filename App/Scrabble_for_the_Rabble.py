from flask import Flask, url_for, escape, render_template, session
import psycopg2
import wordScript
import free_letter_wordScript

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
    try:
        #open connection to db
        conn = psycopg2.connect("postgres://scrabble_db_user:2JjvW1gU3XXmBbtU3ranf8JX7WBoGfeo@dpg-cgv0079euhlk3uujt5q0-a.oregon-postgres.render.com/scrabble_db")
        cur = conn.cursor()
    
        id = 1
        cur.execute('SELECT letters, word, score FROM SearchHistory WHERE userID = %s;', [id])
        search = cur.fetchall()

        conn.close()
    except:
        id = 1
    
    return render_template('SearchHistory.html')

@app.route('/user_score')
def score():
    return "Score Page"



