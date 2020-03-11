from flask import Flask, render_template, session, request
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Leyndo'

vorur=[
	[0,"Coat",10000,"coat.png"],
	[1,"Hoodie",2000,"hoodie.png"],
	[2,"Pants",1600,"pants.png"],
	[3,"Socks",3400,"socks.png"],
	[4,"T-shirt",100,"tshirt.png"],
	[5,"Gloves",4000,"gloves.png"]
]


@app.route('/')
def index():
	karfa = 0
	if 'karfa' in session:
		karfa = len(session['karfa'])
		til = True
	else:
		til = False
	return render_template("index.tpl", vorur=vorur, k=karfa, til=til)


@app.route('/ikorfu/<int:id>')
def ikorfu(id):
	karfa = []
	if 'karfa' in session:
		karfa = session['karfa']
		karfa.append(id)
		session['karfa'] = karfa
	else:
		karfa.append(id)
		session['karfa'] = karfa
	print(len(karfa))
	return render_template("ikorfu.tpl", vorur=vorur)


@app.route('/karfa')
def karfa():
	karfa = []
	k=0
	heild=0
	if 'karfa' in session:
		karfa = session['karfa']
		k = len(session['karfa'])
		for x in karfa:
			for y in vorur:
				if y[0] == x:
					heild += y[2]
	return render_template("karfa.tpl", vorur=vorur, karfa=karfa, k=k, heild=heild)


@app.route('/eyda/<int:id>')
def eyda(id):
	karfa = []
	if 'karfa' in session:
		karfa = session['karfa']
		karfa.remove(id)
		session['karfa'] = karfa
	return render_template("eyda.tpl", vorur=vorur)

@app.route('/taema')
def taema():
	session.pop('karfa',None)
	return render_template("taema.tpl", vorur=vorur)

@app.route('/karfa/kaupa')
def kaupa():
	karfa = []
	heild = 0
	if 'karfa' in session:
		karfa = session['karfa']
		for x in karfa:
			for y in vorur:
				if y[0] == x:
					heild += y[2]
	return render_template("kaupa.tpl", vorur=vorur, karfa=karfa, heild=heild)

@app.route('/karfa/kaupa/takk', methods=['GET','POST'])
def takk():
	if request.method == 'POST':
		nafn = request.form['name']
		netfang = request.form['email']
	karfa = []
	session['karfa'] = karfa
	return render_template("takk.tpl", vorur=vorur, nafn=nafn, netfang=netfang)

@app.errorhandler(404)
def error404(error):
	return render_template("404.tpl"),404

if __name__ == "__main__":
	app.run(debug=True)