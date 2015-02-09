import socket
from functools import wraps
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


@app.route('/enterUrl', methods = ['POST'])
def enterUrl():
    url = request.form['url']  
    print("The url to watch is " + url + "'")
    session['url']=url 
    return redirect('/sendUrl')   




@app.route('/sendUrl',methods=['GET', 'POST'])
def sendUrl(): 
        url=session['url']
        #print("The email address is '" + email + "raditha")
    #while 1:
        TCP_IP = '192.168.25.1'
        TCP_PORT = 8080
        BUFFER_SIZE = 1024  # Normally 1024, but we want fast response
        #print("The email address is '" + email + "dilshan")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((TCP_IP, TCP_PORT))
        s.listen(1)
   
        conn, addr = s.accept()
        print 'Connection address:', addr
        #while 1:
        #print("The email address is '" + email + "damith")
            #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #s.connect((TCP_IP, TCP_PORT))
            
        data = conn.recv(BUFFER_SIZE)
        #if  not data: break
        print "received data:", data
        url=session['url']
        #print("The email address is '" + email + "sadasdasd")
        conn.send(url.encode())
        #conn.send(email)  # echo
        conn.close()
        print("done")
        return redirect('/change')   

@app.route('/change',methods=['GET', 'POST']) 
def change():    
    TCP_IP = '192.168.25.1'
    TCP_PORT = 8080
    BUFFER_SIZE = 1024
    MESSAGE = ('Hello, World!')
    
    s = socket.socket()         # Create a socket object
    #host = socket.gethostname() # Get local machine name
    #port = 12345                # Reserve a port for your service.
    s.bind((TCP_IP, TCP_PORT))        # Bind to the port

    s.listen(5)                 # Now wait for client connection.
    while True:
        c, addr = s.accept()     # Establish connection with client.
        print 'Got connection from', addr
        print c.recv(1024)
        
        #c.send('Changes of Log file have been received')
        c.close()                # Close the connection



if __name__ == '__main__': 
    app.secret_key="123"
    
    app.run(debug=True)
    
    app.run(host='127.0.0.1')
    










