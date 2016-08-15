import unirest
import subprocess


class AuthenticationException(Exception):
    pass


class ApiGateway(object):
    BASE_URL = 'https://api.enabling.be/seaas/0.0.1'
    AUTH_URL = 'https://login.enabling.be/oauth2/token'
    CONSUMER_KEY = 'mKPCKnzKW4j8eVh4WaEmR3qlhwQa'
    CONSUMER_SECRET = 'uVzpRK57MizQ7aNN_0LL8M3avR4a'
    SESSION_TOKEN = '1cfa6ae8ac38b87fee124a1443671f'
    DEVICE_ID = '1C8779C0000000C9'

    def __init__(self):
        pass

    def _authenticate(self):
        """
        curl -i -X POST --basic -u "mKPCKnzKW4j8eVh4WaEmR3qlhwQa:uVzpRK57MizQ7aNN_0LL8M3avR4a"
        -H "Accept:application/json" -H "Content-Type:application/x-www-form-urlencoded"
        https://login.enabling.be/oauth2/token
        -d "grant_type=password&username=vclaes1986@gmail.com&password=1saJocVin$
        """

        uri = '{0}'.format(ApiGateway.AUTH_URL)
        parameters = {'grant_type': 'password', 'username': 'vclaes1986@gmail.com', 'password': '1saJocVin$'}
        headers = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}
        auth = (ApiGateway.CONSUMER_KEY, ApiGateway.CONSUMER_SECRET)
        response = unirest.post(uri, auth=auth, headers=headers, parameters=parameters)
        if response.code == 200:
            print response.body
        else:
            raise AuthenticationException('authentication failed')

    @staticmethod
    def get_current_location():
        uri = '{0}/{1}/{2}/{3}'.format(ApiGateway.BASE_URL,'device',ApiGateway.DEVICE_ID , 'location')
        headers = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded',
                   'Authorization': 'Bearer ' + ApiGateway.SESSION_TOKEN}
        response = unirest.get(uri, headers=headers)
        if response.code == 200:
            #print response.body
            pass
        return response.body
