import collections, itertools

def main(include_diagonals: bool):
    with open("input.txt") as f:
        return len((lambda l: [item for item, count in collections.Counter(l).items() if count > 1])([val for sublist in [list(itertools.zip_longest((lambda a, b: range(a, b+1) if a <= b else range(a, b-1, -1))(line[0][1], line[1][1]), (lambda a, b: range(a, b+1) if a <= b else range(a, b-1, -1))(line[0][0], line[1][0]), fillvalue=(line[0][0] if line[0][0]==line[1][0] else line[0][1]))) for line in [[[int(y) for y in x.split(',')] for x in row.strip().split(' -> ')] for row in f] if line[0][0]==line[1][0] or line[0][1]==line[1][1] or include_diagonals] for val in sublist]))

if __name__ == "__main__":
    print(main(include_diagonals=False))
    print(main(include_diagonals=True))
