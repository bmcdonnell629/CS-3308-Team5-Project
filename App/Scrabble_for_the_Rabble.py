from flask import Flask
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
    return "Search History"

@app.route('/user_score')
def score():
    return "Score Page"



