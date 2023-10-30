import string
import random
from collections import defaultdict

shortUrlType = "short"
longUrlType = "long"



class UrlShortner:
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.base_url = "https://twid/"
        self.characters = string.ascii_letters + string.digits
        self.storeDb = storeUrl()

    def storeData(self, url):
        self.storeDb.populateData(url)

    def shorten_url(self, long_url):
        if long_url in self.url_to_code:
            return self.base_url + self.url_to_code[long_url]
        code = self.generate_unique_code()
        short_url = self.base_url + code
        self.url_to_code[long_url] = short_url
        self.code_to_url[code] = long_url
        return short_url

    def generate_unique_code(self):
        code = ''.join(random.choice(self.characters) for _ in range(6))
        while code in self.code_to_url:
            code = ''.join(random.choice(self.characters) for _ in range(6))
        return code

    def expand_url(self, short_url):
        code = short_url.split("/")[-1]
        if code in self.code_to_url:
            return self.code_to_url[code]
        else:
            return "Short url doesn't exist"


class storeUrl:
    def __init__(self):
        self.code_to_url = defaultdict(str)
        self.url_to_code = defaultdict(str)

    def populateData(self, code=None, url=None, urlType=None):
        if code and urlType == longUrlType and url != None:
            self.code_to_url[code] = url
        # elif url and urlType="":
        #     pri


url_shortner = UrlShortner()
short_url = url_shortner.shorten_url("https://www.abcd.com")
print(short_url)
print(url_shortner.expand_url(short_url))
