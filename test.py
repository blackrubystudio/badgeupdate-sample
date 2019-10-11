from flask import Flask, url_for
from bson.objectid import ObjectId
import getdb
import config
import datetime

app = Flask(__name__)


@app.route('/test/')
def test():
    data = getdb.FollowersCount.get()
    return str(data)  # artists[3]['followers']


@app.route('/test2/<un>')
def test_un(un):
    return 'test : ' + un


@app.route('/getuser/')
def getuser():
    #user_id = getdb.user2
    #user_nick = getdb.user[0]["nickname"]


    userid = ['test']
    count = 0

    for user in getdb.user:
        #userid = str(getdb.user[count]['_id'])   
        #userid.append(str(getdb.user[count]['_id']))   
        userid.append(getdb.user[count]['_id']) 
        count = count + 1

    #print(userid, count)
    badge = getdb.getUserBadge.get(userid.pop())

    print( badge[0]['_id'] )

    return '33' #badge['uid']
    '''
    if userid is None: 
        return 'empty'
    else:
        return userid.pop()
    '''

    
@app.route('/bedgeupdate/')
def bedgeupdate():
    
    now = datetime.datetime.now()
    print('시작', now)
    abc = '종료'
    userid = ['test']
    count = 0

    for user in getdb.user:  
        userid = str(getdb.user[count]['_id'])     
        print(userid, count)
        getdb.testttt.get(userid)
        count = count + 1

    print(abc, datetime.datetime.now() - now)
    return abc 


if __name__ == "__main__":
    with app.test_request_context():
        print(url_for('getuser'))
        print(url_for('test'))
        print(url_for('test_un', un='test')) 
        print(url_for('bedgeupdate')) 
    app.run('localhost', 5000)  

