from flask import Flask 

app=Flask("MyApp")

@app.route("/")

def hello():
	return "hallo world"
	
app.run(debug=True)