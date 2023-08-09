import requests
from endpoints.get_url_endpoint import GetUrlEndpoint


def test_get_existing_long(create_short_url):
    short, long = create_short_url
    url_info = GetUrlEndpoint(short)
    url_info.get_short_info()
    assert url_info.status_code_is_200()
    assert url_info.url_is_correct(long)
