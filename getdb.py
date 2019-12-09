import pymongo
from bson.objectid import ObjectId

#conn = pymongo.MongoClient('mongodb://localhost', 27017)
conn = pymongo.MongoClient('mongodb://blackruby:b1ackruby@13.209.225.92', 27017)
#conn = pymongo.MongoClient('mongodb://hyeonwoo:blAckRuby!@127.0.0.1', 27018)

#conn = pymongo.MongoClient('mongodb://hyeonwoo:blAckRuby!@fanrep-ver2-db.cluster-cjickd1ydhwd.ap-northeast-2.docdb.amazonaws.com:27017') 
#'mongodb://localhost:27017   mongodb://blackruby:b1ackruby@13.209.225.92    mongodb://hyeonwoo:blAckRuby!@fanrep-ver2-db.cluster-cjickd1ydhwd.ap-northeast-2.docdb.amazonaws.com:27017/fanrep2
db = conn.get_database('fanrep2') 

abc = list(db.comments.find({"_id": ObjectId("5db2a261c50529ea5c7e114e")}))

artists = list(db.artists.find({"followers": {"$gt": 1}}, {"_id": 0, "type": 1, "followers": 1}))

user = list(db.users.find({"likes": {"$exists": True}},{"_id": 1}))
'''
user2 = db.users.aggregate([{
       "$project": {
          "_id": {
             "$toString": "$_id"
                }}}])
'''

alarmuser = list(db.users.find({'is_notified': True}))

badges = list(db.badges.find({}))

comment = list(db.comments.find({"_id": ObjectId("5d9ed7437fb82f822171cbb3")}))

getuserid = db.posts.find_one({"_id": ObjectId("5d9ef7a00f7a3f4816cf7e0f")}, {"user._id": 1})

post = db.posts.find_one({"_id": ObjectId("5dafb6a481569efc09ce0ea9")})

eventbadges = list(db.badges.find({"event": {"$exists": True}}))

user = db.users.find_one({"token": '08YLaHH6iCFeGg8wmBYna7weguvAXgDZPjcRWAopdbMAAAFuM8h8Cg'})

test = list(db.comments.aggregate([
        {'$match' : {'cocomments._id': ObjectId("5dc24fb080e926ca7146374c")}}
        ,{'$project' : { '_id' : 0, 
            'cocomments': {'$filter': {
            'input': '$cocomments',
            'as': 'cocomments',
            'cond': {'$eq': ['$$cocomments._id', ObjectId("5dc24fb080e926ca7146374c")]}}}}}
        ,{'$unwind' : '$cocomments'}  
        ]))

# test2 = db.comments.find_one({'cocomments._id': ObjectId("5dc3bd4835a64569e5fd7d65")}, {'cocomments.$': 1})['cocomments'][0]

a = 'Zz'
test3 = list(db.users.find({'nickname': {'$regex': '^' + a }}).limit(3))

b = [{
			"_id" : "5d6c8a05d204852c606dd745",
			"type" : "x1",
			"en_name" : "X1",
			"ko_name" : "엑스원",
			"img" : "https://d2bf187k2967hr.cloudfront.net/static_files/idol_image/x1.png"
		}]

c = "x1"

test4= list(db.users.find({'following': {'$regex': ".*{}.*".format(c) }}).limit(3))

test5= list(db.users.find({'following': {'$in': b }}).limit(3))

artists2 = list(db.artists.find({"type": {"$nin": ["fanrep"]}}, {"followers": 0} ))

#뱃지정보     
without_event_badges = list(db.badges.find({"event": {"$exists": False}}))
without_event_badges.sort(key=lambda badge: badge['needed_counts'])
likes_badges = [badge for badge in without_event_badges if badge['badge_collection'] == 'likes']
posts_badges = [badge for badge in without_event_badges if badge['badge_collection'] == 'posts']
comments_badges = [badge for badge in without_event_badges if badge['badge_collection'] == 'comments']

class FollowersCount():
    def get():
        sumval = 0
        count = 0

        for row in artists:
            sumval = sumval + artists[count]["followers"]
            count = count + 1

        return sumval


    def get2(**updated_user):
        for updated_key, updated_value in updated_user.items():
            a = updated_key
            if a == 'nickname':
                b = "bbb"
            else:
                b = 'ccc'
        return b


    def get3():
        return {1}, 2, {3}


