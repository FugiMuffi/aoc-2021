def main():
    with open("input.txt") as f:
        tmp = f.read().split("\n\n")
        coords = [[int(b) for b in a.strip().split(',')] for a in tmp[0].split('\n')]
        folds = [(lambda b: [b[0], int(b[1])])(a.strip().split()[-1].split('=')) for a in tmp[1].split('\n')]

    sheet = (lambda x,y: [[0]*(max(x)+1) for _ in range(max(y)+1)])(*zip(*coords))
    for x,y in coords:
        sheet[y][x] = 1

    for i, (axis, at) in enumerate(folds):
        if axis == 'x':
            sheet = [[int(a or b) for a,b in zip(line[:at], list(reversed((list(line[at+1:]) + at*[0])[:at])))] for line in sheet]
        else:
            sheet = list(zip(*[[int(a or b) for a,b in zip(col[:at], list(reversed((list(col[at+1:]) + at*[0])[:at])))] for col in zip(*sheet)]))
        if i == 0:
            print(sum([sum(row) for row in sheet]))

    print()
    for line in sheet:
        for x in line: print('██' if x else '  ', end='')
        print()
    print()

if __name__ == "__main__":
    main()
