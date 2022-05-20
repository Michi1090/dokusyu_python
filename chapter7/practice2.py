import csv

data = [
    ['山田太郎', '160-9999', '東京都新宿区東町1-1-1'],
    ['鈴木次郎', '1070-1111', '東京都港区西町2-2-2'],
    ['佐藤花子', '150-2222', '東京都渋谷区東町3-3-3'],
]

with open('/Users/michi/Desktop/dokusyu_python/chapter7/address.csv', 'w', newline='', encoding='UTF-8') as file:
    writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
    writer.writerows(data)
