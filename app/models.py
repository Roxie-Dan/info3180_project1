from . import db

class UserProfile(db.Model):
    id= db.Column(db.String(8), primary_key=True)
    username = db.Column(db.String(80))
    profile_created_on = db.Column(db.DateTime)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    image = db.Column(db.String(80))
    age = db.Column(db.Integer)
    bio = db.Column(db.String(500))
    gender = db.Column(db.String(80))

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False
    def set_id(self,userid):
        self.userid = userid

    def get_id(self):
        try:
            return unicode(self.userid)  # python 2 support
        except NameError:
            return str(self.userid)  # python 3 support
    def __init__(self,userid,username,profile_created_on,first_name,last_name,image,age,bio,gender):
        self.id = userid 
        self.username = username
        self.profile_created_on = profile_created_on
        self. first_name = first_name
        self.last_name = last_name
        self.image = image
        self.age = age
        self.bio = bio
        self.gender = gender

    def __repr__(self):
        return '<User %r>' % (self.username)
