def main():
    file1 = open('day4/input.txt', 'r')
    lines = file1.readlines()
    overlaps: int = 0  # initial value
    for line in lines:
        curr: str = line.split("\n")[0]
        words: list = curr.split(",")
        word1: str = words[0]
        word2: str = words[1]
        start1: int = int(word1.split("-")[0])
        end1: int = int(word1.split("-")[1])
        start2: int = int(word2.split("-")[0])
        end2: int = int(word2.split("-")[1])
        if not (end1 < start2) and not (end2 < start1):
            overlaps += 1

    print("Day 4b: " + str(overlaps))


if __name__ == '__main__':
    main()
