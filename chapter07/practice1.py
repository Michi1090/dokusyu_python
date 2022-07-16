# 1
import re

txt = """"
住所は〒160-0000 新宿区南町0-0-0です。
あなたの住所は〒210-9999 川崎町1-1-1ですね。
"""
ptn = re.compile(r'\d{3}-\d{4}')

results = ptn.findall(txt)
for result in results:
    print(result)

print()

# 2
txt = 'お問い合わせはsupport@exaple.comまで'
ptn = re.compile(
    '[a-zA-Z0-9_.+-]+@([a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]*\.)+[a-zA-Z]{2,}'
)

print(ptn.sub(r'<a href="mailto: \g<0>">\g<0></a>', txt))
