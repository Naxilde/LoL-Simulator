# -*- coding: utf-8 -*-
from bottle import route, run, request, redirect, post, get, template, static_file
import requests
import json
from sys import argv

@get('/')
def index():
	return template('Index.tpl')

@post('/Ficha')
def event():
  mykey=KEY
  payloadCode={"locale":request.forms.get('Language'),'api_key':mykey,'dataByld':'true','champListData':'info'}
  code=requests.get('https://euw1.api.riotgames.com/lol/static-data/v3/champions',params=payloadCode)
  cod = code.json()
  for c in cod['data']:
    if cod['data'][c]['name'] == request.forms.get('name'):
      ID = str(cod['data'][c]['id'])

  payload = {"locale":request.forms.get('Language'),"champData":'stats','api_key':mykey}
  URL = 'https://euw1.api.riotgames.com/lol/static-data/v3/champions/'+ID
  r=requests.get(URL,params=payload)
  if r.status_code == 200:
    doc = r.json()
    stats = doc['stats']
    return template('Champion.tpl',Info=stats,campeon=doc['name'],mote=doc['title'])

@get('/Comparator')
def com():
	return template('Comparator.tpl')

@post('/Ficha2')
def event():
  payloadCode1={"locale":request.forms.get('Language'),'api_key':mykey,'dataByld':'true','champListData':'info'}
  code1=requests.get('https://euw1.api.riotgames.com/lol/static-data/v3/champions',params=payloadCode1)
  cod1 = code1.json()
  for c in cod1['data']:
    if cod1['data'][c]['name'] == request.forms.get('name1'):
      ID1 = str(cod1['data'][c]['id'])

  payload = {"locale":request.forms.get('Language'),"champData":'stats','api_key':mykey}
  URL1 = 'https://euw1.api.riotgames.com/lol/static-data/v3/champions/'+ID1
  r1=requests.get(URL1,params=payload)
  if r1.status_code == 200:
    doc1 = r1.json()
    stats1 = doc1['stats']

  payloadCode2={"locale":request.forms.get('Language'),'api_key':mykey,'dataByld':'true','champListData':'info'}
  code2=requests.get('https://euw1.api.riotgames.com/lol/static-data/v3/champions',params=payloadCode2)
  cod2 = code2.json()
  for c in cod2['data']:
    if cod2['data'][c]['name'] == request.forms.get('name2'):
      ID2 = str(cod2['data'][c]['id'])

  URL2 = 'https://euw1.api.riotgames.com/lol/static-data/v3/champions/'+ID2
  r2=requests.get(URL2,params=payload)
  if r2.status_code == 200:
    doc2 = r2.json()
    stats2 = doc2['stats']
    return template('Comparator2.tpl',Info1=stats1,campeon1=doc1['name'],Info2=stats2,campeon2=doc2['name'])

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')


run(host='0.0.0.0', port='argv[1]', debug=True)
