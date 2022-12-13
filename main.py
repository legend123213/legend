from mongoengine import *


class User(Document):
    username = StringField(required=True, unique=True)
    password = BinaryField(required=True)
    roll = BooleanField(required=True)


class Member(Document):
    username = StringField(required=True, unique=True)
    name = StringField()
    roll = BooleanField(required=True)
    img = ImageField()
    email = EmailField()
    contact = StringField()
    year = StringField()
    sex =StringField()
    club =StringField()
    group = StringField()
    dept = StringField()

class waiting(Document):
    username = StringField(required=True, unique=True)
    name = StringField()
    roll = BooleanField(required=True)
    img = ImageField()
    contact = StringField()
    year = IntField()
    group = StringField()
    dept = StringField()


class Ability(Document):
    username = StringField(required= True)
    language = ListField()
    working = StringField()
class Rating(Document):
    username = StringField(required=True, unique=True)
    rate = StringField()
class Notifcation(Document):
    username = StringField(required=True, unique=True)
    message = StringField()
    acceptance = IntField(-1,1)