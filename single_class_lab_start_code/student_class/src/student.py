from unicodedata import name

class Student:

    def __init__(self, input_name, input_cohort):
        self.name = input_name
        self.cohort = input_cohort

    def update_name(name):
        self.name = name


    def update_cohort(cohort):
        self.cohort = cohort

    def talk(self):
        return "I can talk!"

    def say_favourite_language(self, language):
        return f"I love {language}"