times = [55,99,97,93]
distances = [401,1485,2274,1405]
total = 1
for i in range(0, 4):
    winners = 0
    for j in range(1, times[i] + 1):
        if (times[i] - j) * j > distances[i]:
            winners += 1
    total *= winners

print(total)

time = 55999793
distance = 401148522741405
total = 0
found = False
for i in range(47487001, 47587001, 1):
    if i * (time - i) > distance: 
        print(i)
        if not found:
            print(f"first = {i}")
            print("e")

        found = True
        total += 1
    else:
        if found:
            print(f"last = {i}")
            print(total)
            break