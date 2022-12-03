LETTERS: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_priority(letter: str) -> int:
    for i in range(len(LETTERS)):
        if LETTERS[i] == letter:
            return i + 1
    return -1


def common(first: str, second: str, third: str) -> str:
    res: str = ""  # initial value
    for c in first:
        if c in second and c in third and c not in res:
            res += c

    return res


def main():
    file1 = open('day3/input.txt', 'r')
    lines = file1.readlines()
    total_priority: int = 0  # initial value
    first: str = ""
    second: str = ""
    third: str = ""
    for i in range(len(lines)):
        line: str = lines[i].split("\n")[0]
        if i % 3 == 0:
            first = line
        elif i % 3 == 1:
            second = line
        else:
            third = line
            in_all: str = common(first, second, third)
            total_priority += sum(get_priority(l) for l in in_all)

    print("Day 3b: " + str(total_priority))


if __name__ == '__main__':
    main()
