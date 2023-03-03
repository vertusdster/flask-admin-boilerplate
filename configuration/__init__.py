from app import app
import urllib
import os

# secret key for user session
app.secret_key = "ITSASECRET"

#setting up mail
app.config['MAIL_SERVER']='127.0.0.1' #mail server
app.config['MAIL_PORT'] = 587 #mail port
app.config['MAIL_USERNAME'] = 'vertusd@gmail.com' #email
app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD'] #password
app.config['MAIL_USE_TLS'] = True #security type
app.config['MAIL_USE_SSL'] = False #security type

#database connection parameters
connection_params = {
    'user': '123',
    'password': os.environ['DB_PASSWORD'],
    'host': '127.0.0.1',
    'port': '33',
    'namespace': '',
}
