from flask import Flask,render_template,send_file,request,redirect,url_for
import json
from  urllib.parse import unquote
import requests
app=Flask(__name__)

@app.route('/brain',methods=['GET'])
def 536():
  pass

@app.route('/brain',methods=['GET'])
def brain():
  pass



@app.errorhandler(404)
def E_404(x):
    return render_template('404/404.html')

        
