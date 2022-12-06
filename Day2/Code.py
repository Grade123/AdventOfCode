Rock = 1
Paper = 2
Scissors = 3

Loss = 0
Draw = 3
Win = 6

with open('Day2/input.txt', "r") as file:
    lines = file.readlines()

    sum = 0

    for line in lines:
        tools = line[0:3].split(" ")
        mytool = ""

        if tools[1] == "X":
            sum += Loss
            sum += 3 if tools[0] == "A" else 1 if tools[0] == "B" else 2 if tools[0] == "C" else 0
        elif tools[1] == "Y":
            sum += Draw
            sum += 1 if tools[0] == "A" else 2 if tools[0] == "B" else 3 if tools[0] == "C" else 0
        elif tools[1] == "Z":
            sum += Win
            sum += 2 if tools[0] == "A" else 3 if tools[0] == "B" else 1 if tools[0] == "C" else 0
        
    print(sum)