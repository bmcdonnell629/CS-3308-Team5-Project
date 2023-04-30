from flask import Flask, url_for, escape, render_template, session, request
import psycopg2
import wordScript
import free_letter_wordScript
import scoreInsert
import get_anagrams
import advanced_filters

app = Flask(__name__)
app.secret_key = 'Scrabble'

@app.route('/', methods=['GET', 'POST']) 
def search():
    return render_template('search_page.html')

@app.route('/login',  methods=["GET", "POST"])
def login():
    msg = ''
    Username = request.form.get('Username')
    Password = request.form.get('Password')
    print(Username, Password)
    conn = psycopg2.connect("postgres://scrabble_db_user:2JjvW1gU3XXmBbtU3ranf8JX7WBoGfeo@dpg-cgv0079euhlk3uujt5q0-a.oregon-postgres.render.com/scrabble_db")
    cur = conn.cursor()
    
    if request.method == 'POST':
        cur.execute('SELECT* FROM Users WHERE Username = %s AND password = %s;', (Username, Password))
        LoggedInUser = cur.fetchone()
        if LoggedInUser:
            #session['loggedin'] = True
            #session['id'] = LoggedInUser['userID']
            session['user'] = Username
            msg = 'Logged in successfully'
        else:
            msg = 'Username/Password is incorrect'
    conn.close()
    return render_template('Login_Page.html', msg=msg)

@app.route('/logout')
def logout():
    #session.clear()
    session.pop('user')         
    return render_template('Login_Page.html')

@app.route('/sign_up', methods=["GET", "POST"])
def register():
    msg = ''
    Username = request.form.get('Username')
    Password = request.form.get('Password')
    Name = request.form.get('Name')
    print(Username, Password, Name)
    conn = psycopg2.connect("postgres://scrabble_db_user:2JjvW1gU3XXmBbtU3ranf8JX7WBoGfeo@dpg-cgv0079euhlk3uujt5q0-a.oregon-postgres.render.com/scrabble_db")
    cur = conn.cursor()
    cur.execute('SELECT MAX(UserID) FROM Users;')
    maxUserID = cur.fetchall()
    maxUserID = maxUserID[0][0]
    if request.method == 'POST':
        cur.execute('SELECT* FROM Users WHERE Username = %s;', [Username])
        account = cur.fetchone()
        if account:
            msg = 'Username Already Exists, Please Use A Different Username'
        else:
            cur.execute('INSERT INTO Users (userID, name, Username, password) VALUES (%s,%s,%s,%s);', (maxUserID+1, Name, Username, Password))    
            conn.commit()
            conn.close()
            msg = 'User Added Successfully'

    return render_template('Register_User.html', msg=msg)

@app.route('/Users_Table')
def UsersTable():
    Users = []
       #open connection to db
    conn = psycopg2.connect("postgres://scrabble_db_user:2JjvW1gU3XXmBbtU3ranf8JX7WBoGfeo@dpg-cgv0079euhlk3uujt5q0-a.oregon-postgres.render.com/scrabble_db")
    cur = conn.cursor()
    
    id = 1
    cur.execute('SELECT * FROM Users;')
    Users = cur.fetchall()

    conn.close()
    return Users

@app.route('/about')
def about():
    return render_template('about_page.html')

@app.route('/search_results')
def show_results():
    search_word = request.args.get('search_word')
    allow_anagrams = request.args.get('allow_anagrams')
    min_letters = request.args.get('min_letters')
    max_letters = request.args.get('max_letters')
    starts_with = request.args.get('starts_with')
    ends_with = request.args.get('ends_with')
    contains = request.args.get('contains')
    fixed_letters = request.args.get('fixed_letters')
    
    result_list = get_anagrams.find_anagrams(search_word)
    
    if allow_anagrams == "false":
        result_list = advanced_filters.remove_anagrams(search_word, result_list)
    
    result_list = advanced_filters.word_length_filter(result_list, min_letters, max_letters)
    result_list = advanced_filters.starts_with_filter(starts_with, result_list)
    result_list = advanced_filters.ends_with_filter(ends_with, result_list)
    result_list = advanced_filters.contains_filter(contains, result_list)
    
    return render_template('search_results.html', result_list=result_list)

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



