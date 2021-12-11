def main():
    with open("input.txt") as f:
        lines = [x.strip() for x in f]

        brackets = {
            '(': ')',
            '[': ']',
            '{': '}',
            '<': '>',
        }

        score_table = {
            ')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137,
            '(': 1,
            '[': 2,
            '{': 3,
            '<': 4,
        }

        score_1 = 0
        scores_2 = []

        for line in lines:
            stack = []
            score_2 = 0

            for c in line:
                if c in brackets:
                    stack.append(c)
                elif brackets[stack[-1]] == c:
                    stack.pop()
                else:
                    # print(f'Expected {brackets[stack[-1]]}, but found {c} instead.')
                    score_1 += score_table[c]
                    stack = []
                    break

            if len(stack) > 0:
                # print(f'Line is incomplete.')
                for c in reversed(stack):
                    score_2 *= 5
                    score_2 += score_table[c]
                scores_2.append(score_2)

        print(score_1, sorted(scores_2)[len(scores_2)//2])


if __name__ == "__main__":
    main()
