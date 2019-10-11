import os
import boto3


class Config:
    MONGO_URI = os.environ.get("MONGO_URI")


class S3:
    # 기본 bucket 이름
    bucket_name = "fanrep-static-file"
    # return해서 쓸 수 있는  최종 url을 위한 s3 base url
    s3_base_url = os.environ.get("S3_ABSOLUTE_BASE_URL", "https://{}.s3.ap-northeast-2.amazonaws.com".format(bucket_name))


'''
 https://fanrep-static-file.s3.ap-northeast-2.amazonaws.com  

https://fanrep-static-file.s3.ap-northeast-2.amazonaws.com/static_files/badge/comment-65.png
 '''