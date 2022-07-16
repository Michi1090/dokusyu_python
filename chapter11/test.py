# 2
class SingletonMeta(type):
    def __init__(cls, name, bases, disc, **kwargs):
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.instance

class MySingleton(metaclass=SingletonMeta):
    pass

# 3
## 1
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Person: {self.name}'

## 2
class MyAppError(Exception):
    pass

## 3
import dataclasses

@dataclasses.dataclass(frozen=True)
class Book:
    title: str
    price: int

## 4
for f in dataclasses.field(Book):
    print(f)

## 5
try:
    raise KeyError
except KeyError:
    raise
except TypeError:
    raise
finally:
    print('終了しました')
