#fileName : engine.py
#author : Aishwarya Pagalla
# last modified : 11/28/2018

from flask import Flask
from flask_cors import CORS
import os
import json
from sys_met import *
import markdown
app = Flask(__name__)
CORS(app)

@app.route("/processes")
def Proc():
    return json.dumps(sys_met.met,indent = 4)

@app.route("/info")
def Info():
    return json.dumps(sys_met.inf,indent = 4)	
	
@app.route("/usage")
def Usgae():
    return json.dumps(sys_met.sett,indent = 4)
    
	
if __name__ == '__main__':
    app.run(debug = True)