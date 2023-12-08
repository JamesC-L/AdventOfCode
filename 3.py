f = open("aoc3.txt", "r")
lines = f.readlines()
total = 0
notSymbols = [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

grid = [["_" for i in range(140)]for j in range(140)]
row = -1
for line in lines:
    row += 1
    line = line.strip()
    column = 0
    for char in line:
        grid[row][column] = char
        column += 1


asterisks = 0
row = -1
for line in lines:
    row += 1
    column = -1
    line = line.strip()
    while column < 139:
        column += 1
        char = grid[row][column]
        if char == "*":
            asterisks += 1
        if char in nums:
            startx = row
            starty = column + 1
            num = char
            while char in nums and column < 139:
                column += 1
                char = grid[row][column]
                if char in nums:
                    num += char
            if column - len(num) - 1 > 0:
                leftBound = column - len(num) - 1
            else:
                leftBound = 0
            if column < 139:
                rightBound = column
            else:
                rightBound = 139
            if row != 0:
                upperBound = row - 1
            else:
                upperBound = 0
            if row != 139:
                lowerBound = row + 1
            else:
                lowerBound = 139
            found = False
            for i in range(upperBound, lowerBound + 1):
                for j in range(leftBound, rightBound + 1):
                    if grid[i][j] not in notSymbols and not found:
                        found = True
                        total += int(num)


print(asterisks)