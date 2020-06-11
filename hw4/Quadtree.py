import sys


class Quadrant:
    def __init__(self, depth, q1, q2, q3, q4):
        self.depth = depth
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4


# open and read input
# f = open(sys.argv[1], "r")

input = input()

if (len(input) == 1):
    print(input)
    exit()

i = 0
depth = 0
maxDepth = 0


def createQuadrant():
    global i
    global depth
    global maxDepth

    children = []

    while (i < len(input) - 1 and len(children) < 4):
        i += 1

        if (input[i] != "+"):
            children.append(input[i])

        else:
            depth += 1

            if (depth > maxDepth):
                maxDepth = depth

            children.append(createQuadrant())

    q = Quadrant(depth, children[0], children[1], children[2], children[3])
    depth -= 1

    return q


def quadrantToArray(startCol, startRow, q):
    global printArr
    global printSize

    if (type(q.q1) is not str):
        quadrantToArray(startCol, startRow, q.q1)
    else:
        for row in range(2 ** (maxDepth - q.depth)):
            for col in range(2 ** (maxDepth - q.depth)):
                printArr[startRow + row][startCol + col] = q.q1

    if (type(q.q2) is not str):
        quadrantToArray(startCol + 2 ** (maxDepth - q.depth), startRow, q.q2)
    else:
        for row in range(2 ** (maxDepth - q.depth)):
            for col in range(2 ** (maxDepth - q.depth)):
                printArr[startRow + row][startCol + 2 ** (maxDepth - q.depth) + col] = q.q2

    if (type(q.q3) is not str):
        quadrantToArray(startCol + 2 ** (maxDepth - q.depth), startRow + 2 ** (maxDepth - q.depth), q.q3)
    else:
        for row in range(2 ** (maxDepth - q.depth)):
            for col in range(2 ** (maxDepth - q.depth)):
                printArr[startRow + 2 ** (maxDepth - q.depth) + row][startCol + 2 ** (maxDepth - q.depth) + col] = q.q3

    if (type(q.q4) is not str):
        quadrantToArray(startCol, startRow + 2 ** (maxDepth - q.depth), q.q4)
    else:
        for row in range(2 ** (maxDepth - q.depth)):
            for col in range(2 ** (maxDepth - q.depth)):
                printArr[startRow + 2 ** (maxDepth - q.depth) + row][startCol + col] = q.q4


qt = createQuadrant()
printSize = (2 ** maxDepth) * 2
printArr = [["" for i in range(printSize)] for j in range(printSize)]
quadrantToArray(0, 0, qt)

for i, dummy in enumerate(printArr, start=0):
    for j, dummy2 in enumerate(dummy, start=0):
        print(printArr[i][j], end='')
    print("\n", end='')