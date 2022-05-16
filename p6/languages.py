from programming_language import ProgrammingLanguage
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(ruby, python, visual_basic)
print("The dynamically typed languages are:")
Languages = [ruby, python, visual_basic]

for each in Languages:
    if ProgrammingLanguage.is_dynamic(each):
        print(each.field)
