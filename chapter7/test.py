# 2
from cmath import pi
import re
from traceback import print_tb

ptn = re.compile(r'\d{2,4}-\d{2,4}-\d{4}')
with open('./chapter7/sample.dat', 'r', encoding='UTF-8') as file:
    for line in file:
        results = ptn.findall(line)

        for result in results:
            print(result)

print()

# 3
## 1
print(abs(-12))

print()

## 2
print(round(987.654, 2))

print()

# 3
import os

PATH = './'
for f in os.listdir(PATH):
    print(f)

print()

# 4
import random
print(random.randint(1,100))

print()

# 5
import re

txt = 'にわに/わうらにわに\わにわと/りがいる'
ptn = re.compile(r'[/\\]')
result = ptn.split(txt)
print(result)
