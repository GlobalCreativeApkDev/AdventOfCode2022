def main():
    file1 = open('day4/input.txt', 'r')
    lines = file1.readlines()
    full_contain: int = 0  # initial value
    for line in lines:
        curr: str = line.split("\n")[0]
        words: list = curr.split(",")
        word1: str = words[0]
        word2: str = words[1]
        start1: int = int(word1.split("-")[0])
        end1: int = int(word1.split("-")[1])
        start2: int = int(word2.split("-")[0])
        end2: int = int(word2.split("-")[1])
        if (start1 <= start2 and end1 >= end2) or (start2 <= start1 and end2 >= end1):
            full_contain += 1

    print("Day 4a: " + str(full_contain))


if __name__ == '__main__':
    main()
