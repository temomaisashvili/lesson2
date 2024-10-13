class Member:
    def __init__(self, name, age, status, subject):
        self.name = name
        self.age = age
        self.status = status
        self.subject = subject



class Teachers(Member):
    def __init__(self, name, age, status, subject, salary):
        super().__init__(name, age, status, subject)
        self.salary = salary
    def calculate_yearly_salary(self):
        return self.salary * 12


class Student(Member):
    def __init__(self, name, age, status, subject, grade):
        super().__init__(name, age, status, subject)
        self.grade = grade
    def __str__(self):
        return (f'name: {self.name}, age: {self.age}, status: {self.status}'
                f'subject: {self.subject}, grade: {self.grade}')
