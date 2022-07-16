# 3
import calendar
import datetime
import locale

locale.setlocale(locale.LC_ALL, 'ja_JP.UTF-8')
dt = datetime.datetime(2020, 12, 4, 11, 37, 20, 0,
                       datetime.timezone(datetime.timedelta(hours=9)))
print(dt.strftime('%Y年%m月%d日%I時'))


# 4
## 1
txt = 'となりのきゃくはよくかきくうきゃくだ'
print(txt.rfind('きゃく'))

## 2
place = '千葉'
temp = 17.256
print('{0}の気温は、{1:.2f}℃ です。'.format(place, temp))

## 3
txt = '彼女の名前は花子です。'
result = txt.replace('彼女', '妻')
print(result)

## 4
today = datetime.datetime.today()
result = today + datetime.timedelta(days=6, hours=5)
print(result)

## 5
calendar.setfirstweekday(6)
print(calendar.month(2020, 10, 5))
