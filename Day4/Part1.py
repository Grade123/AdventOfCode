with open("Day4/input.txt", "r") as f:
    lines = f.readlines()
    
    numberOfOverlaps = 0

    for line in lines:
        line = line.removesuffix("\n")
        assignments = line.split(",")

        elf1Assignment = [int(camp) for camp in assignments[0].split("-")]
        elf2Assignment = [int(camp) for camp in assignments[1].split("-")]

        if elf1Assignment[0] <= elf2Assignment[0] and elf1Assignment[1] >= elf2Assignment[1]:
            numberOfOverlaps += 1
        elif elf1Assignment[0] >= elf2Assignment[0] and elf1Assignment[1] <= elf2Assignment[1]:
            numberOfOverlaps += 1

    print(numberOfOverlaps)
