def all_letters_different(string: str):
    a_list: list = []  # initial value
    for s in string:
        if s in a_list:
            return False
        a_list.append(s)

    return True


def main():
    file1 = open('day6/input.txt', 'r')
    lines = file1.readlines()
    line: str = lines[0].split("\n")[0]
    marker_index: int = -1  # initial value
    for i in range(len(line) - 4):
        if all_letters_different(line[i:i+4]):
            marker_index = i + 4
            break

    print("Day 6a: " + str(marker_index))


if __name__ == '__main__':
    main()
