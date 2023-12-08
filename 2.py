f = open("aoc2.txt", "r")
lines = f.readlines()
total = 0
for line in lines:
    line = line.strip()
    line = line.split(": ")
    game = line[0]
    game = game.split(" ")
    id = int(game[1])
    draws = line[1]
    draws = draws.split("; ")
    #possible = True
    maxRed = 0
    maxBlue = 0
    maxGreen = 0
    for draw in draws:
        draw = draw.split(", ")
        for cube in draw:
            cube = cube.split(" ")
            num = int(cube[0])
            match cube[1]:
                case "red":
                    if num > maxRed:
                        #possible = False
                        maxRed = num
                case "blue":
                    if num > maxBlue:
                        #possible = False
                        maxBlue = num
                case "green":
                    if num > maxGreen:
                        #possible = False
                        maxGreen = num
    power = maxRed * maxBlue * maxGreen
    print(power)
    total += power

print(total)



    