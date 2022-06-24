class MyClass:
    def __init__(self, kind, name):
        self.kind = kind
        self.name = name

    def show(self):
        return f'ペットの{self.kind}の名前は、{self.name}です。'

class MySubClass(MyClass):
    def show(self):
        return f'[{super().show()}]'

if __name__ == '__main__':
    m1 = MySubClass('犬', 'ラッキー')
    m2 = MySubClass('猫', 'クム')
    print(m1.show())
    print(m2.show())
