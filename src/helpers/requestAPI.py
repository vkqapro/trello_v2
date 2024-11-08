import requests

class API_Calls:

    def GET(self):
        req = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
        return req