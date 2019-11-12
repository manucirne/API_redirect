#!flask/bin/python
from flask import Flask, redirect, url_for,request, jsonify
from flask_restful import Api
import requests
import os

app = Flask(__name__)
api = Api(app)

ip_saida = os.environ["IP_REDIRECT"]
print(ip_saida)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path, methods = ['GET', 'POST', 'PUT', 'DELETE']):
    print("entrou na função")
    if request.method == 'POST':
        req = requests.post(ip_saida + '/' + path, data = request.get_json())
        return req.content
    elif request.method == 'PUT':
        req = requests.put(ip_saida + '/' + path, data = request.get_json())
        return req.content
    elif request.method == 'DELETE':
        req = requests.delete(ip_saida + '/' + path)
        return req.content
    elif request.method == 'GET':
        print("entrou no GET")
        req = requests.get(ip_saida + '/' + path)
        return req.content

@app.route('/healthcheck')
def hc():
    return '',200


if __name__ == '__main__':
    app.run('0.0.0.0',port=8090)