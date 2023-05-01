import psycopg2
from datetime import date

def insert(score, id):
    '''
    function that takes two int inputs: score and id#
    inserts top 10 scores for user into db
    returns no value
    '''
    conn = psycopg2.connect("postgres://scrabble_db_user:2JjvW1gU3XXmBbtU3ranf8JX7WBoGfeo@dpg-cgv0079euhlk3uujt5q0-a.oregon-postgres.render.com/scrabble_db")
    cur = conn.cursor()
    cur.execute('SELECT MAX(scoreNum) FROM ScoreHistory WHERE userID = %s;', [id])
    
    #query db for mac score min score and # of user scores in db
    maxScoreNum = cur.fetchall()
    maxScoreNum = maxScoreNum[0][0]
    cur.execute('SELECT MAX(score) FROM ScoreHistory WHERE userID = %s;', [id])
    maxScore = cur.fetchall()
    maxScore = maxScore[0][0]
    cur.execute('SELECT MIN(score) FROM ScoreHistory WHERE userID = %s;', [id])
    minScore = cur.fetchall()
    minScore = minScore[0][0]
    
    #get date for day of score input
    Date = date.today()
    if !maxscoreNum:
        cur.execute('INSERT INTO ScoreHistory (userID, date, scoreNum, score) Values (%s, %s, %s, %s);', (id, Date, 1, score))
    #if less than 10 total scores for user in db score will be added
    elif maxScoreNum < 10:
        #add at front if greater than max score
        if score > maxScore:
            for i in range(maxScoreNum, 0, -1):
                cur.execute('UPDATE ScoreHistory SET scoreNum = %s WHERE (userID = %s AND scoreNum = %s);', (i+1, id, i))
            cur.execute('INSERT INTO ScoreHistory (userID, date, scoreNum, score) Values (%s, %s, %s, %s);', (id, Date, 1, score))
        #if less than min score add at end
        elif score < minScore:
            cur.execute('INSERT INTO ScoreHistory (userID, date, scoreNum, score) Values (%s, %s, %s, %s);', (id, Date, maxScoreNum+1, score))
        #if in the middle add after next highest score
        else:
            cur.execute('SELECT MIN(scoreNum) FROM ScoreHistory WHERE userID = %s AND score < %s;', (id, score))
            updateScoreNum = cur.fetchall()
            updateScoreNum = updateScoreNum[0][0]
            for i in range(maxScoreNum, updateScoreNum-1, -1):
                cur.execute('UPDATE ScoreHistory SET scoreNum = %s WHERE userID = %s AND scoreNum = %s;', (i+1, id, i))
            cur.execute('INSERT INTO ScoreHistory (userID, date, scoreNum, score) Values (%s, %s, %s, %s);', (id, Date, updateScoreNum, score))
    #if 10 scores in db for user add score if greater han lowest score
    else:
        #if greater than min score add to db
        if score > minScore:
            cur.execute('DELETE FROM ScoreHistory WHERE userID = %s AND scoreNum = 10;', [id])
            if score > maxScore:  
                for i in range(maxScoreNum-1, 0, -1):
                    cur.execute('UPDATE ScoreHistory SET scoreNum = %s WHERE userID = %s AND scoreNum = %s;', (i+1, id, i))
                cur.execute('INSERT INTO ScoreHistory (userID, date, scoreNum, score) Values (%s, %s, %s, %s);', (id, Date, 1, score))
            else:
                cur.execute('SELECT MIN(scoreNum) FROM ScoreHistory WHERE userID = %s AND score < %s;', (id, score))
                updateScoreNum= cur.fetchall()
                updateScoreNum = updateScoreNum[0][0]
                for i in range(maxScoreNum, updateScoreNum-1, -1):
                    cur.execute('UPDATE ScoreHistory SET scoreNum = %s WHERE userID = %s AND scoreNum = %s;', (i+1, id, i))
                cur.execute('INSERT INTO ScoreHistory (userID, date, scoreNum, score) Values (%s, %s, %s, %s);', (id, Date, updateScoreNum, score))

    conn.commit()
    conn.close()
    return