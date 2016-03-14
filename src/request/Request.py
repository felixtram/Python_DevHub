from Config import Config
from Utilities import RemoveFromJson
import jsonpickle
import urllib2

class Request (object):
    def __getstate__(self):
        body = RemoveFromJson(self.__dict__.copy())
        return body
     
    def __init__(self, category, proxy, endpoint, method):
        self.queryParams = {}
        self.url =  "https://" +Config.baseEndpoint + "/" + category + "/sp2/" + proxy + "/v" + str(Config.version) + "/" + endpoint
        self.method = method
    
    def send(self):
        if (Config.doNotSend):
            body = jsonpickle.encode(self, unpicklable = False)
            if (Config.printRequest):
                print(body)
            return body
        else:
            queryParamString = ''
            if (self.queryParams):
                queryParamString = "?"
                for key, value in self.queryParams.iteritems():
                    queryParamString += key + "=" + value + "&"
                queryParamString = queryParamString[:-1]
            url = self.url +queryParamString 
            body = jsonpickle.encode(self, unpicklable = False)
            if (Config.printRequest):
                print (body)
            if(Config.proxy):
                proxy = urllib2.ProxyHandler(Config.proxy)
                auth = urllib2.HTTPBasicAuthHandler()
                opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
                urllib2.install_opener(opener)
            req = urllib2.Request(url)
            req.add_header('Authorization', 'VANTIV license=' + "\"" + Config.license + "\"" )
            req.add_header('Content-Type', 'application/json')
            try:
                resp = urllib2.urlopen(req, body)
                code = resp.getcode()
                contents = resp.read()
            except urllib2.HTTPError, error:
                contents = error.read() 
            if (Config.printResponse):
                print(contents)

            return contents
            