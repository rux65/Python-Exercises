from flask import Flask , render_template, request

app=Flask("myApp")

@app.route("/test") # decorator

##can be /
##can be /news
## but need to update the url 


def hello():
    return "hallo world"
	
	
@app.route("/<name>")
def hello_someone(name):
	return render_template("hallo.html", name=name.title())


@app.route("/signup", methods=["POST"])
def signup():
	form_data=request.form
	var=form_data["email"]
	return "all ok"
	return var ## returns one or the other 
	
app.run(debug=True) # always run with debug true 