





class get_server_info():

    def __init__(self):
        self.url = "http://192.168.61.128:3000/api/Crawlers/Security_Focus/status"
        #self.url = "http://localhost:8000/postreq/"
        #self.headers = {'content-type': 'application/json'}
        self.headers = {'content-type': 'application/x-www-form-urlencoded'}

    def get_url(self):
        return self.url
    def get_headers(self):
        return self.headers
