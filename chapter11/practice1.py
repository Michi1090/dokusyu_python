class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.firstname == other.firstname and self.lastname == other.lastname
        return False

p1 = Person('山田', '太郎')
p2 = Person('山田', '太郎')
p3 = Person('田中', '次郎')
print(p1 == p2)
print(p1 == p3)
