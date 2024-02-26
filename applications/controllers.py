import json
import os
from flask import Flask, request, redirect, url_for
from flask import render_template
from applications.models import *
from flask import current_app as app
from sqlalchemy.sql import text
from datetime import date, timedelta
import requests
from sqlalchemy.sql import text
from sqlalchemy import union, intersect
from flask import session
import base64
from PIL import Image
from io import BytesIO
from datetime import datetime

app.secret_key = 'your_secret_key'


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', 'https://editor.swagger.io')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


@app.route("/", methods=["GET", "POST"])
def a1():
    if request.method == "GET":
        session.clear()
        return render_template("login_page.html", disp="TRUE")
    elif request.method == "POST":
        name = request.form["name"]
        pass_word = request.form["password"]
        ch = request.form["ch"]
        if ch == "1":
                user = Users.query.filter_by(username=name).first()
                if user is not None:
                    if user.username == name and user.password == pass_word:

                        session["id"]=user.user_id

                        v=User_details.query.filter_by(user_id=session["id"]).first()
                        last_date = datetime.strptime(v.last_login_date, "%d-%m-%Y").date()
                        current_date = datetime.now().date()
                        difference = (current_date - last_date).days
                        v.login_streak=1 if difference>1 else (v.login_streak+1 if difference==1 else v.login_streak)
                        v.last_login_date=current_date.strftime("%d-%m-%Y")
                        db.session.commit() 

                        photo=User_details.query.filter(User_details.user_id == session["id"]).first().photo
                        blob_data = base64.b64decode(photo)
                        image = Image.open(BytesIO(blob_data))

                        session["current_directory"]=os.getcwd()
                        print(image.save(session["current_directory"]+f"\\static\\img\\{user.user_id}.png"))
                        image.save(session["current_directory"]+f"\\static\\img\\{user.user_id}.png")
                        return redirect(url_for('a3'))
                    else:
                        return render_template("login_page.html", disp="", content="*Password is not correct")
                else:
                    return render_template("login_page.html", disp="", content="*Username does not exist")
        else:
            try:
                db.session.add(Users(username=name,name=name,password=pass_word))
                db.session.commit()
                return render_template("index.html")
            except:
                return render_template("login_page.html", disp="", content="*Username already exists")


@app.route("/update",methods=["GET", "POST"])
def a2():
    if request.method=="POST":
        req=request.json
        id=req["post_id"]
        status=req["status"]
        for i in Posts.query.filter_by(post_id=int(id)).all():
            if status:
                i.likes=i.likes+1
            else:
                i.likes=i.likes-1
        
        db.session.commit()
        return ""


@app.route("/feed", methods=["GET", "POST"])
def a3():
    if request.method == "GET":
        try:
            id=session["id"]
            query=[i[0] for i in db.session.execute(text('''SELECT us.username from users as us inner join 
                    posts as ps on ps.user_id=us.user_id ORDER BY ps.likes DESC LIMIT 5''')).all()]
            my_lks=[i for i in db.session.execute(text(f'''SELECT sum(ps.likes) from users as us inner join 
                    posts as ps on ps.user_id=us.user_id where us.user_id ={id}''')).all()][0][0]
            
            con=" "
            response = requests.get(f"http://127.0.0.1:8080/api/posts/{con}")
            if response.status_code == 200:
                data_from_api = response.json()
                for i in data_from_api:
                    blob_data = base64.b64decode(i["content"])
                    image = Image.open(BytesIO(blob_data))
                    id=i["post_id"]
                    c=Users.query.filter_by(user_id=i["user_id"]).first()
                    i["username"] = c.username
                    i["name"] = c.name
                    image.save(session["current_directory"]+f"\static\img\{id}.png") 
                return render_template("index.html",posts=data_from_api,most_liked=query,my_likes=my_lks)
            else:
                return "Failed to fetch data from the API", 500
        except  Exception as e:
            return "Failed to fetch data from the API",500
    


@app.route("/search", methods=["GET","POST"])
def a4():
    if request.method == "GET":
        try:
            return render_template("search.html")
        except:
            return "Failed to fetch data from the API", 500
    elif request.method == "POST":
        con=request.form["user_search"]
        response = requests.get(f"http://127.0.0.1:8080/api/users/{con}")
        response1 = requests.get(f"http://127.0.0.1:8080/api/posts/{con}")
        data_from_api=[]
        data_from_api1=[]
        if response.status_code == 200 and response1.status_code==200:
            data_from_api = response.json()
            data_from_api1 = response1.json()
            for i in data_from_api:
                photo=User_details.query.filter(User_details.user_id == i["user_id"]).first().photo
                blob_data = base64.b64decode(photo)
                image = Image.open(BytesIO(blob_data))
                id=i["user_id"]
                image.save(session["current_directory"]+f"\static\img\{id}.png")
            for i in data_from_api1:
                blob_data = base64.b64decode(i["content"])
                image = Image.open(BytesIO(blob_data))
                id=i["post_id"]
                image.save(session["current_directory"]+f"\static\img\{id}.png")
        return render_template("search.html",users=data_from_api,posts=data_from_api1)



@app.route("/post", methods=["GET", "POST"])
def a5():
    if request.method == "GET":
        try:
            return render_template("post.html")
        except:
            return "Failed to fetch data from the API", 500



@app.route("/profile", methods=["GET", "POST"])
def a6():
    if request.method == "GET":
        try:
            user1 = Users.query.filter(Users.user_id == session["id"]).first()
            user2= User_details.query.filter(User_details.user_id ==session["id"]).first()
            return render_template("profile.html",userdet=user2,user=user1)
        except Exception as e:
            return "Failed to fetch data from the API",500
    elif request.method == "POST":
        try:
            req=request.json
            user1 = Users.query.filter(Users.user_id == session["id"]).first()
            user2= User_details.query.filter(User_details.user_id ==session["id"]).first()
            if req['element']=="name":
                user1.name=req["value"]
            elif req['element']=="email":
                user2.email=req["value"]
            elif req['element']=="bio":
                user2.bio=req["value"]
            elif req['element']=="gender":
                user2.gender=req["value"]
            elif req['element']=='phone':
                user2.phone=int(req['value'])
            db.session.commit()
            return ""
        except Exception as e:
            return "Failed to fetch data from the API",500



@app.route("/post_image", methods=["GET", "POST"])
def a7():
    if request.method == "POST":
        try:
            bytes_data = (request.files['image']).read()
            # image_base64=base64.b64encode(bytes_data)            
            # # print(type(image_bytes),type(image_base64),type(capt))
            db.session.add(Posts(caption=request.form.get('capt'),likes=0,user_id=session["id"]))
            db.session.commit()
            return redirect(url_for('a5'))
        except Exception as e:
            return "Failed to fetch data from the API", 500
