import base64
import json
import bcrypt as bcrypt

from main import *
from mongoengine import connect






def create_user(username, password, roll):
    use = User()
    hashandsalt = bcrypt.hashpw(password.encode(),bcrypt.gensalt())
    use.username = username
    use.password = hashandsalt
    use.roll = roll
    use.save()


def set_profile(username):
    for a in Member.objects(username = username):
        with open("sample.json", "w") as outfile:
            json.dump(a.to_json(), outfile)
        return a.to_json()

def gett():
    with open('sample.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
        user_profile_dic = json.loads(json_object)
    return user_profile_dic


def create_member(username, name, roll, img, contact,year,group,dept,email,sex,club):
    member = Member()
    member.username = username
    member.name = name
    member.roll = roll
    member.img = img
    member.contact = contact
    member.year = year
    member.sex =sex
    member.club = club
    member.email = email
    member.group =group
    member.dept = dept
    member.save()


def get_ability(username, language, working):
    ability = Ability()
    ability.username = username
    ability.language = language
    ability.working = working
    ability.save()
def get_score(username,rate):
    score = Rating()
    score.username = username
    score.rate = rate
    score.save()
def imgg(username):
    img_person = Member.objects(username = username).first()
    y = img_person.img.read()
    o = open("/home/legend/PycharmProjects/Icpc/profile pics/"+username + ".jpg", "wb")
    o.write(y)
    o.close()
    return username+".jpg"
def show_abi(username):
    abi = Ability.objects(username=username).first()

    return abi.working

def get_lang(username):
    abi = Ability.objects(username=username).first()
    return abi.language

def show_rate(username):
    ab = Rating.objects(username=username).first()
    return ab.rate

def notif(username,message):
    notifc = Notifcation()
    notifc.username = username
    notifc.message = message
    notifc.acceptance = 0
    notifc.save()
def wait_member(username, name, roll, img, contact,year,group,dept,email,sex,club):
    member = wait_member()
    member.username = username
    member.name = name
    member.roll = roll
    member.img = img
    member.contact = contact
    member.year = year
    member.group =group
    member.dept = dept
    member.sex = sex
    member.club = club
    member.email = email
    member.save()
def approve_waiting(username):
    if wait_member.objects(username=username).first() != None:
        member = wait_member.objects(username=username).first()
        create_member(member.username,member.name,member.roll,member.img,member.contact,member.year,member.group,member.dept,member.email,member.sex,member.club)
    else:
        return None







def qur_notif(username):
    notif = Notifcation.objects(username = username).first()
    return notif
def del_member(username):
    nam = quary_user(username)
    nam.delete()
def del_w_member(username):
    nam = quary_user(username)
    nam.delete()
def test(username,password,roll):
    Test = True
    if User.objects(username=username).first() != None:
        stu = User.objects(username=username).first()
        if bcrypt.checkpw(password.encode(),stu.password) and roll == True:
            Test = True
        elif bcrypt.checkpw(password.encode(),stu.password):
            Test = True
        else:
            Test = False
    else:
        Test = False
    return Test
def log_in_user(username):
    user = User.objects(username = username).first()
    return user

def quary_user(username):
    member = Member.objects(username=username).first()
    return member
def quary_ability(username):
    abi = Ability.objects(username=username).first()
    return abi.working
def quary_rate(username):
    rat = Rating.objects(username=username).first()
    return rat
def listi():
    d=[]
    icpc = []
    l = Member.objects()

    for i in range(len(l)):
        if l[i].club == 'ICPC':
            d.append(str(i))
            d.append(l[i].username)
            namee = l[i].username
            d.append(quary_user(namee).year)
            d.append(quary_user(namee).dept)
            d.append(Rating.objects(username=namee).first().rate)
            d.append(Ability.objects(username=namee).first().working)
            icpc.append(d)
        d=[]

    return icpc
def add_lang(username,lis):
    abi = Ability.objects(username=username).first()
    la = list(abi.language)
    for i in lis:
        if i not in la:
            la.append(i)

    abi.update(language=la)
    return abi.language


def listd():
    d = []
    div= []
    l = Member.objects()

    for i in range(len(l)):
        if l[i].club != 'ICPC':
            d.append(str(i))
            d.append(l[i].username)
            namee = l[i].username
            d.append(quary_user(namee).year)
            d.append(quary_user(namee).dept)
            d.append(Rating.objects(username=namee).first().rate)
            d.append(Ability.objects(username=namee).first().working)
            div.append(d)
        d = []

    return div
def rat():
    for Rate in Rating.objects(rate=10):
        return Rate.username




dbname = "ICPC"
password = "78900987"
ho="mongodb+srv://Legend:{}@pycluster.ajv4lb8.mongodb.net/{}?retryWrites=true&w=majority".format(password,dbname)

connect(host=ho)
