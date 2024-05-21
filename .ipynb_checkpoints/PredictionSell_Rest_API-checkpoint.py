#!/usr/bin/env python
#creando una aplicacion Rest API

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, jsonify, request
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

app=Flask(__name__)
@app.route("/")    
def prediccion():
    path='E:/Study/Data Science/Ocula/'
    fileName = 'ventas20190101-20231231.xlsx'
    path = path+fileName
    prediction2023 = 2023
    df = pd.read_excel(path, sheet_name='SummarySells')
    specificRow=df.iloc[0]
    value=np.array([2019,2020,2021,2022])
    TotalSelling=np.array(specificRow)    
    coef = np.polyfit(value,TotalSelling,2)
    p = np.polyval(coef,prediction2023)        
    x1=np.linspace(2019, prediction2023 + 1, 6)    
    y1=fx(x1,coef)    
    #Json_data = '"{x1}"'
    Json_data ="x1: " + str(x1) + "-y1:" + str(y1) + "-Prediction:" + str(prediction2023) + "-value:" + str(value) + "-TotalSelling:" + str(TotalSelling) 
    #json_string = '{"Name": "John", "Age": 30, "City": "New York"}'
    #json.loads(Json_data)
    return(Json_data)
    
def fx(x1,coef):
    fx=0
    n=len(coef)-1
    for p in coef:        
        fx=fx+p*x1**n        
        n=n-1        
    return fx
        
if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8080,debug=True)
    #app.run(debug=True)
    