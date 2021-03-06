# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 15:24:53 2018

@author: zouco
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)




@app.route('/')
def the_main_page():
    return render_template('3.html')

@app.route('/about')
def func_a():
    return render_template('3_about.html')

@app.route('/members')
def func_m():
    return render_template('3_members.html', members=members)

@app.route('/tasks')
def func_t():
    return render_template('3_tasks.html')

if __name__=='__main__':
    members = ['Apollo','Adam','Cauchy']
    app.run(debug=False)  # to stop the script, change this to false
    # go to http://localhost:5000 to see result