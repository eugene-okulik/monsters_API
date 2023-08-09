import requests

from endpoints.create_url_endpoint import CreateUrlEndpoint


def test_create_short_url():
    new_url_endpoint = CreateUrlEndpoint()
    new_url_endpoint.long = 'https://sjdhfksjdfhksjdf.com'
    new_url_endpoint.post_new_url()
    assert new_url_endpoint.status_code_is_200()
    assert new_url_endpoint.long_url_is_the_same_as_sent()
    assert new_url_endpoint.code_is_not_empty()


def test_custom_short_url():
    new_url_endpoint = CreateUrlEndpoint(custom=True)
    new_url_endpoint.post_new_url()
    assert new_url_endpoint.status_code_is_200()
    assert new_url_endpoint.long_url_is_the_same_as_sent()
    assert new_url_endpoint.custom_code_is_the_same_as_sent()
