digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
total = 0
f = open("aoc1.txt", "r")
lines = f.readlines()
for line in lines:
    count = -1
    line = line.strip()
    num = ""
    last = ""
    for char in line:
        count += 1
        if char in digits:
            if num == "":
                num = char
            last = char
        else:
            word = char
            for i in range(count + 1, len(line)):
                word += line[i]
                if word in words:
                    if num == "":
                        num = str(words.index(word))
                    last = str(words.index(word))
                    break
    num += last
    print(num)
    total += int(num)
print(total)
