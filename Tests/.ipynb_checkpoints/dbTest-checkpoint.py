#!/usr/bin/env python3
import func
import psycopg2

def test_scoreInsert():
    #create cursor
    conn = psycopg2.connect("postgres://scrabble_db_user:2JjvW1gU3XXmBbtU3ranf8JX7WBoGfeo@dpg-cgv0079euhlk3uujt5q0-a.oregon-postgres.render.com/scrabble_db")
    cur = conn.cursor()
    # get test userID
    cur.execute("SELECT userID FROM Users where username = 'test';")
    id = cur.fetchone()
    id = id[0]
    
    #get scoreNum to know if table is full
    cur.execute('SELECT MAX(scoreNum) FROM scoreHistory WHERE userID = %s;', [id])
    scoreNum = cur.fetchone()
    scoreNum = scoreNum[0]
    flag = 0
    #insert above and below max and min score into table
    if scoreNum < 10:
        cur.execute('SELECT MAX(score) FROM scoreHistory WHERE userID = %s;', [id])
        maxScore = cur.fetchone()
        maxScore = maxScore[0]
    
        cur.execute('SELECT MIN(score) FROM scoreHistory WHERE userID = %s;', [id])
        minScore = cur.fetchone()
        minScore = minScore[0]
    
        #test the insertion is succesful 
        tests = [
            [id, maxScore + 1, maxScore + 1, 'SELECT MAX(score) FROM scoreHistory WHERE userID = 27;', 'Did not properly insert max score', 'Properly inserted max score with  non full score table'],
            [id, minScore - 1, minScore -1, 'SELECT MIN(score) FROM scoreHistory WHERE userID = 27;', 'Did not properly handle inserts less than top 10', 'Properly inserted min score with  non full score table']
        ]
        #iterate over tests
        for test in tests:
            print( test[1], test[0])
            func.scoreInsert(test[1], test[0])
            cur.execute(test[3])
            testNum = cur.fetchone()
            #test that string of query results matches testing value
            try:
                assert testNum[0] == test[2]
                print(test[5])
            #if eception print error from tests
            except:
                print(test[4])
                flag = 1
            scoreNum += 1
            if scoreNum == 10:
                break
    #if table is full    
    if scoreNum == 10:
        #insert above and below max and min
        cur.execute('SELECT MAX(score) FROM scoreHistory WHERE userID = %s;', [id])
        maxScore = cur.fetchone()
        maxScore = maxScore[0]
    
        cur.execute('SELECT score FROM scoreHistory WHERE userID = %s and scoreNum = 9;', [id])
        minScore = cur.fetchone()
        minScore = minScore[0]
        
        #test thatt new max is inserted and values less thna min are not inserted
        tests = [
            [id, maxScore + 1, maxScore+ 1, 'SELECT MAX(score) FROM scoreHistory WHERE userID = 27;', 'Did not properly insert max score', 'Properly inserted max score with full score table'],
            [id, minScore - 1, minScore, 'SELECT MIN(score) FROM scoreHistory WHERE userID = 27;', 'Did not properly handle inserts less than top 10', 'Properly handled score less than minimum with full table']
        ]
        #iterate over tests
        for test in tests:
            
            func.scoreInsert(test[1], test[0])
            cur.execute(test[3])
            testNum = cur.fetchone()
            #test that string of query results matches testing value
            try:
                assert testNum[0] == test[2]
                print(test[5])
            #if eception print error from tests
            except:
                print(test[4])
                flag = 1
                
    if flag == 0:
        print('All tests succesfully passed')
    conn.close()
        
            
    
        

    

def main():
    test_scoreInsert()

if __name__=="__main__":
    main()