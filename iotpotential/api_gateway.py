import json
from iotpotential import DEVICE_ID
import requests


class AuthenticationException(Exception):
    pass


class ApiGatewayException(Exception):
    pass


class ApiGateway(object):
    BASE_URL = 'https://api.enco.io/seaas/0.0.1'
    AUTH_URL = 'https://api.enco.io/token'
    ACCESS_TOKEN = None
    DEVICE_ID = '1C8779C0000000C9'

    def __init__(self):
        pass

    def _authenticate(self):
        """
        curl -i -X POST --basic -u "mKPCKnzKW4j8eVh4WaEmR3qlhwQa:uVzpRK57MizQ7aNN_0LL8M3avR4a"
        -H "Accept:application/json" -H "Content-Type:application/x-www-form-urlencoded"
        https://login.enco.io/oauth2/token
        -d "grant_type=password&username=vclaes1986@gmail.com&password=1saJocVin$"
        """
        # url = "https://login.enco.io/oauth2/token"

        querystring = {"grant_type": "client_credentials", "client_id": "mKPCKnzKW4j8eVh4WaEmR3qlhwQa",
                       "client_secret": "uVzpRK57MizQ7aNN_0LL8M3avR4a", "scope": "openid"}

        payload = "="
        headers = {
            'accept': "application/json",
            'content-type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache",
            'postman-token': "f51149f5-ffdf-c7ac-88f3-7d1445efda6c"
        }

        response = requests.request("POST", ApiGateway.AUTH_URL, data=payload, headers=headers, params=querystring)
        print(response.text)
        if response.status_code == 200:
            ApiGateway.ACCESS_TOKEN = json.loads(response.content).get('access_token')
        else:
            raise AuthenticationException('authentication failed')

    @staticmethod
    def get_current_location():
        print 'in get current location'
        uri = '{0}/{1}/{2}/{3}'.format(ApiGateway.BASE_URL, 'device', ApiGateway.DEVICE_ID, 'stream/9/pop')
        headers = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded',
                   'Authorization': 'Bearer ' + ApiGateway.ACCESS_TOKEN}
        response = requests.request('GET', uri, headers=headers)
        if response.status_code == 200:
            # print 'we have a good response'
            return json.loads(response.content)
        elif response.status_code == 401:
            ApiGateway._authenticate()
            return ApiGateway.get_current_location()
        else:
            raise ApiGatewayException(response)


ApiGateway()._authenticate()
