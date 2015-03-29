var jsonTemplate = {
    "status": "", // server status
    "message": "", // (optional) server message
    "data": {
        "name": "", // name of site
        "httpStatus": 400, // status code
        "ip": "", // IP (geocoding done client side)
        "serverLocation": "", // vps being hit
        "requestTime": "", // UTC
        "responseTime": 0, // full response time (milliseconds)
        "assets": [
            {
                "name": "", // file name
                "size": 0, // bytes
                "requestTime": "", // UTC
                "responseTime": 0 // milliseconds
            },
            {
                "name": "", // file name
                "size": 0, // bytes
                "requestTime": "", // UTC
                "responseTime": 0 // milliseconds
            },
        ]
    }
}