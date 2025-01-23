class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_child(cls, person_str):
        name, age = person_str.split(',')
        return cls(name.strip(), int(age.strip()))

    def _str_(self):
        return f"Name: {self.name}, Age: {self.age}"

person = Person.create_child("Bruno, 25")
print(person)




