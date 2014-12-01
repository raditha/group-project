from flask import Flask ,url_for,redirect,session
from flask import request
from flask import render_template
from flask.ext.wtf import Form 
from wtforms import StringField, SubmitField ,IntegerField
from app import app
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)

@app.route('/',methods=['GET', 'POST']) 
def index(): 
    return render_template("test.html")
    
    
@app.route('/signup', methods = ['POST'])
def signup():
    email = request.form['email']
    email=
    print("The email address is '" + email + "'")
    return redirect('/lo')   
    
#@app.route('/LogIn',methods=['GET', 'POST'])
#def my_form_post():
    #url=request.form['url_box']
    #return url; 
    #return redirect(url_for('Log In'))
    
    
    
if __name__ == '__main__': 
	app.secret_key="123"
	app.run(debug=True)
	app.run(host='127.0.0.1')
    
    
    
    
    
    
    
    
