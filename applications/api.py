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


class UserAPI(Resource):
    def get(self, category_name):
        try:
            n_cat = Category.query.filter(Category.category_name.like(f'%{category_name}%')).all()
        except:
            return json.dumps({"message":" An internal server error occurred."}), 500
        a = []
        for i in n_cat:
            a.append({"category_id": i.category_id, "category_name": i.category_name})
        return a, 200

    def put(self, category_id):
        u_u_p = reqparse.RequestParser()
        u_u_p.add_argument("category_name")
        args = u_u_p.parse_args()
        c_name = args.get("category_name", None)
        if c_name is None:
            return json.dumps({"message":"Category name is required"}), 400
        try:
            n_cat = Category.query.filter_by(category_id=category_id).first()
        except:
            return json.dumps({"message":" An internal server error occurred."}), 500
        if n_cat is None:
            return 404
        n_cat.category_name = c_name
        db.session.commit()
        return {"category_id": category_id, "category_name": c_name}, 200

    def post(self):
        c_u_p = reqparse.RequestParser()
        c_u_p.add_argument("category_name")

        args = c_u_p.parse_args()
        c_name = args.get("category_name", None)
        if len(c_name) ==0:
            return json.dumps({"message":"Category name is required"}), 400
        try:
            n_cat = Category.query.filter_by(category_name=c_name).first()
        except:
            return json.dumps({"message":" An internal server error occurred."}), 500
        if n_cat is not None:
            return 409
        db.session.add(a := Category(category_name=c_name))
        db.session.commit()
        return {"category_id": a.category_id, "category_name": a.category_name}, 200

    def delete(self, category_id):
        try:
            n_cat = Category.query.filter_by(category_id=category_id).first()
            if n_cat is None:
                return 404
            db.session.delete(n_cat)
            db.session.commit()
        except:
            return json.dumps({"message":" An internal server error occurred."}), 500
        return "", 200


class UserAPI_pro(Resource):
    def get(self):
        try:
            json_data = []
            pro = Product.query.all()
            for row in pro:
                json_data.append({"product_id": row.product_id, "product_name": row.product_name, "brand": row.brand,
                                  "man_date": row.man_date, "exp_date": row.exp_date, "rate": row.rate,
                                  "stock": row.stock, "category_id": row.category_id, "quantity": row.quantity,
                                  "rating": row.rating})
            return json_data, 200
        except:
            return json.dumps({"message":" An internal server error occurred."}), 500


class UserAPI1_pro(Resource):
    def get(self, category_id):
        try:
            json_data = []
            pro = Product.query.filter_by(category_id=category_id).all()
            for row in pro:
                json_data.append({"product_id": row.product_id, "product_name": row.product_name, "brand": row.brand,
                                  "man_date": row.man_date, "exp_date": row.exp_date, "rate": row.rate,
                                  "stock": row.stock, "category_id": row.category_id, "quantity": row.quantity,
                                  "rating": row.rating})
            return json_data, 200
        except:
            return json.dumps({"message":" An internal server error occurred."}), 500


class UserAPI1(Resource):
    def get(self, product_name):
        try:
            n_cat = Product.query.filter(Product.product_name.like(f'%{product_name}%')).all()
        except:
            return json.dumps({"message":" An internal server error occurred."}), 500
        a = []
        for i in n_cat:
            a.append({"product_id": i.product_id, "product_name": i.product_name, "brand": i.brand,
                      "man_date": i.man_date, "exp_date": i.exp_date, "rate": i.rate,
                      "stock": i.stock, "category_id": i.category_id, "quantity": i.quantity,
                      "rating": i.rating})
        return a, 200

    def post(self):
        c_u_p = reqparse.RequestParser()
        c_u_p.add_argument("product_name")
        c_u_p.add_argument("brand")
        c_u_p.add_argument("man_date")
        c_u_p.add_argument("exp_date")
        c_u_p.add_argument("rate")
        c_u_p.add_argument("stock")
        c_u_p.add_argument("category_id")
        c_u_p.add_argument("quantity")
        c_u_p.add_argument("rating")


        args = c_u_p.parse_args()
        p_name = args.get("product_name",None)
        p_brand = args.get("brand", None)
        p_man_date = args.get("man_date", None)
        p_exp_date = args.get("exp_date", None)
        p_rate = args.get("rate", None)
        p_stock = args.get("stock", None)
        p_category_id = args.get("category_id", None)
        p_quantity = args.get("quantity", None)
        p_rating = args.get("rating", None)

        if len(p_name) ==0:
            return json.dumps({"message":"Product name is required"}), 400
        try:
            n_cat = Product.query.filter_by(product_name=p_name).first()
        except:
            return json.dumps({"message":" An internal server error occurred."}), 500
        db.session.add(a := Product(product_name=p_name, brand=p_brand,
                                    man_date=p_man_date, exp_date=p_exp_date, rate=p_rate,
                                    stock=p_stock, category_id=p_category_id, quantity=p_quantity,
                                    rating=p_rating))
        db.session.commit()
        return {"product_id": a.product_id, "product_name": a.product_name, "brand": a.brand,
                "man_date": a.man_date, "exp_date": a.exp_date, "rate": a.rate, "stock": a.stock,
                "category_id": a.category_id, "quantity": a.quantity,"rating": a.rating}

    def put(self, product_id):
        c_u_p = reqparse.RequestParser()
        c_u_p.add_argument("product_id")
        c_u_p.add_argument("product_name")
        c_u_p.add_argument("brand")
        c_u_p.add_argument("man_date")
        c_u_p.add_argument("exp_date")
        c_u_p.add_argument("rate")
        c_u_p.add_argument("stock")
        c_u_p.add_argument("category_id")
        c_u_p.add_argument("quantity")
        c_u_p.add_argument("rating")

        args = c_u_p.parse_args()
        p_name = args.get("product_name", None)
        p_brand = args.get("brand", None)
        p_man_date = args.get("man_date", None)
        p_exp_date = args.get("exp_date", None)
        p_rate = args.get("rate", None)
        p_stock = args.get("stock", None)
        p_category_id = args.get("category_id", None)
        p_quantity = args.get("quantity", None)
        p_rating = args.get("rating", None)

        if len(p_name)==0:
            return json.dumps({"message":"Product name is required"}), 400
        try:
            n_cat = Product.query.filter_by(product_id=product_id).first()
        except:
            return json.dumps({"message":" An internal server error occurred."}), 500
        if n_cat is None:
            return 404
        n_cat.product_name = p_name
        n_cat.brand = p_brand
        n_cat.man_date = p_man_date
        n_cat.exp_date = p_exp_date
        n_cat.rate = p_rate
        n_cat.stock = p_stock
        n_cat.category_id = p_category_id
        n_cat.quantity = p_quantity
        n_cat.rating = p_rating

        db.session.commit()
        return {"product_id": n_cat.product_id, "product_name": n_cat.product_name, "brand": n_cat.brand,
                "man_date": n_cat.man_date, "exp_date": n_cat.exp_date, "rate": n_cat.rate,
                "stock": n_cat.stock, "category_id": n_cat.category_id, "quantity": n_cat.quantity,
                "rating": n_cat.rating}

    def delete(self, product_id):
        try:
            n_cat = Product.query.filter_by(product_id=product_id).first()
            if n_cat is None:
                return 404
            db.session.delete(n_cat)
            db.session.commit()
        except:
            return json.dumps({"message":" An internal server error occurred."}), 500
        return "", 200
