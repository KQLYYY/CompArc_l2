from flask import Flask, render_template
from data import Articles
from pymongo import MongoClient
import pprint
import operator
client = MongoClient()

app = Flask(__name__)

db = client.mydb
btc = db.btc
eth = db.eth
eos = db.eos
ltc = db.ltc
rpl = db.rpl

Themes=[]

bt=btc.find_one()
bt=str(bt['topic'])
Themes.append(bt[2:-4])

et=eth.find_one()
et=str(et['topic'])
Themes.append(et[2:-4])

eo=eos.find_one()
eo=str(eo['topic'])
Themes.append(eo[2:-4])

lt=ltc.find_one()
lt=str(lt['topic'])
Themes.append(lt[2:-4])

rp=rpl.find_one()
rp=str(rp['topic'])
Themes.append(rp[2:-4])


print(Themes)


@app.route('/')
def index():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/themes')
def themes():
	return render_template('themes.html',Themes= Themes)

@app.route('/theme/<path:id>')
def article(id):
	if id == 'Bitcoin':
		id_col=btc
	elif id == 'Ethereum':
		id_col=eth
	elif id == 'EOS':
		id_col=eos
	elif id == 'Litecoin':
		id_col=ltc
	elif id == 'Ripple':
		id_col=rpl

	d = {}
	for elem in id_col.find():
		author_name=str(elem['author'])
		if (author_name == "['{username}']" or author_name == "[]"): continue 
		d.update({author_name[2:-2]:id_col.find({"author":elem['author']}).count()})

	d1 = sorted(d.items(), key=operator.itemgetter(1), reverse=True)

	return render_template('btc_info.html',id=id,dictt=d1)


@app.route('/<path:tid>/user/<path:id>')
def userInfo(tid,id):
	if tid == 'Bitcoin':
		id_col=btc
	elif tid == 'Ethereum':
		id_col=eth
	elif tid == 'EOS':
		id_col=eos
	elif tid == 'Litecoin':
		id_col=ltc
	elif tid == 'Ripple':
		id_col=rpl

	return render_template('user_info.html',id=id,author_mess=id_col.find({'author':id}),user_m_count=id_col.find({'author':id}).count(),all_m_count=id_col.find().count())

if __name__ == '__main__':
	app.run(debug=True)