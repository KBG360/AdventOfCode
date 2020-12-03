import numpy as np
a_file = open("input.txt")
file_contents = a_file.read()
funnyList = file_contents.splitlines()
numbers = np.array(funnyList)

for x in range(len(numbers)):
    for y in range(len(numbers)):
        for z in range(len(numbers)):
            if int(numbers[x]) + int(numbers[y]) + int(numbers[z]) == 2020:
                print(int(numbers[x]) * int(numbers[y]) * int(numbers[z]))
                break
