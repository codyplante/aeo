from engineApp.WebProfiler import *
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse


def scanTarget(request):
    try:
        target = request.GET["target"]
    except Exception:
        target = "http://google.com"
    scan = WebProfiler(target)
    scanResult = {
        "status": "success",
        "message": "",
        "data": {
            "name": scan.request.url,
            "httpStatus": scan.request.status_code,
            "ip": "",
            "serverLocation": "",
            "requestTime": scan.request.elapsed.microseconds/1000,
            "responseTime": scan.request.history[0].elapsed.microseconds/1000,
            "assets": [
                {
                    "name": "index",
                    "size": len(scan.request.content),
                    "requestTime": "",
                    "responseTime": 0
                },
                {
                    "name": "",
                    "size": 0,
                    "requestTime": "",
                    "responseTime": 0
                },
            ]
        }
    }
    return JsonResponse(scanResult)