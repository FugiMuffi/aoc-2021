def main(find_last: bool):
    with open("input.txt") as f:
        draw = f.readline().strip().split(',')
        f.readline()

        boards = [[b.split() for b in a.split('\n')] for a in ''.join(f.readlines()).split('\n\n')]

        for num in draw:
            boards = [[[("" if cell == num else cell) for cell in row] for row in board] for board in boards]

            for board in boards[:]:
                if ['' for n in range(5)] in board + [[cell for row in board for cell in row][i::5] for i in range(5)]:
                    if not find_last or len(boards) == 1:
                        return int(num) * sum([int(cell) for row in board for cell in row if cell != ""])
                    boards.remove(board)


if __name__ == "__main__":
    print(main(find_last=False))
    print(main(find_last=True))
