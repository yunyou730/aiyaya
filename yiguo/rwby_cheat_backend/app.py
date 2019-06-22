from flask import Flask
from flask import session
from flask import url_for
from flask import escape
from flask import request
from flask import redirect

app = Flask(__name__);
app.secret_key = b"miaoyunyou";
# print("app:{}".format(__name__));

counter = 0;

@app.route("/")
def index():
	if "username" in session:
		return "Logged in as %s" % escape(session['username']);
	return "You are not logged in"


@app.route("/login",methods = ["GET","POST"])
def login():
	if request.method == "POST":
		session["username"] = request.form["username"]
		return redirect(url_for("index"))
	return '''
		<form method = "post">
			<p><input type = "text" name = "username"></input>
			<p><input type = "submit" name = "login"></input>
		</form>
	'''


@app.route("/logout")
def logout():
	session.pop("username",None);
	return redirect(url_for("index"));


@app.route("/session_view")
def session_view():
	global counter
	counter = counter + 1;
	ret = "[session view]"
	for key,value in session.items():
		ret = ret + "[" + key + "]->" + value + ";"
	ret = ret + "|counter:" + str(counter);
	return ret;

@app.route("/session_put/<key>/<value>")
def session_put(key,value):
	session[key] = value;
	return "key:" + key + ",value:" + value

@app.route("/session_remove/<key>")
def session_remove(key):
	session.pop(key,None);
	return session_view();
