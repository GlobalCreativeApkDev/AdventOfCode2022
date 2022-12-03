def main():
    file1 = open('day2/input.txt', 'r')
    lines = file1.readlines()
    total_score: int = 0
    for line in lines:
        curr: str = line.split("\n")[0]
        p1: str = curr.split(" ")[0]
        p2: str = curr.split(" ")[1]
        if p1 == "A" and p2 == "X":
            total_score += 3
        elif p1 == "A" and p2 == "Y":
            total_score += 4
        elif p1 == "A" and p2 == "Z":
            total_score += 8
        elif p1 == "B" and p2 == "X":
            total_score += 1
        elif p1 == "B" and p2 == "Y":
            total_score += 5
        elif p1 == "B" and p2 == "Z":
            total_score += 9
        elif p1 == "C" and p2 == "X":
            total_score += 2
        elif p1 == "C" and p2 == "Y":
            total_score += 6
        else:
            total_score += 7

    print("Day 2b: " + str(total_score))


if __name__ == '__main__':
    main()
