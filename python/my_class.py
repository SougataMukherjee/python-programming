class Person:
    compile = "dev"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._email = None

    def introduce(self):
        return f"Hi, I am {self.name} ,and {self.age} years old"

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" in value:
            self._email = value
        else:
            raise ValueError('invalid email')


person1 = Person('Sam', 29)
person1.email = "sam@gmail.com"
print(person1.introduce(), person1.email)
