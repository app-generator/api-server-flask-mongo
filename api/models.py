# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash
from flask_mongoengine import MongoEngine

db = MongoEngine() 

class Users(db.Document):
    username = db.StringField(max_length=32, required=True)
    email = db.StringField(required=True)
    password = db.StringField()
    jwt_auth_active = db.BooleanField()
    date_joined = db.DateTimeField(default=datetime.utcnow)

    def __repr__(self):
        return f"User {self.username}"

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def update_email(self, new_email):
        self.email = new_email

    def update_username(self, new_username):
        self.username = new_username

    def check_jwt_auth_active(self):
        return self.jwt_auth_active

    def set_jwt_auth_active(self, set_status):
        self.jwt_auth_active = set_status

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)

    @classmethod
    def get_by_email(cls, email):
        return cls.objects(email=email).first()

    def toDICT(self):

        cls_dict = {}
        cls_dict['_id'] = str(self.id)
        cls_dict['username'] = self.username
        cls_dict['email'] = self.email

        return cls_dict

    def toJSON(self):

        return self.toDICT()


class JWTTokenBlocklist(db.Document):
    jwt_token = db.StringField(required=True)
    created_at = db.DateTimeField(required=True)

    def __repr__(self):
        return f"Expired Token: {self.jwt_token}"

    @classmethod
    def get_by_jwt_token(cls, jwt_token):
        return cls.objects(jwt_token=jwt_token).first()
