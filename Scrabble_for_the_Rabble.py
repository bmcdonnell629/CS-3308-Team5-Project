from flask import Flask, url_for, escape, render_template, session, request
import psycopg2
import wordScript
import free_letter_wordScript
import scoreInsert

app = Flask(__name__)


@app.route('/')
def login():
    return render_template('Login_Page.html')

@app.route('/sign_up', methods=["GET", "POST"])
def register():
    msg = ''
    if request.method == 'POST' and 'Username' in request.form and 'Password' in request.form and 'Name' in request.form:
        Username = request.form['Username']
        Password = request.form['Password']
        Name = request.form['Name']
        
        conn = psycopg2.connect("postgres://scrabble_db_user:2JjvW1gU3XXmBbtU3ranf8JX7WBoGfeo@dpg-cgv0079euhlk3uujt5q0-a.oregon-postgres.render.com/scrabble_db")
        cur = conn.cursor()
        
        cur.execute('SELECT* FROM form WHERE Username = %s', (Username,))
        account = cur.fetchone()
        conn.close()
        if account:
            msg = 'Account already exists'
        elif not re.match(r'[A-Za-z0-9]+', Username):
            msg = 'Username must contain only either characters and/or numbers'
        elif not Username or not Password or not Name:
            msg = 'Please fill out the form'
        else:
            conn = psycopg2.connect("postgres://scrabble_db_user:2JjvW1gU3XXmBbtU3ranf8JX7WBoGfeo@dpg-cgv0079euhlk3uujt5q0-a.oregon-postgres.render.com/scrabble_db")
            cur = conn.cursor()
            cur.execute('INSERT INTO Users (UserID, Username, Password, Name) VALUES (Null, % s, % s, % s)', (Username, Password, Name,))
            msg = 'You have successfully registered'
            conn.close()
    return render_template('Register_User.html', msg=msg)

@app.route('/about')
def about():
    return render_template('about_page.html')

@app.route('/search')
def search():
    return render_template('search_page.html')

@app.route('/search_results/<search_word>/<allow_anagrams>/<min_letters>/<max_letters>/<starts_with>/<ends_with>/<contains>/<fixed_letters>')
def search_results(search_word=None, allow_anagrams=True, min_letters=2, max_letters=15, starts_with=None, ends_with=None, contains=None, fixed_letters=None):
    return render_template('search_results.html', search_word=search_word, allow_anagrams=allow_anagrams, min_letters=min_letters, max_letters=max_letters, starts_with=starts_with, ends_with=ends_with, contains=contains, fixed_letters=fixed_letters)

@app.route('/search_history')
def history():
    search = []
    try:
        #open connection to db
        conn = psycopg2.connect("postgres://scrabble_db_user:2JjvW1gU3XXmBbtU3ranf8JX7WBoGfeo@dpg-cgv0079euhlk3uujt5q0-a.oregon-postgres.render.com/scrabble_db")
        cur = conn.cursor()
    
        id = 1
        cur.execute('SELECT * FROM SearchHistory WHERE userID = %s ORDER BY searchNum ASC;', [id])
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
        score = request.form.get('Score')
        print(score)
        try:
            id = 1
            
            scoreInsert.insert(int(score), id)
            
            conn = psycopg2.connect("postgres://scrabble_db_user:2JjvW1gU3XXmBbtU3ranf8JX7WBoGfeo@dpg-cgv0079euhlk3uujt5q0-a.oregon-postgres.render.com/scrabble_db")
            cur = conn.cursor()
            cur.execute('SELECT * FROM ScoreHistory WHERE userID = %s ORDER BY scoreNum ASC;', [id])
            scores = cur.fetchall()
            conn.close()
        except:
            render_template('user_scores_fail.html')
        return render_template('user_scores.html', scores=scores)
    else:
        try:
            #open connection to db
            conn = psycopg2.connect("postgres://scrabble_db_user:2JjvW1gU3XXmBbtU3ranf8JX7WBoGfeo@dpg-cgv0079euhlk3uujt5q0-a.oregon-postgres.render.com/scrabble_db")
            cur = conn.cursor()

            id = 1
            cur.execute('SELECT * FROM ScoreHistory WHERE userID = %s ORDER BY scoreNum ASC;', [id])
            scores = cur.fetchall()
            conn.close()

        except:
            render_template('user_scores_fail.html')
        return render_template('user_scores.html', scores=scores)



