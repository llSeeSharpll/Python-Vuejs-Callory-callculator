import flask 
from flask import jsonify, request, session, redirect
import sys
from flask.json import dumps

from sqlalchemy.sql.expression import null
sys.path.append('../')
from services.auth import Auth
from services.item_user import Item_User
from models.defaultMethodResult import DefaultMethodResult
from models.loginTokenResult import LoginTokenResult
from services.jsonClassEncoder import JsonClassEncoder

import flask_login
from flask_login import user_loaded_from_header
from services.customSessionInterface import CustomSessionInterface

app = flask.Flask(__name__)
# Configurations
ALOWED_CORS_DOMAIN = 'http://localhost:8080'
app.secret_key = 'this will be used to cryptograph sensible data like authentication tokens'
jsonClassEncoder = JsonClassEncoder()

login_manager = flask_login.LoginManager()
login_manager.init_app(app)
app.session_interface = CustomSessionInterface()
# End of Configurations section

authModule = Auth()
item_UserModule = Item_User()

@login_manager.user_loader
def load_user(user_id):
    return authModule.load_user(user_id)

# Only requests that have an Authorization request reader set with a valid login token
# can access the protected routes, like this '/home' one for example
@app.route('/home', methods=(['GET']))
@flask_login.login_required
def home():
    return 'Home protected by @flask_login.login_required'

# Sets the route for this endpoint, this will configure our web server to receive requests at this path.
@app.route('/register', methods=(['POST']))
def register():
    requestPayload = request.get_json()
    username=requestPayload['username']
    email = requestPayload['email']
    password = requestPayload['password']
    mobilePhone= requestPayload['mobilePhone']
    gender = requestPayload['gender']
    weight = requestPayload['weight']
    height = requestPayload['height']
    age = requestPayload['age']

    registerResult = authModule.register(username, email, password, mobilePhone,gender,float(weight),float(height),int(age))
    if registerResult.success == True:
        return jsonClassEncoder.encode(registerResult), 200
    else:
        return jsonClassEncoder.encode(registerResult), 500

# this route will login the user and return a Json Web Token, this token 
# will be stored into the client aplication and need to be passed over for each new 
# request, via Authorizaton header.
@app.route('/token', methods=(['POST']))
def token():
    authToken = request.headers.get('Authorization')
    activeSession = authModule.GetActiveSession(authToken)
    if activeSession is not None:
        loginResult = LoginTokenResult(True, 'Login successful', activeSession.jwToken)
        return jsonClassEncoder.encode(loginResult), 200
    else:
        requestPayload = request.get_json()  
        username = requestPayload['username']
        password = requestPayload['password']
        loginResult = authModule.getLoginToken(username, password, app.config['SECRET_KEY'])
        if loginResult.success == True:
            return jsonClassEncoder.encode(loginResult), 200
        else:
            return jsonClassEncoder.encode(loginResult), 401

# This will invalidate the user current user session on the server
@app.route('/logout', methods=(['POST']))
def sessionLogout():
    authToken = request.headers.get('Authorization')
    logoutResult = authModule.SessionLogout(authToken, request.url)
    if logoutResult.success == True:        
        return jsonClassEncoder.encode(logoutResult), 200
    else:
        return jsonClassEncoder.encode(logoutResult), 401


# This enable CORS, it means that this server will authorize AJAX calls from
# other domains than the current domain where the API is running
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = ALOWED_CORS_DOMAIN
    if request.method == 'OPTIONS':
        response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
        headers = request.headers.get('Access-Control-Request-Headers')
        if headers:
            response.headers['Access-Control-Allow-Headers'] = headers

    return response
app.after_request(add_cors_headers)


# Checks if the user is auhenticated for protected routes decorated with @flask_login.login_required
@login_manager.request_loader
def load_user_from_request(request):
    # Get the token from the Authorization request header 
    authToken = request.headers.get('Authorization')
    if authToken:
        try:
            # Checks if is there a active session for this token and return his user
            user = authModule.GetUserByToken(authToken)
            return user
        except TypeError:
            pass        

    # If it can't find an active session returns None, 
    # this will cause the request decorated with @flask_login.login_required been denied
    return None
@app.route('/addfood', methods=['POST'])
def addfood():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        username = post_data.get('username')
        name = post_data.get('name')
        fat= int(post_data.get('fat'))
        prot = int(post_data.get('prot'))
        carb = int(post_data.get('carb'))
        callories = int(post_data.get('callories'))
        savedata =  item_UserModule.SaveFood(username,name,fat,prot,carb,callories)
        if savedata:
            return jsonify('All Done')
        return jsonify('error happened')

@app.route('/getfood', methods=['POST'])
def getfood():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        username = post_data.get('username')
        fooddata =  item_UserModule.GetFood(username)
        if fooddata is not null:
            return dumps(fooddata)
        return jsonify('error happened')

@app.route('/getdetials',methods=['POST'])
def getdetails():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        username = post_data.get('username')
        fooddata =  item_UserModule.GetDetail(username)
        return dumps(fooddata)
    return jsonify('error happened')

@app.route('/changeheight',methods=['POST'])
def changeheight():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        username = post_data.get('username')
        height = post_data.get('height')
        item_User=item_UserModule.UpdateHeight(username,float(height))
        if item_User is not null:
            return jsonify("done")
        return jsonify("error")

@app.route('/changeweight',methods=['POST'])
def changeweight():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        username = post_data.get('username')
        weight = post_data.get('weight')
        item_User=item_UserModule.UpdateWeight(username,float(weight))
        if item_User is not null:
            return jsonify("done")
        return jsonify("error")

@app.route('/changeage',methods=['POST'])
def changeage():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        username = post_data.get('username')
        age = post_data.get('age')
        item_User=item_UserModule.UpdateAge(username,float(age))
        if item_User is not null:
            return jsonify("done")
        return jsonify("error")


















if __name__=='__main__':
    app.run()