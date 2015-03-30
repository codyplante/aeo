from datetime import datetime
import requests
from bs4 import BeautifulSoup
class WebProfiler:
    def __init__(self, target="http://google.ca"):
        self.request = None
        self.requestTimes = self.detailedScanTarget(target)

    def getResourceLinks(self):
        soup = BeautifulSoup(self.request.text)
        self.assetLinks = []
        for link in soup.select('[src]'):
            self.assetLinks.append(link['src'])

    def getResponseTime(self):
        return self.compareTime("requestStart", "headerResponse")

    def getContentTime(self):
        return self.compareTime("headerResponse", "contentResponse")

    def printResponseTiming(self):
        s = "Response Times:\n"
        s += "{}: {} ms\n".format("response", self.getResponseTime())
        s += "{}: {} ms\n".format("content",  self.getContentTime())
        s += "{}: {} ms\n".format("total", self.getResponseTime() + self.getContentTime())
        print (s)


    def compareTime(self, startEvent, endEvent):
        return (self.requestTimes[endEvent] - self.requestTimes[startEvent]).microseconds/1000

    def detailedScanTarget(self, target):
        requestStart = datetime.now()
        r = requests.get(target, stream=True)
        headerResponse = datetime.now()
        c = r.content
        self.request = r
        contentResponse = datetime.now()
        return ({
            "requestStart": requestStart,
            "headerResponse": headerResponse,
            "contentResponse": contentResponse
        })
