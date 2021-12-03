from collections import Counter

def part1():
    with open('input.txt') as f:
        lines = f.readlines()
        gamma = ""
        for i in range(len(lines[0])-1):
            gamma += Counter([x[i] for x in lines]).most_common(1)[0][0]

        epsilon = gamma.translate({ord('0'): '1', ord('1'): '0'})

        return int(gamma, 2) * int(epsilon, 2)

def part2():
    with open('input.txt') as f:
        lines = f.readlines()

        o2_lines = lines
        for i in range(len(lines[0])-1):
            if len(o2_lines) > 1:
                c = Counter([x[i] for x in o2_lines])
                crit = '1' if c['1'] == c['0'] else c.most_common(1)[0][0]
                o2_lines = [x for x in o2_lines if x[i] == crit]
            else:
                break

        co2_lines = lines
        for i in range(len(lines[0])-1):
            if len(co2_lines) > 1:
                c = Counter([x[i] for x in co2_lines])
                crit = '0' if c['1'] == c['0'] else c.most_common()[-1][0]
                co2_lines = [x for x in co2_lines if x[i] == crit]
            else:
                break

        return int(o2_lines[0], 2) * int(co2_lines[0], 2)

if __name__ == "__main__":
    print(part1())
    print(part2())
