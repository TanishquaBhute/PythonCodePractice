class Person:
    def __init__(self, name, surname, age, address, skills=[]):
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address
        self.skills = skills

    def info(self):

        print(f"{self.name} {self.surname} and age is {self.age} from {self.address}")

    def set_skills(self, skills):
        self.skills = skills
        print(f"Set skill: {self.skills}")

    def add_skills(self, new_skill):
        self.skills.append(new_skill)
        print(f"New skill is added and Your skills are {self.skills}")

    def print_skill(self):
        print(f"Parent skills: {self.skills}")
