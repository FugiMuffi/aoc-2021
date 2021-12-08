def main():
    with open("input.txt") as f:
        lines = [[y.split() for y in x.strip().split(" | ")] for x in f]

        # part 1
        print(len([y for x in [x[1] for x in lines] for y in x if len(y) in [2,3,4,7]]))

        # part 2
        s = 0

        for line in lines:
            # analyze code
            alphabet = [set(x) for x in line[0]]

            digits = {
                1: [x for x in alphabet if len(x) == 2][0],
                4: [x for x in alphabet if len(x) == 4][0],
                7: [x for x in alphabet if len(x) == 3][0],
                8: set("abcdefg"),
            }

            code = dict()
            code['t'] = digits[7] - digits[1]

            for x in digits[8] - digits[4] - code['t']:
                pos_digit = digits[4] | code['t'] | set(x)
                if pos_digit in alphabet:
                    code['b'] = set(x)
                    digits[9] = pos_digit
                else:
                    code['bl'] = set(x)

            for x in digits[1]:
                pos_digit = digits[8] - set(x)
                if pos_digit in alphabet:
                    code['tr'] = set(x)
                    digits[6] = pos_digit
                else:
                    code['br'] = set(x)

            for x in digits[4] - digits[7]:
                pos_digit = digits[1] | code['t'] | code['b'] | set(x)
                if pos_digit in alphabet:
                    code['c'] = set(x)
                    digits[3] = pos_digit
                else:
                    code['tl'] = set(x)

            digits[2] = digits[3] - code['br'] | code['bl']

            digits[5] = digits[3] - code['tr'] | code['tl']

            digits[0] = digits[8] - code['c']

            # decode output
            s += int(''.join(map(str,[list(digits.keys())[list(digits.values()).index(set(x))] for x in line[1]])))

        print(s)


if __name__ == "__main__":
    main()
