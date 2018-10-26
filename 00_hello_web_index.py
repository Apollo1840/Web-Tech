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
    return render_template('index_1.html')



if __name__=='__main__':
    app.run(debug=False)  # to stop the script, change this to false
    # go to http://localhost:5000 to see result