class ProgrammingLanguage:
    def __init__(self, field, typing, reflection, year):
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.field},{self.typing},Reflection={self.reflection},First appeared in {self.year}"

    def is_dynamic(self):
        if self.typing == "Dynamic":
            is_dynamic = True
        else:
            is_dynamic = False
        return is_dynamic

    def __repr__(self):
        return self.__str__()




