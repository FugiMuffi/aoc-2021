def part1():
    with open('input.txt') as f:
        x = y = 0

        for line in f:
            instruction, amount = line.split(' ')

            if instruction == 'forward':
                x += int(amount)
            elif instruction == 'down':
                y += int(amount)
            elif instruction == 'up':
                y -= int(amount)
            else:
                raise Exception("impossible error")

        print(x*y)

def part2():
    with open('input.txt') as f:
        x = y = aim = 0

        for line in f:
            instruction, amount = line.split(' ')

            if instruction == 'forward':
                x += int(amount)
                y += int(amount) * aim
            elif instruction == 'down':
                aim += int(amount)
            elif instruction == 'up':
                aim -= int(amount)
            else:
                raise Exception("impossible error")

        print(x*y)

if __name__ == "__main__":
    part1()
    part2()
