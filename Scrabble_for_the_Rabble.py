from flask import Flask, url_for, escape, render_template, session, request
import psycopg2
import wordScript
import free_letter_wordScript
import scoreInsert

app = Flask(__name__)


@app.route('/')
def search():
    return render_template('search_page.html')

@app.route('/login')
def login():
    return render_template('Login_Page.html')

@app.route('/sign_up', methods=["GET", "POST"])
def register():
    msg = ''
    Username = request.form.get('Username')
    Password = request.form.get('Password')
    Name = request.form.get('Name')
    UserID = request.form.get('UserID')
    #if request.method == 'POST':
        
        
    conn = psycopg2.connect("postgres://scrabble_db_user:2JjvW1gU3XXmBbtU3ranf8JX7WBoGfeo@dpg-cgv0079euhlk3uujt5q0-a.oregon-postgres.render.com/scrabble_db")
    cur = conn.cursor()
        
    cur.execute('SELECT* FROM Users WHERE Username = %s', (Username,))
    account = cur.fetchone()
    conn.close()
    if account:
        msg = 'Account already exists'
        #elif not re.match(r'[A-Za-z0-9]+', Username):
            #msg = 'Username must contain only either characters and/or numbers'
        #elif not Username or not Password or not Name:
            #msg = 'Please fill out the form'
        #else:
            #conn = psycopg2.connect("postgres://scrabble_db_user:2JjvW1gU3XXmBbtU3ranf8JX7WBoGfeo@dpg-cgv0079euhlk3uujt5q0-a.oregon-postgres.render.com/scrabble_db")
            #cur = conn.cursor()
            #cur.execute('INSERT INTO Users (userID, Username, password, Name) VALUES (% s, % s, % s, % s)', (UserID, Username, Password, Name, ))
            #msg = 'You have successfully registered'
            #conn.close()
    #elif request.method == 'POST':
        #msg = 'Please fill out the form'
    return render_template('Register_User.html', msg=msg)

@app.route('/about')
def about():
    return render_template('about_page.html')

@app.route('/search_results/<search_word>')
def search_results(search_word=None):
    return render_template('search_results.html', search_word)

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



