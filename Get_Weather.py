###スクレイピング、天気予報の取得

import urllib.request
from bs4 import BeautifulSoup

import requests
line_notify_token = ''
line_notify_api = 'https://notify-api.line.me/api/notify'

# 天気情報 (宇都宮)
url = "https://rss-weather.yahoo.co.jp/rss/days/4110.xml"

### 情報の取得を支持する部分
weather = []

with urllib.request.urlopen(url) as res:
    html = res.read()
    soup = BeautifulSoup(html, "html.parser")

    for item in soup.findAll("item"):
        title = item.find("title").string
        weather.append(title)

#ラインに返す部分
for i in range(0,5):
    message = weather[i]
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}  # Token
    line_notify = requests.post(line_notify_api, data=payload, headers=headers)