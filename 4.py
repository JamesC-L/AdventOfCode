f = open("aoc4.txt", "r")
lines = f.readlines()
total = 0
totalCards = 0
currentCard = 0
numberOfCards = [1 for i in range(300)]
for line in lines:
    winners = 0
    currentCard += 1
    line = line.strip()
    line = line.split(": ")
    cards = line[1]
    cards = cards.split(" | ")
    winning = cards[0]
    card = cards[1]
    winningNumbers = winning.split(" ")
    numbers = card.split(" ")
    for num in winningNumbers:
        if num == "":
            winningNumbers.remove(num)
    for num in numbers:
        if num == "":
            numbers.remove(num)
    for number in numbers:
        if number in winningNumbers:
            winners += 1

    print(currentCard, numberOfCards[currentCard], winners)
    count = 0
    for i in range(winners):
        count += 1
        numberOfCards[currentCard + count] += numberOfCards[currentCard]

    
    # if winners != -1:
    #     score = 2 ** (winners)
    #     total += score
    # print(score)
    

#print(total)
numberOfCards[0] = 0
for i in range(209, len(numberOfCards)):
    numberOfCards[i] = 0
print(sum(numberOfCards))