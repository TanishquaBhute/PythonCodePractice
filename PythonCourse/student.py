from person import Person


class Student(Person):
    def __init__(self, name, surname, age, address, skills=[]):
        super().__init__(name, surname, age, address, skills)

    def print_skill(self):
        print(f"Student skills: {self.skills}")
