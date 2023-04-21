from flask import Flask, url_for, escape, render_template, session, request
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
    return render_template('about_page.html')

@app.route('/search')
def search():
    return "Search Page"

@app.route('/search_history')
def history():
    search = []
    try:
        #open connection to db
        conn = psycopg2.connect("postgres://scrabble_db_user:2JjvW1gU3XXmBbtU3ranf8JX7WBoGfeo@dpg-cgv0079euhlk3uujt5q0-a.oregon-postgres.render.com/scrabble_db")
        cur = conn.cursor()
    
        id = 1
        cur.execute('SELECT * FROM SearchHistory WHERE userID = %s;', [id])
        search = cur.fetchall()

        conn.close()
        template = 'SearchHistory.html'
    except:
        template = 'SearchHistoryFailure.html'
    
    return render_template(template, search = search)

@app.route('/user_score', methods=["GET", "POST"])
def score():
    scores = []
    if request.method == "POST":
        try:
            #open connection to db
            conn = psycopg2.connect("postgres://scrabble_db_user:2JjvW1gU3XXmBbtU3ranf8JX7WBoGfeo@dpg-cgv0079euhlk3uujt5q0-a.oregon-postgres.render.com/scrabble_db")
            cur = conn.cursor()

            id = 1
            cur.execute('SELECT * FROM ScoreHistory WHERE userID = %s;', [id])
            scores = cur.fetchall()

        except:
            render_template('user_scores_fail.html')
        score = request.form.get('Score')
        return render_template('user_scores.html', scores=scores)
    else:
        try:
            #open connection to db
            conn = psycopg2.connect("postgres://scrabble_db_user:2JjvW1gU3XXmBbtU3ranf8JX7WBoGfeo@dpg-cgv0079euhlk3uujt5q0-a.oregon-postgres.render.com/scrabble_db")
            cur = conn.cursor()

            id = 1
            cur.execute('SELECT * FROM ScoreHistory WHERE userID = %s;', [id])
            scores = cur.fetchall()

        except:
            render_template('user_scores_fail.html')
        return render_template('user_scores.html', scores=scores)



