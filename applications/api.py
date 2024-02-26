from flask_restful import Resource, reqparse
from applications.models import *
from applications.database import db
from applications.validation import *
from flask import jsonify
import json


class UserAPI_posts(Resource):
    def get(self,capt):
        try:
            json_data = []
            if capt==" ":
                a=Posts.query.all()
            else:
                a=Posts.query.filter(Posts.caption.like(f'%{capt}%')).all()
            for row in a:
                record = {"post_id": row.post_id, "caption": row.caption,
                          "likes": row.likes,"content": row.content, "user_id":row.user_id}
                json_data.append(record)
            return json_data, 200
        except:
            return json.dumps({"message":" An internal server error occurred."}), 500
class UserAPI_users(Resource):
    def get(self,user_n):
        try:
            json_data = []
            if user_n==" ":
                a=Users.query.all()
            else:
                a=Users.query.filter(Users.username.like(f'%{user_n}%')).all()
            for row in a:
                record = {"user_id": row.user_id, "username": row.username,
                          "name": row.name , "password": row.password}
                json_data.append(record)
            return json_data, 200
        except:
            return json.dumps({"message":" An internal server error occurred."}), 500

