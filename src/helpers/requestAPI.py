import requests

class Api_Calls:
    def GET(self, status_code):
        req = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
        assert req.status_code == int(status_code)
        return req


# req = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
