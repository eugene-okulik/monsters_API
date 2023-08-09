import requests
import string
import random

from endpoints.enpoint_handler import Endpoint


class CreateUrlEndpoint(Endpoint):
    response = None
    short = None
    long = None
    response_long = None

    def __init__(self, long=None, custom=None):
        if custom:
            self.custom = "".join(random.choice(string.ascii_lowercase) for _ in range(10))
        else:
            self.custom = custom
        if long:
            self.long = long
        else:
            self.long = f'https://{"".join(random.choice(string.ascii_lowercase) for _ in range(10))}.com'
        # self.response = self.post_new_url(long)

    def post_new_url(self):
        if self.custom:
            body = {
                'long': self.long,
                'custom': self.custom
            }
        else:
            body = {
                'input': self.long
            }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post('https://gotiny.cc/api', json=body, headers=headers)
        self.response = response
        self.short = self.response.json()[0]['code']
        self.response_long = self.response.json()[0]['long']

    def long_url_is_the_same_as_sent(self):
        return self.long == self.response_long

    def code_is_not_empty(self):
        return len(self.short) > 0

    def custom_code_is_the_same_as_sent(self):
        return self.custom == self.short
