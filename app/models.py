from app import db
import string

class Message(db.Model):
    __tablename__="message"
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String,nullable=False)
    message=db.Column(db.String,nullable=False)

    def addMessage(username,message):
            newMessage=Message(username=username,message=message)
            db.session.add(newMessage)
            db.session.commit()
