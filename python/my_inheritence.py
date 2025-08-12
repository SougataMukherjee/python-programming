from python.my_class_two import Person


class Employee(Person):
    def __init__(self, name, age, emp_id, sal):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.sal = sal

    def introduce(self):
        return f"I am{self.name} and id is {self.emp_id}"

    def annual_sal(self):
        return self.sal*12


# person1 = Person('Sam', 29)
employee2 = Employee('Rupai', 29, 'FF125', 20000)
print(employee2.introduce())
