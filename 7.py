f  =open("aoc7.txt", "r")
lines = f.readlines()
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
fives = []
fours = []
fulls = []
threes = []
twopairs = []
onepairs = []
highs = []
total = 0

def listerise(string):
    list = []
    for char in string:
        if char == "A":
            char = "F"
        elif char == "K":
            char = "E"
        elif char == "Q":
            char = "D"
        elif char == "J":
            char = ")"
        elif char == "T":
            char = "B"
        list.append(char)
    return list

for line in lines:
    line = line.strip()
    line = line.split(" ")
    hand = line[0]
    bid = line[1]
    appearances = []
    result = hand + " " + bid
    jokers = hand.count("J")
    for card in cards:
        appearances.append(hand.count(card))
    egg = [0, 0, 0, 0]
    for appearance in appearances:
        if appearance == 2:
            egg[0] += 1
        elif appearance == 3:
            egg[1] += 1
        elif appearance == 4:
            egg[2] += 1
        elif appearance == 5:
            egg[3] += 1
    for i in range(jokers):
        if egg[2] != 0:
            egg[2] -= 1
            egg[3] += 1
        elif egg[1] != 0:
            egg[1] -= 1
            egg[2] += 1
        elif egg[0] != 0:
            egg[0] -= 1
            egg[1] += 1
        else:
            egg[0] += 1
    if egg[3] == 1:
        fives.append(result)
        print(f"{hand}: Five")
    elif egg[2] == 1:
        fours.append(result)
        print(f"{hand}: Four")
    elif egg[0] == 1 and egg[1] == 1:
        fulls.append(result)
        print(f"{hand}: Full House")
    elif egg[1] == 1:
        threes.append(result)
        print(f"{hand}: Three")
    elif egg[0] == 2:
        twopairs.append(result)
        print(f"{hand}: Two Pair")
    elif egg[0] == 1:
        onepairs.append(result)
        print(f"{hand}: Pair")
    else:
        highs.append(result)
        print(f"{hand}: None")



order = []
highs2 = []
for five in highs:
    five = listerise(five)
    highs2.append(five)
pairs2 = []
for five in onepairs:
    five = listerise(five)
    pairs2.append(five)
twopairs2 = []
for five in twopairs:
    five = listerise(five)
    twopairs2.append(five)
threes2 = []
for five in threes:
    five = listerise(five)
    threes2.append(five)
fulls2 = []
for four in fulls:
    four = listerise(four)
    fulls2.append(four)
fours2 = []
for four in fours:
    four = listerise(four)
    fours2.append(four)
fives2 = []
for five in fives:
    five = listerise(five)
    fives2.append(five)


highs2.sort()
for hand in highs2:
    order.append(hand)
pairs2.sort()
for hand in pairs2:
    order.append(hand)
twopairs2.sort()
for hand in twopairs2:
    order.append(hand)
threes2.sort()
for hand in threes2:
    order.append(hand)
fulls2.sort()
for hand in fulls2:
    order.append(hand)
fours2.sort()
for hand in fours2:
    order.append(hand)
fives2.sort()
for hand in fives2:
    order.append(hand)

count = 0
for hand in order:
    count += 1
    origHand = ""
    for char in hand:
        origHand += char
    origHand = origHand.split(" ")
    
    bid = origHand[1]
    total += count * int(bid)
    print(origHand[0], count, count * int(bid))
    if origHand == ")))))":
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAA")

print(total)