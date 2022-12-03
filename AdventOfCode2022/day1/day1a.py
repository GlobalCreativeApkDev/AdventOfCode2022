def main():
    file1 = open('day1/input.txt', 'r')
    lines = file1.readlines()
    totals: list = []
    curr_total: int = 0
    for line in lines:
        curr: str = line.split("\n")[0]
        if len(curr) == 0:
            totals.append(curr_total)
            curr_total = 0
        else:
            curr_total += int(curr)

    print("Day 1a: " + str(max(totals)))


if __name__ == '__main__':
    main()
