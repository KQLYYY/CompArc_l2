import json
import re
import pymongo
from pymongo import MongoClient
import os
client = MongoClient('localhost', 27017)

os.remove('crypt_btc.json')
os.remove('crypt_eth.json')
os.remove('crypt_eos.json')
os.remove('crypt_ltc.json')
os.remove('crypt_rpl.json')

os.system('scrapy crawl crypt_btc -o crypt_btc.json')
os.system('scrapy crawl crypt_eth -o crypt_eth.json')
os.system('scrapy crawl crypt_eos -o crypt_eos.json')
os.system('scrapy crawl crypt_ltc -o crypt_ltc.json')
os.system('scrapy crawl crypt_rpl -o crypt_rpl.json')

myfile1 = open('crypt_btc.json',mode='r')
json_data_btc = json.load(myfile1)

myfile2 = open('crypt_eth.json',mode='r')
json_data_eth = json.load(myfile2)

myfile3 = open('crypt_eos.json',mode='r')
json_data_eos = json.load(myfile3)

myfile4 = open('crypt_ltc.json',mode='r')
json_data_ltc = json.load(myfile4)

myfile5 = open('crypt_rpl.json',mode='r')
json_data_rpl = json.load(myfile5)

c = pymongo.MongoClient()
db = client['mydb']

db.btc.drop()
result = db.btc.insert_many(json_data_btc)
result.inserted_ids

db.eth.drop()
result = db.eth.insert_many(json_data_eth)
result.inserted_ids

db.eos.drop()
result = db.eos.insert_many(json_data_eos)
result.inserted_ids

db.ltc.drop()
result = db.ltc.insert_many(json_data_ltc)
result.inserted_ids

db.rpl.drop()
result = db.rpl.insert_many(json_data_rpl)
result.inserted_ids
