f = open("aoc5.txt", "r")
lines = f.readlines()
for line in lines:
    line = line.strip()
seeds = lines[0].split(" ")
seeds.pop(0)
soils = []
for i in range(3, 16):
    soils.append(lines[i])
ferts = []
for i in range(18, 39):
    ferts.append(lines[i])
waters = []
for i in range(41, 89):
    waters.append(lines[i])
lights = []
for i in range(91, 130):
    lights.append(lines[i])
temps = []
for i in range(132, 148):
    temps.append(lines[i])
humids = []
for i in range(150, 157):
    humids.append(lines[i])
locs = []
for i in range(159, 190):
    locs.append(lines[i])


def bob(value, big):
    found = False
    for small in big:
        small = small.strip()
        small = small.split(" ")
        for i in range(0, 3):
            small[i] = int(small[i])
        if value >= small[1] and value < small[1] + small[2]:
            found = True
            dist = value - small[1]
            newValue = small[0] + dist
    if not found:
        newValue = value
    return newValue


values = []
count = -1
currentMin = 0
for i in range(1):
    count += 1
    start = int(seeds[count])
    count += 1
    r = int(seeds[count])
    for i in range(3876934551 - 20000, 3876934551 + 20000, 1):
        #seed = seed.strip()
        #value = int(seed)
        value = i
        result = [value]
        value = bob(value, soils)
        result.append(value)
        value = bob(value, ferts)
        result.append(value)
        value = bob(value, waters)
        result.append(value)
        value = bob(value, lights)
        result.append(value)
        value = bob(value, temps)
        result.append(value)
        value = bob(value, humids)
        result.append(value)
        value = bob(value, locs)
        result.append(value)
        values.append(value)
        if min(values) != currentMin:
            print(i)
            currentMin = min(values)
print(min(values), values.index(min(values)))