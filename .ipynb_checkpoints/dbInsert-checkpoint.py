import psycopg2
from datetime import date

def scoreInsert(score, id):
    '''
    function that takes two int inputs: score and id#
    inserts top 10 scores for user into db
    returns no value
    '''
    conn = psycopg2.connect("postgres://scrabble_db_user:2JjvW1gU3XXmBbtU3ranf8JX7WBoGfeo@dpg-cgv0079euhlk3uujt5q0-a.oregon-postgres.render.com/scrabble_db")
    cur = conn.cursor()
   
    cur.execute('SELECT MAX(scoreNum) FROM ScoreHistory WHERE userID = %s;', [id])

    #query db for mac score min score and # of user scores in db
    maxScoreNum = cur.fetchone()
    if maxScoreNum == None:
        maxScoreNum = None
    else:
        maxScoreNum = maxScoreNum[0]
    cur.execute('SELECT MAX(score) FROM ScoreHistory WHERE userID = %s;', [id])
    maxScore = cur.fetchall()
    maxScore = maxScore[0][0]
    cur.execute('SELECT MIN(score) FROM ScoreHistory WHERE userID = %s;', [id])
    minScore = cur.fetchall()
    minScore = minScore[0][0]
    #get date for day of score input
    Date = date.today()
    if maxScoreNum == None:
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

def searchInsert(id, words, letters):
    conn = psycopg2.connect("postgres://scrabble_db_user:2JjvW1gU3XXmBbtU3ranf8JX7WBoGfeo@dpg-cgv0079euhlk3uujt5q0-a.oregon-postgres.render.com/scrabble_db")

    cur = conn.cursor()   
    #cur.execute('Delete from SearchHistory where userID = 23;')
    print(words)
    word = []
    score = []
    for i in len(words):
        word.append(words[i][0])
        score.append(words[i][1])
    cur.execute('Select MAX(searchNum) from SearchHistory where userID = %s;', [id])
    searchNum = cur.fetchone()
    searchNum = searchNum[0]
    print(searchNum)
    if searchNum == None:
        if len(word) >=5:
            cur.execute('INSERT INTO SearchHistory VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);', (id, 1, letters, word[0], score[0], word[1], score[1], word[2], score[2], word[3], score[3], word[4], score[4]))
        elif len(word) == 0:
                cur.execute('INSERT INTO SearchHistory (userID, searchNum, letters) VALUES (%s, %s, %s);', (id, 1, letters))
        else:
            cur.execute('INSERT INTO SearchHistory (userID, searchNum, letters) VALUES (%s, %s, %s);', (id, 1, letters))
            for i in range(len(word)):
                print(word)
                print(i)
                cur.execute('UPDATE SearchHistory SET word%s = %s , score%s = %s;', (i+1, word[i], i+1, score[i]))
    
    
    else:
        if searchNum == 5:
            cur.execute('DELETE FROM SearchHistory WHERE userID = %s AND searchNum = 5;', [id])
            print('delete')
            for i in range(4,0,-1):
                cur.execute('UPDATE SearchHistory SET searchNum = %s where userID = %s and searchNum = %s;', (i+1, id, i))
            if len(word) >=5:
                cur.execute('INSERT INTO SearchHistory VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);', (id, 1, letters, word[0], score[0], word[1], score[1], word[2], score[2], word[3], score[3], word[4], score[4]))
            elif len(word) == 0:
                cur.execute('INSERT INTO SearchHistory (userID, searchNum, letters) VALUES (%s, %s, %s);', (id, 1, letters))
            else:
                cur.execute('INSERT INTO SearchHistory (userID, searchNum, letters) VALUES (%s, %s, %s);', (id, 1, letters))
                for i in range(len(word)):
                    cur.execute('UPDATE SearchHistory SET word%s = %s , score%s = %s;', (i+1, word[i], i+1, score[i]))
        
        else:
            for i in range(searchNum, 0, -1):
                cur.execute('UPDATE SearchHistory SET searchNum = %s where userID = %s and searchNum = %s;', (i+1, id, i))
            if len(word) >=5:
                cur.execute('INSERT INTO SearchHistory VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);', (id, 1, letters, word[0], score[0], word[1], score[1], word[2], score[2], word[3], score[3], word[4], score[4]))
            elif len(word) == 0:
                cur.execute('INSERT INTO SearchHistory (userID, searchNum, letters) VALUES (%s, %s, %s);', (id, 1, letters))
            else:
                cur.execute('INSERT INTO SearchHistory (userID, searchNum, letters) VALUES (%s, %s, %s);', (id, 1, letters))
                for i in range(len(word)):
                    cur.execute('UPDATE SearchHistory SET word%s = %s , score%s = %s;', (i+1, word[i], i+1, score[i]))
    conn.commit()
    conn.close()
