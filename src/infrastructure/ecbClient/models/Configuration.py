import http.client

class Configuration:
    def __init__(self):
        self.httpClient = http.client.HTTPSConnection("www.ecb.europa.eu")