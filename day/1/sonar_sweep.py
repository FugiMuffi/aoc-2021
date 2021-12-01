def part1():
    with open('input.txt') as file:
        last = int(file.readline())
        counter = 0

        for line in file:
            current = int(line)
            if (current > last):
                counter += 1
            last = current

        print(counter)

def part2():
    with open('input.txt') as file:
        l = file.readlines()
        last = None
        counter = 0

        for prev, cur, nxt in zip(l, l[1:], l[2:]):
            s = int(prev) + int(cur) + int(nxt)
            if last is not None and s > last:
                counter += 1
            last = s

        print(counter)

if __name__ == "__main__":
    part1()
    part2()
