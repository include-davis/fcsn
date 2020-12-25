# Creates classes for databases where their attributes are stored

from website import db

# Volunteer class for eligible emails for event registration
class Volunteer(db.Model):
    __bind_key__ = 'valid emails'
    email = db.Column(db.String(100), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return 'valid email: ' + self.email   

# Class for storing all emails entered
class Entry(db.Model):
    email = db.Column(db.String(100), nullable=False, primary_key=True)

    def __repr__(self):
        return 'entered email: ' + self.email