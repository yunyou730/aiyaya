from flask import Flask
from flask import request
from flask import render_template
import json
import time

app = Flask(__name__);

@app.route("/rwby")
def rwby():
	return "rwby"

def valid_login(username,password):
	return True;

def log_the_user_in(username):
	return render_template("hello.html",name = username)

@app.route("/login",methods = ["POST","GET"])
def login():
	error = None;
	if request.method == "POST":
		if valid_login(request.form["username"],request.form["password"]):
			return log_the_user_in(request.form["username"]);
		else:
			error = "Invalid username/password"
	return "user name err!";

@app.route("/")
def index():
	return render_template("index.html");

@app.route("/test")
def testJS():
	return render_template("test.js");


@app.route("/getCheatUsers/<callback>")
def getCheatUsers(callback):
	time.sleep(3);
	users = ["123","345"];
	param = json.dumps(users);
	print("callback" + callback);
	print("param" + param);
	return callback + "(" + param + ")"


'''
from flask import Flask,url_for
from flask import render_template
app = Flask(__name__);

@app.route("/")
def index():
	return "index page"

@app.route("/hello")
def hello():
	return "hello"


@app.route("/user/<username>")
def show_user_profile(username):
	return "User %s" % username


@app.route("/post/<int:post_id>")
def show_post(post_id):
	return "Post %d" % post_id;

@app.route("/path/<path:sub_path>")
def show_path(sub_path):
	return "sub path %s" % sub_path

@app.route("/rwbyconfig/<name>")
def rwby_index(name = None):
	return render_template("hello.html",name=name);

with app.test_request_context():
	print(url_for("index"));
	print(url_for("hello"));
	print(url_for("show_post",post_id = "730"));
	print(url_for("show_path",sub_path = "/aiyaya"));

'''
