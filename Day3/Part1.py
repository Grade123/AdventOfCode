

with open("Day3/input.txt", "r") as f:
    lines = f.readlines()
    
    sum = 0

    for line in lines:
        line = line.removesuffix("\n")
        numberOfItems = len(line)

        compartment1 = line[0:numberOfItems//2]
        compartment2 = line[numberOfItems//2:]

        checked = ""
        for item in compartment1:
            if item in compartment2 and not item in checked:
                sum += 26 if item.isupper() else 0
                sum += ord(item.upper()) - 64
                checked += item

    print(sum)
