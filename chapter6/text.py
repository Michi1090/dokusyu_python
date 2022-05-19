# 2
d = {'cucumber': 'キュウリ', 'lettuce': 'レタス', 'spinach': 'ホウレンソウ'}

d['cucumber'] = '胡瓜'
d.pop('spinach')
d.setdefault('carrot', 'ニンジン')

for item in d.items():
    print(item)

print()

# 3
sets1 = {2, 4, 8, 16, 32}
sets2 = {1, 10, 4, 16}

print(sets1.union(sets2))
sets3 = {str(i) for i in sets1 if i > 5}
print(sets3)


# 4
## 1
result = d.get('apple', '-')
print(result)

## 2
data = ['あ', '×', 'う', '×', 'お']
result = [i for i in data if i != '×']
print(result)

print()

## 3
del data[0:3]
print(data)

print()

## 4
t = ('いろは',)
print(t)

print()

## 5
for key, value in d.items():
    print(key, '=', value)
