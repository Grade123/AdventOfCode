

with open('Day1/input.txt', "r") as file:
    lines = file.readlines()

    first = 0
    second = 0
    third = 0

    sum = 0

    for line in lines:
        if line == "\n":
            
            if sum > first:
                first = sum
            elif sum > second:
                second = sum
            elif sum > third:
                third = sum
            sum = 0
        else:
            sum += int(line)

    print(first+second+third)