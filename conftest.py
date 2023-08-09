import pytest

from endpoints.create_url_endpoint import CreateUrlEndpoint


@pytest.fixture()
def create_short_url():
    new_url_endp = CreateUrlEndpoint()
    new_url_endp.post_new_url()
    short = new_url_endp.short
    long = new_url_endp.long
    return short, long
