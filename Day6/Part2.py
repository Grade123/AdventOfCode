
with open("Day6/input.txt", "r") as f:
    lines = f.readlines()

    for line in lines:
        line = line.removesuffix("\n")
        searches = len(line) - 13

        for n in range(searches):
            searchWord = line[n:n+14]
            searched = ""

            for char in searchWord:
                if char in searched:
                    break
                searched += char

            if len(searched) == 14:
                print(searched, n + 14)
                break
