
with open("Day6/input.txt", "r") as f:
    lines = f.readlines()

    for line in lines:
        line = line.removesuffix("\n")
        searches = len(line) - 3

        for n in range(searches):
            searchWord = line[n:n+4]
            searched = ""

            for char in searchWord:
                if char in searched:
                    break
                searched += char

            if len(searched) == 4:
                print(searched, n + 4)
                break
