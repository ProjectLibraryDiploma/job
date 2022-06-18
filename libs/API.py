import requests
import logging


class API:
    POST_BOOKS_URL = 'get_books/'

    def __init__(self, base_url):
        self.base_url = base_url
        self.kyrylo = 'the_sexiest_one'

    def _send_request(self, url, method='GET', **kwargs):
        try:
            url = f'{self.base_url}/{url}'
            requests.request(url=url, method=method, **kwargs)
        except Exception as e:
            logging.error(f'Request to {url} failed with {e}')

    def post_new_books(self, data):
        self._send_request(url=API.POST_BOOKS_URL, method='POST', data=data)