

def ParseStacks(data: list[str]):
    stacks = []
    for stack in data:
        stack = stack.removesuffix("\n")
        stacks.append([x for x in stack])

    return stacks

def ParseMoves(data: list[str]):
    moves = []
    for move in data:
        move = move.removesuffix("\n")
        parts = move.split(" ")
        moves.append([int(parts[1]), int(parts[3]), int(parts[5])])
    
    return moves

Stacks = []
Moves = []

with open("Day5/stacks.txt", "r") as s:
    Stacks = ParseStacks(s.readlines())
with open("Day5/moves.txt", "r") as m:
    Moves = ParseMoves(m.readlines())

print(Stacks)

for move in Moves:
    for n in range(move[0]):
        Stacks[move[2] - 1].append(Stacks[move[1] - 1].pop())

for s in Stacks:
    print(s[-1])      
