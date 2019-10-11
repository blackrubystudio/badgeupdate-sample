import pymongo
from bson.objectid import ObjectId

#conn = pymongo.MongoClient('13.209.225.92', 27017)

conn = pymongo.MongoClient('mongodb://localhost:27017') 
#'mongodb://localhost:27017   mongodb://blackruby:b1ackruby@13.209.225.92    mongodb://hyeonwoo:blAckRuby!@fanrep-ver2-db.cluster-cjickd1ydhwd.ap-northeast-2.docdb.amazonaws.com:27017/fanrep2
db = conn.get_database('fanrep2')


artists = list(db.artists.find({"followers": {"$gt": 1}}, {
               "_id": 0, "type": 1, "followers": 1}))

user = list(db.users.find({"likes": {"$exists": True}},{"_id": 1}))

user2 = db.users.aggregate([{
       "$project": {
          "_id": {
             "$toString": "$_id"
                }}}])

badges = list(db.badges.find({}))

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


class getUserBadge():
    def get(uid):
        badge = list(db.users.find({"_id": ObjectId(uid)}))         #ObjectId("5d9449f9c0d710129a27ab4e")}))   #ObjectId(uid)}))

        return badge


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



