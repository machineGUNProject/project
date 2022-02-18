import json
import base64
import requests

def position_num(path):
    with open(path, "rb") as f:
        img = base64.b64encode(f.read())

     # 본인의 APIGW Invoke URL로 치환
    URL = "https://4700f1b2658a488d9056e37470ff97b9.apigw.ntruss.com/custom/v1/4967/db0b74efcba54bc7f7c1fda6e0d9ed1a526a2ebf53613e41b93290f4e24b87a0/general"

     # 본인의 Secret Key로 치환
    KEY = "UVFIU3RXZ2x3SUhyQUd0V2FYZUttRnZ0ZmxnVkxjTXE="

    headers = {
        "Content-Type": "application/json",
        "X-OCR-SECRET": KEY
    }

    data = {
        "version": "V1",
        "requestId": "sample_id", # 요청을 구분하기 위한 ID, 사용자가 정의
        "timestamp": 0, # 현재 시간값
        "images": [
            {
                "name": "sample_image",
                "format": "jpg",
                "data": img.decode('utf-8')
            }
        ]
    }
    data = json.dumps(data)
    response = requests.post(URL, data=data, headers=headers)
    res = json.loads(response.text)
    #print(res)

    return len(res['images'][0]['fields'])

def position_find(path, i):
    with open(path, "rb") as f:
        img = base64.b64encode(f.read())

     # 본인의 APIGW Invoke URL로 치환
    URL = "https://4700f1b2658a488d9056e37470ff97b9.apigw.ntruss.com/custom/v1/4967/db0b74efcba54bc7f7c1fda6e0d9ed1a526a2ebf53613e41b93290f4e24b87a0/general"

     # 본인의 Secret Key로 치환
    KEY = "UVFIU3RXZ2x3SUhyQUd0V2FYZUttRnZ0ZmxnVkxjTXE="

    headers = {
        "Content-Type": "application/json",
        "X-OCR-SECRET": KEY
    }

    data = {
        "version": "V1",
        "requestId": "sample_id", # 요청을 구분하기 위한 ID, 사용자가 정의
        "timestamp": 0, # 현재 시간값
        "images": [
            {
                "name": "sample_image",
                "format": "jpg",
                "data": img.decode('utf-8')
            }
        ]
    }
    data = json.dumps(data)
    response = requests.post(URL, data=data, headers=headers)
    res = json.loads(response.text)
    #print(res)

    #print(len(res['images'][0]['fields']))
    #res['images'][0]['fields'][0]['boundingPoly']['vertices']

    #for i in range(0, len(res['images'][0]['fields'])):
    #    print(res['images'][0]['fields'][i]['boundingPoly']['vertices'])

    a = res['images'][0]['fields'][i]['boundingPoly']['vertices'][0]['x']
    b = res['images'][0]['fields'][i]['boundingPoly']['vertices'][0]['y']

    c = res['images'][0]['fields'][i]['boundingPoly']['vertices'][2]['x']
    d = res['images'][0]['fields'][i]['boundingPoly']['vertices'][2]['y']


    return (a, b), (c, d)
    """
    print(type(res['images']))
    a = res['images']
    print(a)
    print(a[0])
    b = a[0]
    print(b['fields'])
    c = b['fields']
    print(c[0])
    d = c[0]
    print(d['boundingPoly'])
    e = d['boundingPoly']
    print(e['vertices'])
    f = e['vertices']
    print(f[0])
    print(f[0]['x'])
    print(f[0]['y'])
    print(f[2])
    """

#print(position_find("C:/Users/Ai/Desktop/img_position/bb.jpg"), 0)
