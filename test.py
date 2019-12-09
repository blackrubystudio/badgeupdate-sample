from flask import Flask, url_for
from bson.objectid import ObjectId
import getdb
import config
from datetime import datetime
import re

from operator import itemgetter

app = Flask(__name__)


@app.route('/test/')
def test():
    '''data3 = getdb.getuserid
    data4 = data3['user']['_id']
    data2 = getdb.comment
    data = data2[0]['cocomments'][0]['user']['_id']'''

    # post = getdb.post
    # comment_counts = len(post['comment_ids'])
    # cocomment_aggr = getdb.cocoget.get(post)
    # if not cocomment_aggr:
    #     cocomment_counts = 0
    # else:
    #     cocomment_counts = cocomment_aggr[0]['cocomment_counts']
    
    # comment_counts += cocomment_counts
    # print(comment_counts)

    # cocomment_id = ObjectId()
    # #a = getdb.abc  

    # updated_user = {}
    # updated_user['nickname'] = 'sdfs'
    # getdb.FollowersCount.get2(**updated_user)
    # for c in a:
    #     print(c)

    # b = sorted(a, key=itemgetter('like_counts')

    # for d in b:
    #     print(d)

    #data = getdb.FollowersCount.get()
    # data = {}
    # data = getdb.FollowersCount.get3()
    # print(data[0])
    # print(data[1])
    # print(data[2])

    # badges = getdb.eventbadges
    # to_be_deleted_ids = []
    # for i, badge in enumerate(badges):
    #     if badge.get('event'):
    #             if not getdb.getUserBadge.is_my_badge(badge['_id']):
    #                 to_be_deleted_ids.append(i)
    # for i in reversed(to_be_deleted_ids):
    #     print(badges[i])
    #     del(badges[i])

    # print(badges)      

    # a = getdb.test
    # print(a[0]['cocomments']['comment_to']['to_nickname']) 

    # #sample
    # print('삼항 for if')
    # #삼항
    # a = 3
    # b = True if a==3 else False
    # print(b)
    
    # #for in
    # temp2 = list()
    # temp = [2, 3, 4, 5]
    # for i in temp:
    #     temp2.append(i)
    # print(temp2)

    # # for in one line
    # print([i for i in temp])

    # #삼항 + for + if else
    # print([i*2 if i>3 else i for i in temp])
        

    # #for + if 
    # print([i for i in temp if i>3])

    # print('== != is not')
    # # == != is not  isnot       is, isnot = 값비교 x 레퍼런스비교 상수만 사용할것
    # c = True
    # if c == True:
    #     print("1")
    # elif c!= True:
    #     print("2")

    # if c:
    #     print("3")
    # if not c:
    #     print("4")
        
    # print(c is True)
    # print(c is not True)

    # e = None
    # print (a is not None)
    # print (e is not None)

    # a = getdb.test2
    # print(a['comment_to']['to_nickname'])
    # print(a['comment_to']['to_user_id'])
    # print(a['user']['_id'])

    # str_dt = '#오늘 #뭐해 뭐하긴 #ab cde '
    # pattern = '#\w*[^ \u3131-\u3136*\uac00-\ud7a3*]*\w*[^ \u3131-\u3163\uac00-\ud7a3*]*'
    # pattern = '#([0-9a-zA-Z가-힣]*)'
    # sp = re.compile(pattern)
    # hash_dt = sp.findall(str_dt)      
    # print(hash_dt)
    # for hash_row in hash_dt:
    #     print(hash_row)
    # if hash_dt:
    #     print("33")
    # if not hash_dt:
    #     print("44")
    # print(len(hash_dt))

    # a = getdb.artists2
    # atype = 'bts'
    # c = [b for b in a if b['type'] == atype]  
    # print(c)

    # d = getdb.getNickname.get('Zz', c)
    # print(len(d))

    # counts = 12
    # if counts in [3, 5, 7] or counts // 5 == 0:
    #     print('호')

    tuser_aggr = getdb.tuserget.get()
    badge_ids = []

    for i in tuser_aggr:
        #print(i['_id'], i['count'])
        alluser = getdb.alluserget.get(i['_id'])
        start = 0
        for j in alluser:
            if start == 0:
                #최상위 _id 만 살려놈
                mainid = j['_id']
            else:
                #uid, token, fcmtoken "" 값 채워넣기 
                getdb.alluserget.set(j['_id'], alluser[0]['_id'])
                alluser[0]['badge_ids'] = alluser[0]['badge_ids'] + j['badge_ids']
                alluser[0]['likes']['schedule_ids'] = alluser[0]['likes']['schedule_ids'] + j['likes']['schedule_ids']
                alluser[0]['likes']['feed_ids'] = alluser[0]['likes']['feed_ids'] + j['likes']['feed_ids']
                alluser[0]['likes']['post_ids'] = alluser[0]['likes']['post_ids'] + j['likes']['post_ids']
                alluser[0]['likes']['comment_ids'] = alluser[0]['likes']['comment_ids'] + j['likes']['comment_ids']
                alluser[0]['likes']['cocomment_ids'] = alluser[0]['likes']['cocomment_ids'] + j['likes']['cocomment_ids']
                alluser[0]['following'] = alluser[0]['following'] + j['following']
                if alluser[0]['img'] == "https://d2bf187k2967hr.cloudfront.net/static_files/profile/profile_image.png":
                    alluser[0]['img'] = j['img']
                if alluser[0]['nickname'] == "":
                    alluser[0]['nickname'] = j['nickname']
                if alluser[0]['Status_message'] == "":
                    alluser[0]['Status_message'] = j['Status_message']
                #해당 id 의 댓글, 대댓글, 개시글, 
            start = start  + 1
        #j for문 끝나고 중복제거해서 맨앞 id 업데이트

    print(badge_ids)
    return '33' #str(data)  # artists[3]['followers']


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
'''
@app.route('/alarm/')
def alarm():
    user = getdb.alarmuser     
    user_counts = len(user)

    counts = user_counts 
    for i in range(counts):
        try:
            a = len("fSsPv4rqyyg:APA91bFp6BB7Oy0WUiQFI1XDjqyY5U9zS6w6nA_JLMDPTF2KVCliKPcaaUQubZfZGZb9E5xcZN8ZXciIA4try7SznYXzfKIAO01qV8raX36ikmZeIUCmSe4s8erhz9h7qNSU7ojpLEfJ")
            b = len("fNlxDm8hv6s:APA91bEkZ7SZ2rVXFt0G7GCDW4poiKEHjbsLMPiTqw3CvQ6TY9JneulY6NpaW3moXTTe-sTOytDSTBvxX1lUUpo9kbYeo7RMFV1migWkCW8I5_4DAGcK6w5MlU6049rTmYsf_uKxrRKX")
   
            print(i, "번째 작업 시작")
            sliced_users = user[1000*i:1000*(i+1)]
            # 1000명 단위로 잘라, device_key들의 list를 만들어 알림 보냄.
            print(i, "번째 작업 map user")
            user_device_keys = map(lambda user: user['fcmToken'], sliced_users)
            print(i, "번째 작업 map user 후")
            user_device_keys = list(user_device_keys)
            print(i, "번째 작업 Notification 생성")
            notification = Notification(title, body, user_device_keys)
            print(i, "번째 작업 push_notification 호출")
            notification.push_notification()   
        except:
            print(i, "번째 error")'''


if __name__ == "__main__":
    with app.test_request_context():
        print(url_for('getuser'))
        print(url_for('test'))
        print(url_for('test_un', un='test')) 
        print(url_for('bedgeupdate')) 
        #print(url_for('alarm')) 

    app.run('127.0.0.1', 5001)  

