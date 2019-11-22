#!flask/bin/python
from flask import Flask, redirect, url_for,request, jsonify
from flask_restful import Api
import requests
import os

app = Flask(__name__)
api = Api(app)

ip_saida = os.environ["IP_REDIRECT"]
print(ip_saida)

@app.route('/', defaults={'path': ''},methods = ['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/<path:path>',methods = ['GET', 'POST', 'PUT', 'DELETE'])
def catch_all(path):
    if request.method == 'POST':
        req = requests.post('http://' + ip_saida + ':8080' + '/' + path,  headers=request.header,  json=request.get_json())
        return req.content
    elif request.method == 'PUT':
        req = requests.put('http://' + ip_saida + ':8080' + '/' + path, headers=request.header,  json=request.get_json())
        return req.content
    elif request.method == 'DELETE':
        req = requests.delete('http://' + ip_saida + ':8080' + '/' + path)
        return req.content
    elif request.method == 'GET':
        print("entrou no GET")
        req = requests.get('http://' + ip_saida + ':8080' + '/' + path)
        return req.content

@app.route('/healthcheck')
def hc():
    return '<3',200


if __name__ == '__main__':
    app.run('0.0.0.0',port=8080)