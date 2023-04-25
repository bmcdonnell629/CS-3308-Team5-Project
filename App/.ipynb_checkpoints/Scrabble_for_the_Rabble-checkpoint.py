from flask import Flask, url_for, escape, render_template, session, request
import psycopg2
import wordScript
import free_letter_wordScript
from datetime import date

app = Flask(__name__)


@app.route('/')
def login():
    return 'Login Page'

@app.route('/sign_up')
def register():
    sg = ''
    if request.method == 'POST' and 'Username' in request.form and 'Password' in request.form and 'Name' in request.form:
        Username = request.form['Username']
        Password = request.form['Password']
        Name = request.form['Name']
        
        conn = psycopg2.connect("postgres://scrabble_db_user:2JjvW1gU3XXmBbtU3ranf8JX7WBoGfeo@dpg-cgv0079euhlk3uujt5q0-a.oregon-postgres.render.com/scrabble_db")
        cur = conn.cursor()
        
        cur.execute('SELECT * FROM form WHERE Username = %s', (Username,))
        account = cur.fetchone()
        
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[A-Za-z0-9]+', Username):
            msg = 'Username must contain only either characters and/or numbers!'
        elif not Username or not Password or not Name:
            msg = 'Please fill out the form'
        else:
            cursor.execute('INSERT INTO accounts Users (NULL, %s, %s, %s)', (Username, Password, Name,))
            mysql.connection.commit()
            msg = 'You have successfully registered'
    elif request.method == 'POST':
        msg = 'Please fill out the form'
    return render_template('register.html', msg=msg)

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
        cur.execute('SELECT * FROM SearchHistory WHERE userID = %s ORDER BY searchNum ASC;', [id])
        search = cur.fetchall()

        conn.close()
        template = 'SearchHistory.html'
    except:
        template = 'SearchHistoryFailure.html'
    
    return render_template(template, search = search)


def scoreInsert(score, id):
    print('starting')
    print(id, " ", score)
    conn = psycopg2.connect("postgres://scrabble_db_user:2JjvW1gU3XXmBbtU3ranf8JX7WBoGfeo@dpg-cgv0079euhlk3uujt5q0-a.oregon-postgres.render.com/scrabble_db")
    cur = conn.cursor()
    print('connected')
    cur.execute('SELECT MAX(scoreNum) FROM ScoreHistory WHERE userID = %s;', [id])
    maxScoreNum = cur.fetchall()
    maxScoreNum = maxScoreNum[0][0]
    cur.execute('SELECT MAX(score) FROM ScoreHistory WHERE userID = %s;', [id])
    maxScore = cur.fetchall()
    maxScore = maxScore[0][0]
    cur.execute('SELECT MIN(score) FROM ScoreHistory WHERE userID = %s;', [id])
    minScore = cur.fetchall()
    minScore = minScore[0][0]
    Date = date.today()
    print(maxSCoreNum, " ", maxScore, " ", minScore)
    if maxScoreNum < 10:
        if score > maxScore:
            for i in range(maxScoreNum, 0, -1):
                cur.execute('UPDATE ScoreHistory SET scoreNum = %s WHERE (userID = %s AND scoreNum = %s);', (i+1, id, i))
                print('updateing')
            cur.execute('INSERT INTO ScoreHistory (userID, date, scoreNum, score) Values (%s, %s, %s, %s);', (id, Date, 1, score))
            print('inserted')
        elif score < minScore:
            cur.execute('INSERT INTO ScoreHistory (userID, date, scoreNum, score) Values (%s, %s, %s, %s);', (id, Date, maxScoreNum+1, score))
        else:
            cur.execute('SELECT MAX(scoreNum) FROM ScoreHistory WHERE userID = %s AND score < %s;', (id, score))
            updateScoreNum= cur.fetchall()
            for i in range(maxScoreNum, updateScoreNum-1, -1):
                cur.execute('UPDATE ScoreHistory SET scoreNum = %s WHERE userID = %s AND scoreNum = %s;', (i+1, id, i))
            cur.execute('INSERT INTO ScoreHistory (userID, date, scoreNum, score) Values (%s, %s, %s, %s);', (id, Date, updateScoreNum, score))
    else:
        if score > minScore:
            cur.execute('DELETE FROM ScoreHistory WHERE userID = %s AND scoreNum = 10;', [id])
            if score > maxScore:  
                for i in range(maxScoreNum-1, 0, -1):
                    cur.execute('UPDATE ScoreHistory SET scoreNum = %s WHERE userID = %s AND scoreNum = %s;', (i+1, id, i))
                cur.execute('INSERT INTO ScoreHistory (userID, date, scoreNum, score) Values (%s, %s, %s, %s);', (id, Date, 1, score))
            else:
                cur.execute('SELECT MAX(scoreNum) FROM ScoreHistory WHERE userID = %s AND score < %s;', (id, score))
                updateScoreNum= cur.fetchall()
                for i in range(maxScoreNum, updateScoreNum-1, -1):
                    cur.execute('UPDATE ScoreHistory SET scoreNum = %s WHERE userID = %s AND scoreNum = %s;', (i+1, id, i))
                cur.execute('INSERT INTO ScoreHistory (userID, date, scoreNum, score) Values (%s, %s, %s, %s);', (id, Date, updateScoreNum, score))

    conn.commit()
    conn.close()
    return


@app.route('/user_score', methods=["GET", "POST"])
def score():
    scores = []
    if request.method == "POST":
        score = request.form.get('Score')
        print(score)
        try:
            id = 1
            
            scoreInsert(score, id)
            
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



