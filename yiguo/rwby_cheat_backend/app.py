from flask import Flask
from flask import session
from flask import url_for
from flask import escape
from flask import request
from flask import redirect
from flask import render_template
import json
import urllib.parse

app = Flask(__name__);
app.config["SECRET_KEY"] = b"aiyaya730"

state = {"enable_key":"bukai"}	
state["rids"] = {}

users = {
	"rwbydev":"mmo2018001"
}

CONST_ENABLE_KEY = "yzj_said_dakai_tiaoshi!!"

@app.route("/getList/<callback>")
def getList(callback):
	if not checkLogin():
		ret = {"not_login":True}
		retStr = json.dumps(ret);
		return callback + "(" + retStr + ")"
	return getUserListCallbackStr(callback)

@app.route("/add/<uid>/<callback>")
def add(uid,callback):
	if not checkLogin():
		ret = {"not_login":True}
		retStr = json.dumps(ret)
		return callback + "(" + retStr + ")"	
	state["rids"][uid] = True;
	return getUserListCallbackStr(callback)

@app.route("/rem/<uid>/<callback>")
def rem(uid,callback):
	if not checkLogin():
		ret = {"not_login":True}
		retStr = json.dumps(ret);
		return callback + "(" + retStr + ")"	

	if uid in state["rids"]:
		del state["rids"][uid]
	return getUserListCallbackStr(callback)	

@app.route("/toggle/<callback>")
def toggle(callback):
	if not checkLogin():
		ret = {"not_login":True}
		retStr = json.dumps(ret);
		return callback + "(" + retStr + ")"	
	if state["enable_key"] == CONST_ENABLE_KEY
		state["enable_key"] = "bukai";
	else:
		state["enable_key"] = CONST_ENABLE_KEY
	return isEnable(callback);

@app.route("/checkEnable/<callback>")
def isEnable(callback):
	if not checkLogin():
		ret = {"not_login":True}
		retStr = json.dumps(ret);
		return callback + "(" + retStr + ")"
	if state["enable_key"] == CONST_ENABLE_KEY:
		return callback + "(\"""enable" + "\")";
	return callback + "(\"""disable" + "\")";

@app.route("/rwby/<callback>")
def rwbyState(callback):
	# if not checkLogin():
	# 	ret = {"not_login":True}
	# 	retStr = json.dumps(ret);
	# 	return callback + "(" + retStr + ")"
	resultStr = json.dumps(state);
	return resultStr

def getUserListCallbackStr(callback):
	if not checkLogin():
		ret = {"not_login":True}
		retStr = json.dumps(ret);
		return callback + "(" + retStr + ")"		
	userList = state["rids"];
	resultStr = json.dumps(userList);
	return callback + "(" + resultStr + ")";

@app.route("/login",methods = ["POST"])
def login():
	print("login----");
	username = request.form.get("uname");
	password = request.form.get("pwd");
	domain = request.form.get("dmain");
	print("domain:" + domain);
	if username in users:
		if users[username] == password:
			# return "login success"
			# url = urllib.parse.quote("d:/miao/aiyaya/yiguo/rwby_cheat_frontend/index.html")
			# url = urllib.parse.quote(domain)
			url = domain
			print("after encode url:" + url);
			session["username"] = username;
			return render_template("login_success.html",url=url)
	if session.get("username") != None:
		session.pop("username");
	return "wrong username password"

@app.route("/logout/<callback>")
def logout(callback):
	if session.get("username") != None:
		session.pop("username")
	return callback + "(\"logout success\")";

def checkLogin():
	if session.get("username") == None:
		return False;
	return True;

@app.route("/login")
def showLogin():
	return "";

@app.route("/showControlpanel")	
def showControlpanel():
	return "";
