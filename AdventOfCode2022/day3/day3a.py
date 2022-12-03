LETTERS: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_priority(letter: str) -> int:
    for i in range(len(LETTERS)):
        if LETTERS[i] == letter:
            return i + 1
    return -1


def common(first: str, second: str) -> str:
    res: str = ""  # initial value
    for c in first:
        if c in second and c not in res:
            res += c

    return res


def main():
    file1 = open('day3/input.txt', 'r')
    lines = file1.readlines()
    total_priority: int = 0  # initial value
    for line in lines:
        curr: str = line.split("\n")[0]
        half: int = int(round(len(curr)) / 2)
        first: str = curr[0:half]
        second: str = curr[half::]
        in_both: str = common(first, second)
        total_priority += sum(get_priority(l) for l in in_both)

    print("Day 3a: " + str(total_priority))


if __name__ == '__main__':
    main()
