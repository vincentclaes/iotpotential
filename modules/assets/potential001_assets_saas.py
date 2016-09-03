from oauth.api_oauth_gateway import get_promixmus_app_token, oauth_authorized




DEVICEID = "1C8779C0000000C9"
BASEURL = "https://api.enabling.be/seaas/0.0.1"


 logger = logging.getLogger()






#function getDevice Location from the SeAAS api and returns device location. 
#it requires values from get_promixmus_app_token to be passed in header
def getDeviceLocation():

     request_url = BASEURL + '/device/'+ DEVICEID + '/location'
     header_values = {'Authorization': 'Bearer ' + api_oauth_gateway.get_promixmus_app_token,'Accept': 'application/json', 'Content-Type': 'application/json'}
     location = request.get(request_url, headers)
     if location.status == 200:
     	return location.body
     else: 
     	location =  None 
     	logger.info ("Unable to get device location. maybe authentication issue or device is swithced off")