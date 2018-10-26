# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 21:11:43 2018

@author: zouco
"""

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("4_input.html") # this should be the name of your html file

@app.route('/', methods=['POST'])
def my_form_post():
    text1 = request.form['text1']
    text2 = request.form['text2']
    if text1 == text2 :
        return "<h1>Plagiarism Detected !</h1>"
    else :
        return "<h1>No Plagiarism Detected !</h1>"


@app.route('/input')
def show_input():
    print(request.args['name'])


if __name__ == '__main__':
    app.run(port=80)