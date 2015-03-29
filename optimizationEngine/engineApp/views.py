from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse


def scanTarget(request):
    scanResult = {
        "status": "",
        "message": "",
        "data": {
            "name": "",
            "httpStatus": 400,
            "ip": "",
            "serverLocation": "",
            "requestTime": "",
            "responseTime": 0,
            "assets": [
                {
                    "name": "",
                    "size": 0,
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