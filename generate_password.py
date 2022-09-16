import random
name = input('What is your name?\n')
without_spaces_name = name.replace(" ", "").lower()
password = ""
for i in range(3):
    randomStr = random.choice(without_spaces_name)
    password += randomStr
for i in range(4):
    randomInt = random.randint(0, 9)
    password += str(randomInt)

print(password)

