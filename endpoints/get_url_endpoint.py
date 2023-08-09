import requests
from endpoints.enpoint_handler import Endpoint


class GetUrlEndpoint(Endpoint):
    response = None

    def __init__(self, short):
        self.short = short

    def get_short_info(self):
        response = requests.get(f'https://gotiny.cc/api/{self.short}')
        self.response = response

    def url_is_correct(self, url):
        return self.response.text == url
