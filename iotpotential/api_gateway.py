import json

import requests


class AuthenticationException(Exception):
    pass


class ApiGatewayException(Exception):
    pass


class ApiGateway(object):
    BASE_URL = 'https://api.enabling.be/seaas/0.0.1'
    AUTH_URL = 'https://login.enabling.be/oauth2/token'
    # CONSUMER_KEY = 'mKPCKnzKW4j8eVh4WaEmR3qlhwQa'
    # CONSUMER_SECRET = 'uVzpRK57MizQ7aNN_0LL8M3avR4a'
    ACCESS_TOKEN = None
    DEVICE_ID = '1C8779C0000000C9'

    def __init__(self):
        pass

    def _authenticate(self):
        """
        curl -i -X POST --basic -u "mKPCKnzKW4j8eVh4WaEmR3qlhwQa:uVzpRK57MizQ7aNN_0LL8M3avR4a"
        -H "Accept:application/json" -H "Content-Type:application/x-www-form-urlencoded"
        https://login.enabling.be/oauth2/token
        -d "grant_type=password&username=vclaes1986@gmail.com&password=1saJocVin$"
        """
        url = "https://login.enabling.be/oauth2/token"

        payload = "grant_type=password&username=vclaes1986%40gmail.com&password=1saJocVin%24"
        headers = {
            'accept': "application/json",
            'content-type': "application/x-www-form-urlencoded",
            'authorization': "Basic bUtQQ0tuektXNGo4ZVZoNFdhRW1SM3FsaHdRYTp1VnpwUks1N01pelE3YU5OXzBMTDhNM2F2UjRh",
            'cache-control': "no-cache",
            'postman-token': "7afd9f3a-c728-185b-1d39-944da55528f6"
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)
        if response.status_code == 200:
            ApiGateway.ACCESS_TOKEN = json.loads(response.content).get('access_token')
        else:
            raise AuthenticationException('authentication failed')

    @staticmethod
    def get_current_location():
        uri = '{0}/{1}/{2}/{3}'.format(ApiGateway.BASE_URL, 'device', ApiGateway.DEVICE_ID, 'location')
        headers = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded',
                   'Authorization': 'Bearer ' + ApiGateway.ACCESS_TOKEN}
        response = requests.request('GET', uri, headers=headers)
        if response.status_code == 200:
            return json.loads(response.content)
        elif response.status_code == 401:
            ApiGateway._authenticate()
            return ApiGateway.get_current_location()
        else:
            raise ApiGatewayException(response)


ApiGateway()._authenticate()