class getUserBadge():
    def get(uid):
        badge = list(db.users.find({"_id": ObjectId(uid)}))         #ObjectId("5d9449f9c0d710129a27ab4e")}))   #ObjectId(uid)}))

        return badge

    def is_my_badge(badge_id):
        my_badge_ids = {badge_id for badge_id in
                        user.get('badge_ids', [])}
        if badge_id in my_badge_ids:
            return True
        return False


class cocoget():
    def get(item):
        comment_ids = item.pop('comment_ids')
        count_cocomments_query = [
            {"$match": {"_id": {"$in": comment_ids}}},
            {"$unwind": "$cocomments"},
            {"$group": {"_id": None, "cocomment_counts": {"$sum": 1}}}
        ]
        cocomment_aggr = list(db.comments.aggregate(count_cocomments_query))

        return cocomment_aggr


class tuserget():
    def get():
        tuser_query = [
            {"$group" : { "_id": "$uid", "count": { "$sum": 1 } } },
            {"$match": {"_id" :{ "$ne" : None } , "count" : {"$gt": 1} } }
        ]
        tuser_aggr = list(db.users.aggregate(tuser_query))

        return tuser_aggr


class alluserget():
    def get(uid):
        alluserdata = list(db.users.find({'uid': uid}))
        return alluserdata
    def set(_id, o_id):
        me = ObjectId(_id)
        db.users.update({"_id": me}, {"$set": {"uid": "", "token": "", "fcmToken": ""}})
        db.comments.update({"likes": ObjectId(_id)}, {'likes.$': ObjectId(o_id)}) 
        db.users.update({"_id": me}, {"$set": {"uid": "", "token": "", "fcmToken": ""}})
        db.users.update({"_id": me}, {"$set": {"uid": "", "token": "", "fcmToken": ""}})
        db.users.update({"_id": me}, {"$set": {"uid": "", "token": "", "fcmToken": ""}})

class testttt():
    def get(uid):
        #유저별 처리 
        me = ObjectId(uid)

        #유저뱃지 정보 
        my_badges = list(db.users.find({"_id": me}, {"badge_ids": 1}))

        #좋아요, 개시글, 댓글 수 count
        likes = db.users.find_one({"_id": me})['likes']
        likescount = len(likes['schedule_ids']) + len(likes["feed_ids"]) + len(likes['post_ids']) + len(likes['comment_ids']) + len(likes['cocomment_ids'])
        posts = list(db.posts.find({"user._id": me}))
        postscount = len(posts)
        comments = list(db.comments.find({"user._id": me}))
        commentscount = len(comments)
        cocomments = list(db.comments.aggregate([{"$match" : {"cocomments.user._id" : me}}, {"$unwind": "$cocomments"}, {"$group": {"_id": None, "count":{"$sum": 1}}}]))
        
        if not cocomments:
            cocommentscount = 0
        else:
            cocommentscount = cocomments[0]['count']
        commentssum = commentscount + cocommentscount

        #좋아요 뱃지 체크 후 업데이트 뒤에서부터 보유 뱃지 발견후 종료  좋아요뱃지가 중간에 추가되면 break->continue 변경
        for likebadge in reversed(likes_badges):
            if likebadge['needed_counts'] <= likescount:
                if likebadge['_id'] in my_badges[0]['badge_ids']:
                    break
                else:
                    db.users.update({"_id": me}, {"$addToSet": {"badge_ids": likebadge['_id']} })
            else:
                continue

        #개시글 뱃지 체크 후 업데이트 
        for postbadge in reversed(posts_badges):
            if postbadge['needed_counts'] <= postscount:
                if postbadge['_id'] in my_badges[0]['badge_ids']:
                    break
                else:
                    db.users.update({"_id": me}, {"$addToSet": {"badge_ids": postbadge['_id']} })
            else:
                continue  
  
        #댓글글 뱃지 체크 후 업데이트 
        for commentbadge in reversed(comments_badges):
            if commentbadge['needed_counts'] <= commentssum:
                if commentbadge['_id'] in my_badges[0]['badge_ids']:
                    break
                else:
                    db.users.update({"_id": me}, {"$addToSet": {"badge_ids": commentbadge['_id']} })
            else:
                continue

        return '완료' #+ counts + badge


# class getNickname():
#     def get(nickname, type):
#         hnickname = list(db.users.find({'nickname': {'$regex': '^' + nickname }}, 'following': type}   ).limit(3))
#         return hnickname



