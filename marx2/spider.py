'''
:authority: www.zhihu.com
:method: GET
:path: /api/v4/answers/348184378/voters?include=data%5B*%5D.answer_count%2Carticles_count%2Cfollower_count%2Cgender%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&limit=10&offset=0
:scheme: https
accept: application/json, text/plain, */*
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
authorization: oauth c3cef7c66a1843f8b3a9e6a1e3160e20
cache-control: no-cache
cookie: _zap=01e0284b-287e-4203-9f2c-5b07a0cefc3c; __DAYU_PP=nzrJUjBmiR7ivZFinvJU21d30f48128e; _xsrf=0b31f530-1733-41ef-90e2-889bc0f96b1e; d_c0="AOAuD--EVw2PTqDSK0D-jNsRXFsnwAbbI0o=|1521991618"; q_c1=0a30f8a266294ae5a0944311c9b84f5c|1521991618000|1519239324000; l_cap_id="NWQyZmQzOGViNzlmNDVhMDg5NDQ2MTUyNTM2YzIxNjU=|1521994061|15c12d67f9d9b6442aecc49449d800ef5c963690"; r_cap_id="NDU0ZjlkZTE5NmI1NDFmMGE0YTM5MTY0ZTJlMzBlYWY=|1521994061|1cb30c6d63ec5a193d3ab4e8ac88e0dcdf865df6"; cap_id="MDNmNGM1ZTYzMjkwNDRhNTg2MDZhYjljODYyMDRjY2I=|1521994061|3d8d0c942ef52fbd33c4b83f355a24d9fa4f88ca"; capsion_ticket="2|1:0|10:1521995014|14:capsion_ticket|44:NWZhNjYzYWE2NmQwNDQ5NGJmODc4MzQzNzcwOWU0MjE=|75cc6f0bacdc46f99b50d683e885c8fa407ecaed96b55cf468dd1fc67ff4ecd2"; __utma=155987696.1517916129.1521995104.1521995104.1521995104.1; __utmb=155987696.0.10.1521995104; __utmc=155987696; __utmz=155987696.1521995104.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)
dnt: 1
pragma: no-cache
referer: https://www.zhihu.com/question/64427330/answer/348184378
user-agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36
x-udid: AOAuD--EVw2PTqDSK0D-jNsRXFsnwAbbI0o=
'''
import json
import threading
import urllib.request

import time

try:
    from BytesIO import BytesIO
except ImportError:
    from io import BytesIO


def get_people():
    if len(id_list) > 20:
        id_list.clear()
    headers = {
        'accept': 'application/json, text/plain, */*',
        # 'accept-encoding': " gzip, deflate",
        'accept-language': 'zh-CN,zh;q=0.9',
        'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20',
        'cache-control': 'no-cache',
        'cookie': ' _zap=01e0284b-287e-4203-9f2c-5b07a0cefc3c; __DAYU_PP=nzrJUjBmiR7ivZFinvJU21d30f48128e; _xsrf=0b31f530-1733-41ef-90e2-889bc0f96b1e; d_c0="AOAuD--EVw2PTqDSK0D-jNsRXFsnwAbbI0o=|1521991618"; q_c1=0a30f8a266294ae5a0944311c9b84f5c|1521991618000|1519239324000; l_cap_id="NWQyZmQzOGViNzlmNDVhMDg5NDQ2MTUyNTM2YzIxNjU=|1521994061|15c12d67f9d9b6442aecc49449d800ef5c963690"; r_cap_id="NDU0ZjlkZTE5NmI1NDFmMGE0YTM5MTY0ZTJlMzBlYWY=|1521994061|1cb30c6d63ec5a193d3ab4e8ac88e0dcdf865df6"; cap_id="MDNmNGM1ZTYzMjkwNDRhNTg2MDZhYjljODYyMDRjY2I=|1521994061|3d8d0c942ef52fbd33c4b83f355a24d9fa4f88ca"; capsion_ticket="2|1:0|10:1521995014|14:capsion_ticket|44:NWZhNjYzYWE2NmQwNDQ5NGJmODc4MzQzNzcwOWU0MjE=|75cc6f0bacdc46f99b50d683e885c8fa407ecaed96b55cf468dd1fc67ff4ecd2"; __utma=155987696.1517916129.1521995104.1521995104.1521995104.1; __utmb=155987696.0.10.1521995104; __utmc=155987696; __utmz=155987696.1521995104.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
        'dnt': '1',
        'pragma': 'no-cache',
        'referer': 'https://www.zhihu.com/question/64427330/answer/348184378',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'x-udid': 'AOAuD--EVw2PTqDSK0D-jNsRXFsnwAbbI0o='}
    req = urllib.request.Request(url="https://www.zhihu.com/api/v4/answers/348184378/voters?include=data%5B*%5D"
                                     ".answer_count%2Carticles_count%2Cfollower_count%2Cgender%2Cis_followed"
                                     "%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&limit=10&offset=0",
                                 headers=headers)
    res = urllib.request.urlopen(req)
    data = json.loads(res.read().decode("utf-8"))
    print(data['data'][0]['name'])
    totals = data["paging"]["totals"]
    people_list = data["data"]
    for people in people_list:
        if people["id"] not in id_list:
            output.write(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+" "+
                str(str(totals) + " " + str(people["id"]) + " " + str(people["name"]) + " " + str(
                    people["gender"]) + " " + str(
                    people["follower_count"]) + " " + "\n"))
            output.flush()
            id_list.append(people["id"])
    tmpTimer = threading.Timer(5, get_people)
    tmpTimer.start()


id_list = []
output = open('people', 'a+')
timer = threading.Timer(1, get_people)
timer.start()
