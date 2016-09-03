from flask_oauth import OAuth
from flask import session, redirect



    logger = logging.getLogger()
    #create OAuth object 
    oauth = OAuth() 

    #register application suing the oath.remote_app method initialze the required OAuth machinery.
    promixmus_app = oauth.remote_app('promixmus_app',

        base_url='https://api.smartliving.io/login',
        request_token_url=None,
        access_token_url=None,
        authorize_url=None,
        consumer_key='mKPCKnzKW4j8eVh4WaEmR3qlhwQa',
        consumer_secret='uVzpRK57MizQ7aNN_0LL8M3avR4a',
        request_token_params={'grant_type':'password','username':'vclaes1986@gmail.com','password':'1saJocVin$'}
      )


#Authenticate and pass it to oauth_authorized to get device location. f
@app.route('/login')
def login():
	return promixmus_app.authorize(callback=url_for('oauth_authorized'))

#Proximus passes all relevant information to getDeviceLocation
@promixmus_app.authorized_handler 
@app.route('oauth_authorized')
def oauth_authorized(response):
	if response is None:
		logger.info('Authorization was not sucessful: error message {0}', .format(response))
		return redirect(url_for('/fullmap'))
	#store the session token gotten from proximus enco
	session['promixmus_token'] = (response['access_token'] , response['refresh_token'])
	logger.info('Authorization was successful : wthe tokens access_token {0}, refresh_token {1}' .format(response['access_token'],response['refresh_token']))
   return response.body

@promixmus_app.tokengetter 
def get_promixmus_app_token(token=None):
    return session.get('access_token')