# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 15:21:29 2018

@author: zouco
"""


from flask import Flask

app = Flask(__name__)

@app.route('/')
def the_main_page():
    return 'Hello web world!'

if __name__=='__main__':
    app.run(debug=False)  # to stop the script, change this to false
    # go to http://localhost:5000 to see result