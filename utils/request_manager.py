import requests

class RequestManager:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.session = requests.Session()
        self.headers = headers if headers is not None else {}

    def send_get_request(self, endpoint, params=None):
        url = self.base_url + endpoint
        response = self.session.get(url, params=params, headers=self.headers)
        return response

    def send_post_request(self, endpoint, data=None, json=None, headers=None):
        url = self.base_url + endpoint
        if headers:
            request_headers = {**self.headers, **headers}
        else:
            request_headers = self.headers

        response = self.session.post(url, data=data, json=json, headers=request_headers)
        return response

    def send_put_request(self, endpoint, data=None, json=None, headers=None):
        url = self.base_url + endpoint
        if headers:
            request_headers = {**self.headers, **headers}
        else:
            request_headers = self.headers

        response = self.session.put(url, data=data, json=json, headers=request_headers)
        return response

    def send_delete_request(self, endpoint, headers=None):
        url = self.base_url + endpoint
        if headers:
            request_headers = {**self.headers, **headers}
        else:
            request_headers = self.headers

        response = self.session.delete(url, headers=request_headers)
        return response

    def close(self):
        self.session.close()
