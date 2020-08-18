import datetime

import requests
line_notify_token = ''
line_notify_api = 'https://notify-api.line.me/api/notify'

# 現時刻の取得
weekday = datetime.datetime.today().weekday()

# 今日の曜日
weekday_list = {
    0: '月曜日',
    1: '火曜日',
    2: '水曜日',
    3: '木曜日',
    4: '金曜日',
    5: '土曜日',
    6: '日曜日'
}
today = weekday_list[weekday]

# 曜日別の回収ゴミ
garbage_list = {
    0: '',
    1: '焼却ゴミ',
    2: '不燃ゴミ',
    3: '資源ゴミ、危険ゴミ',
    4: '焼却ゴミ',
    5: '',
    6: ''
}
today_garbage = garbage_list[weekday]

# 通知
if weekday == 0 or weekday >= 5 :
    message = '今日は{}、回収はありません。'.format(today)
else:
    message = '今日は{}、「{}」の日です。'.format(today,today_garbage)

message = message
payload = {'message': message}
headers = {'Authorization': 'Bearer ' + line_notify_token}  # Token
line_notify = requests.post(line_notify_api, data=payload, headers=headers)