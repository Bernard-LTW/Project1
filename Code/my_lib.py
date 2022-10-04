# This is where I put useful functions that I use in my scripts
import datetime

colors = ["\033[0;30m", "\033[0;31m", "\033[0;32m", "\033[0;33m", "\033[0;34m", "\033[0;35m", "\033[0;36m",
          "\033[0;37m", "\033[0;38m", "\033[0;39m", "\033[0;40m", "\033[0;41m", "\033[0;42m", "\033[0;43m",
          "\033[0;44m", "\033[0;45m", "\033[0;46m", "\033[0;47m", "\033[0;48m", "\033[0;49m", "\033[0;50m",
          "\033[0;51m", "\033[0;52m", "\033[0;53m", "\033[0;54m", "\033[0;55m", "\033[0;56m", "\033[0;57m",
          "\033[0;58m", "\033[0;59m", "\033[0;60m", "\033[0;61m", "\033[0;62m", "\033[0;63m", "\033[0;64m",
          "\033[0;65m", "\033[0;66m", "\033[0;67m", "\033[0;68m", "\033[0;69m", "\033[0;70m", "\033[0;71m",
          "\033[0;72m", "\033[0;73m", "\033[0;74m", "\033[0;75m", "\033[0;76m", "\033[0;77m", "\033[0;78m",
          "\033[0;79m", "\033[0;80m", "\033[0;81m", "\033[0;82m", "\033[0;83m", "\033[0;84m", "\033[0;85m",
          "\033[0;86m", "\033[0;87m", "\033[0;88m", "\033[0;89m", "\033[0;90m", "\033[0;91m", "\033[0;92m"]
end_code = "\033[00m"

def author():
    return "Bernard Lee"


def validate_int_input(prompt: str):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def banner(msg: str):
    header_line = "=" * 100
    space_line = "#" + " " * 98 + "#"
    return header_line + "\n" + space_line + "\n" + "#" + msg.center(98) + "#" + "\n" + space_line + "\n" + header_line


def validate_float_input(prompt: str):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def validate_date_input(prompt: str):
    while True:
        try:
            return datetime.datetime.strptime(input(prompt), '%Y-%m-%d')
        except ValueError:
            print(f"{colors[1]}Incorrect data, should be YYYY-MM-DD{end_code}")


'''
import my_library

print(my_library.author())

age = my_library.validate_int_input("Input your age: ")
height = my_library.validate_int_input("Input your height: ")
weight = my_library.validate_int_input("Input your weight: ")
print(f"You graduate high school in {2022 - age + 18}.")

print(my_library.banner("BMI Calculator"))

bmi = weight / (height / 100) ** 2
print(f"Your BMI is {bmi:.2f}.")

Floatin = my_library.validate_float_input("Input a float: ")
'''
