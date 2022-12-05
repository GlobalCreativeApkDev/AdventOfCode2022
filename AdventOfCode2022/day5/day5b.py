def main():
    file1 = open('day5/input.txt', 'r')
    lines = file1.readlines()
    stacks: list = [[], [], [], [], [], [], [], [], []]
    count: int = 0
    for line in lines:
        count += 1
        curr: str = line.split("\n")[0]
        if count < 9:
            for i in range(len(curr)):
                if (i - 1) % 4 == 0 and curr[i] != " ":
                    stacks[(i - 1) // 4].append(curr[i])
        elif count > 10:
            words: list = curr.split(" ")
            amount: int = int(words[1])
            num_from: int = int(words[3])
            num_to: int = int(words[5])
            for i in range(amount - 1, -1, -1):
                if len(stacks[num_from - 1]) == 0:
                    break

                curr: str = stacks[num_from - 1][i]
                stacks[num_from - 1].pop(i)
                stacks[num_to - 1].insert(0, curr)
        else:
            pass  # do nothing

    result: str = ""  # initial value
    for s in stacks:
        result += s[0]

    print("Day 5b: " + str(result))


if __name__ == '__main__':
    main()
