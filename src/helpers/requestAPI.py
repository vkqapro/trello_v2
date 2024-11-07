import logging

import requests


class API_Call:
    def get_call(self):
        r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
        return r


    def POST(self):
        pass
