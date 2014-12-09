import socket
from flask import Flask 
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
      
    print("The email address is '" + email + "'")
    session['email']=email 
    return redirect('/LogIn')   

    
    



@app.route('/LogIn',methods=['GET', 'POST'])
def LogIn():   
    TCP_IP = '127.0.0.1'
    TCP_PORT = 80
    BUFFER_SIZE = 1024  # Normally 1024, but we want fast response
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
   
    conn, addr = s.accept()
    print 'Connection address:', addr
    while 1:
        data = conn.recv(BUFFER_SIZE)
        if  not data: break
        print "received data:", data
        email=session['email']
    conn.send(email)  # echo
    conn.close()
    
    
    #def my_form_post():
        #url=request.form['url_box']
        #return url; 
        #return redirect(url_for('Log In'))



if __name__ == '__main__': 
    app.secret_key="123"
    app.run(debug=True)
    app.run(host='127.0.0.1')
    










