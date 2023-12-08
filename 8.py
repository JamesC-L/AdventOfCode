instructions = ("LRLRRRLRRLRLRRRLRRLLRRRLRLRLRLRRLRRRLRRLLRLRLRRRLRLLRRLRRLRLLRRLLRRLRRRLLRRLRRLRRRLRRRLRRRLRLRRLRRRLLRRLRRLRRRLRLRRRLRRLRRRLRRRLRLRLRLRLRLRLLRRLLLLRLRRRLRRRLLRRLRLRLLRRRLRLRRLRRRLLLLRRRLLRRLRRLRRLLRLLLLRLRRRLRLRRLRRLLRRRLRRLRLRRLRRRLLRRRLLRLRRLRRLLRRRLLRLRRLRLRRLLLRRRR")
instructs = []
for instruction in instructions:
    instructs.append(instruction)

f = open("aoc8.txt", "r")
lines = f.readlines()
nodes = []
edges = []

for line in lines:
    line = line.strip()
    line = line.split(" = (")
    node = line[0]
    edge = line[1]
    edge = edge[0:8]
    edge = edge.split(", ")
    nodes.append(node)
    edges.append(edge)

found = False
steps = 0
count = -1
currentNodes = []
for node in nodes:
    if node[2] == "A":
        currentNodes.append(node)
while not found:
    # for node in currentNodes:
    #     print(node, edges[nodes.index(node)][0], edges[nodes.index(node)][1])
    steps += 1
    count += 1
    if count >= len(instructs):
        count = 0
    if instructs[count] == "L":
        i = -1
        for node in currentNodes:
            i += 1
            currentNodes[i] = edges[nodes.index(node)][0]
    else:
        i = -1
        for node in currentNodes:
            i += 1
            currentNodes[i] = edges[nodes.index(node)][1]
    done = True
    for node in currentNodes:
        if node[2] != "Z":
            done = False
        if node[2] == "Z":
            print(steps)
            
    if done:
        print(steps)
        found = True




