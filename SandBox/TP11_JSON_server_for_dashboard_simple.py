# -*- coding: utf-8 -*-
"""
Exemple d'utilisation d'un serveur Flask pour fournir des données au format
JSON pour l'application CFPT_FreeBoard

Install Flask dans la console:
pip3 install flask_cors

Si besoin:
pip3 install flask
pip3 install numpy


@author: MONNEYF_CFPT
"""
#from __future__ import print_function
#import sys

import numpy as np
from flask import Flask,request
from flask import jsonify
from flask_cors import CORS

import time



app = Flask(__name__)
CORS(app)


dataDict ={
        'val0' : 0,
        'tab0' : [0,1,2,3,4],
        'tab1' : [5,6,7,8,9,10],
        'name' : "Test VotreNom",
        'SM1'  : 0}

data = {
        'sinus10s' : 10,
        'sinus30s' : 30,
        'sinus60s' : 60,
        'text'     : "RPI VotreNom",
        'requestNb': 0}



@app.route('/DemoData/', methods=['GET'])
def CreateData():
   for value in request.args:
        #print(value, file=sys.stderr)
        global dataDict
        dataDict[value] = request.args.get(value)
        print(dataDict)
   return jsonify(dataDict)


@app.route('/', methods=['GET'])
def SendDataValue():
    sinus10s = np.round(180*np.sin((time.time()%10)/10.0*2*np.pi),2)
    sinus30s = np.round(180*np.sin((time.time()%30)/30.0*2*np.pi),2)
    sinus60s = np.round(180*np.sin((time.time()%60)/60.0*2*np.pi),2)   
    #print locals()
    data["sinus10s"] = sinus10s
    data["sinus30s"] = sinus30s
    data["sinus60s"] = sinus60s
    data["requestNb"] = data["requestNb"]+1
    print(data)
    return jsonify(data)


if __name__ == '__main__':
    
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--IPadd", type=str,default='0.0.0.0',
                        help="definir IP address (default:localhost)")                      
    args = parser.parse_args()
    
    #app.run(host='192.168.43.69',debug=True,threaded=True)
    #app.run(host='localhost'    ,debug=True,threaded=True)
    app.run(host=args.IPadd,debug=True,threaded=True, use_reloader=False)