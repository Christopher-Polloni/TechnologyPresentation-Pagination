import sys
from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from config import Config
from app.models import *
from app import app, db


#index route
@app.route('/')
@app.route("/index", methods=["GET","POST"])
def index():
    messages = Message.query.all()
    page = request.args.get('page', 1, type=int)
    messages = Message.query.order_by(Message.id.desc()).paginate(page, app.config['MESSAGES_PER_PAGE'], False)
    if request.method =="POST":
        username = request.form.get("username")
        message = request.form.get("message")
        Message.addMessage(username=username, message=message)
        return redirect(url_for('index'))
    return render_template("index.html", messages=messages)

#specific user posts route
@app.route("/index/<string:username>")
def user_posts(username):
    messages = Message.query.all()
    page = request.args.get('page', 1, type=int)
    per_page=2
    messages = Message.query.filter_by(username=username).order_by(Message.id.desc()).paginate(page, per_page, False)
    return render_template("user_posts.html", messages=messages, username=username)
