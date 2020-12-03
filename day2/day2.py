import re
a_file = open("input.txt")
file_contents = a_file.read()
inputList = file_contents.splitlines()
firstCount = 0
secondCount = 0

for x in inputList:
    letterRange = re.findall("\d+", x)
    minimum = int(letterRange[0])
    maximum = int(letterRange[1])
    password = x.split(": ")[1]
    temp = x.split(" ")
    letter = temp[1].split(":", 1)[0]
    if password.count(letter) >= minimum and password.count(letter) <= maximum:
        firstCount += 1

    if password[minimum - 1] == letter or password[maximum - 1] == letter:
        if not (password[minimum - 1] == letter and password[maximum - 1] == letter):
            secondCount += 1
                

print(firstCount)
print(secondCount)