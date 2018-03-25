import urllib.request
import re
import threading
import time


def get_thumbs_up():
    page = urllib.request.urlopen('https://www.zhihu.com/question/64427330/answer/348184378')
    html = page.read().decode('utf-8')
    pattern = re.compile("(?<=voteupCount&quot;:).+?(?=,&quot;)")
    output.write(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+" "+re.findall(pattern, html)[0]+"\n")
    output.flush()
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+" "+re.findall(pattern, html)[0])
    tmpTimer = threading.Timer(5, get_thumbs_up)
    tmpTimer.start()
output = open('data', 'a+')
timer = threading.Timer(1, get_thumbs_up)
timer.start()

'''
soup = BeautifulSoup(page,"html.parser")
print(soup.prettify())
s = soup.find_all(text=re.compile("(?<=<!-- react-text: 205 -->).+?(?=<!-- /react-text -->)"))
print(s)
'''
