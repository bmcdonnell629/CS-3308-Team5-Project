import psycopg2
from datetime import date

def insert(score, id):
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
    print(maxScoreNum, " ", maxScore, " ", minScore)
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