# -*- coding: utf-8 -*-
from bottle import route, run, request, redirect, post, get, template, static_file, error
import requests
import json
from sys import argv
import os
mykey=os.environ["KEY"]

@get('/')
def index():
	return template('Index.tpl')

@post('/Ficha')
def event():
  name = request.forms.get('name')
  payloadCode={"locale":request.forms.get('Language'),'api_key':mykey,'dataByld':'true','champListData':'info'}
  code=requests.get('https://euw1.api.riotgames.com/lol/static-data/v3/champions',params=payloadCode)
  cod = code.json()
  for c in cod['data']:
    if cod['data'][c]['name'] == name.title():
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
  name1 = request.forms.get('name1')
  payloadCode1={"locale":request.forms.get('Language'),'api_key':mykey,'dataByld':'true','champListData':'info'}
  code1=requests.get('https://euw1.api.riotgames.com/lol/static-data/v3/champions',params=payloadCode1)
  cod1 = code1.json()
  for c in cod1['data']:
    if cod1['data'][c]['name'] == name1.title():
      ID1 = str(cod1['data'][c]['id'])

  payload = {"locale":request.forms.get('Language'),"champData":'stats','api_key':mykey}
  URL1 = 'https://euw1.api.riotgames.com/lol/static-data/v3/champions/'+ID1
  r1=requests.get(URL1,params=payload)
  if r1.status_code == 200:
    doc1 = r1.json()
    stats1 = doc1['stats']

  name2 = request.forms.get('name2')
  payloadCode2={"locale":request.forms.get('Language'),'api_key':mykey,'dataByld':'true','champListData':'info'}
  code2=requests.get('https://euw1.api.riotgames.com/lol/static-data/v3/champions',params=payloadCode2)
  cod2 = code2.json()
  for c in cod2['data']:
    if cod2['data'][c]['name'] == name2.title():
      ID2 = str(cod2['data'][c]['id'])

  URL2 = 'https://euw1.api.riotgames.com/lol/static-data/v3/champions/'+ID2
  r2=requests.get(URL2,params=payload)
  if r2.status_code == 200:
    doc2 = r2.json()
    stats2 = doc2['stats']
    return template('Comparator2.tpl',Info1=stats1,campeon1=doc1['name'],Info2=stats2,campeon2=doc2['name'])

@get("/Objects")
def obj():
	return template('Objects.tpl')

@post('/Object')
def event():
	ID3 = "1001"
	name3 = request.forms.get('name3')
	payload3={'itemListData':'stats','locale':request.forms.get('Language'),'api_key':mykey}
	r3=requests.get('https://euw1.api.riotgames.com/lol/static-data/v3/items',params=payload3)
	doc3 = r3.json()
	for o in doc3:
		if doc3['data']["3715"]['name'] == name3.title():
			ID3 = "3715"

  payload4={"locale":request.forms.get('Language'),'api_key':mykey,'itemData':'all'}
  URL4 = 'https://euw1.api.riotgames.com/lol/static-data/v3/items/'+ID3
  r4=requests.get(URL4,params=payload4)
  if r4.status_code == 200:
     doc4 = r4.json()
     return template('Object.tpl',stats=doc4)

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

@error(404)
def error404(error):
    return 'Data not found'

run(host='0.0.0.0', port=argv[1])
