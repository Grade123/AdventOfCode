def parseDictionary(lines):
    root = {}

    stack = []
    head = root

    for line in lines:
        line = line.removesuffix("\n")

        if line[0] == "$":
            command = line[2:4]
            value = line[5:]

            if command == "cd":
                if value == "..":
                    head = stack.pop()
                elif value == "/":
                    stack = []
                    head = root
                else:
                    if value in head:
                        stack.append(head)
                        head = head[value]

        elif line[0:3] == "dir":
            value = line[4:]
            head[value] = head[value] if value in head else {}
        else:
            parts = line.split(" ")
            head[parts[1]] = int(parts[0])


    return root

with open("Day7/input.txt") as f:
    lines = f.readlines()

    dictionary = parseDictionary(lines)

    dicts = []

    def sum(head):
        value = 0
        for item in head:
            if type(head[item]) == dict:
                dictValue = sum(head[item])
                dicts.append([item, dictValue])
                value += dictValue
            else:
                value += head[item]

        return value

    def sortSecond(val):
        return val[1]

    subSum = 0

    for i in dicts:
        if i[1] <= 100000:
            subSum += i[1]

    print(subSum)