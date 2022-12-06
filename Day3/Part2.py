

with open("Day3/input.txt", "r") as f:
    lines = f.readlines()
    numberOfGroups = len(lines)//3

    sum = 0

    for groupNumber in range(numberOfGroups):
        elf1 = lines[(groupNumber * 3) - 3]
        elf2 = lines[(groupNumber * 3) - 2]
        elf3 = lines[(groupNumber * 3) - 1]

        for item in elf1:
            if item in elf2 and item in elf3:
                sum += 26 if item.isupper() else 0
                sum += ord(item.upper()) - 64
                break
                

    print(sum)
