from engineApp.WebProfiler import *
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse


def scanTarget(request):
    target = request.GET["target"]
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
            "responseTime": scan.getContentTime(),
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