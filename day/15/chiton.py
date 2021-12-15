import numpy as np

def main():
    with open("input.txt") as f:
        points = [[int (x) for x in line.strip()] for line in f]

    # part 1
    solve(points)

    # part 2
    points_array = np.array(points)
    points_array = np.concatenate([(np.array(points) + n - 1) % 9 + 1 for n in range(5)], axis=1)
    points_array = np.concatenate([(points_array + n - 1) % 9 + 1 for n in range(5)], axis=0)
    solve(points_array.tolist())


def solve(points):
    end = (len(points[0])-1, len(points)-1)

    def get_neighbors(x, y):
        neighbors = []
        if x > 0:
            neighbors.append((x-1,y))
        if x < end[0]:
            neighbors.append((x+1,y))
        if y > 0:
            neighbors.append((x,y-1))
        if y < end[1]:
            neighbors.append((x,y+1))

        return neighbors

    found = set()

    q = dict()
    q[(0,0)] = 0

    while len(q):
        if end in q:
            print(q[end])
            break

        x, y = min(q, key=q.get)
        path_sum = q[(x,y)]

        found.add((x,y))

        for xn, yn in get_neighbors(x, y):
            if (xn,yn) not in found and (xn,yn) not in q:
                q[(xn,yn)] = path_sum + points[yn][xn]

        del q[(x,y)]


if __name__ == "__main__":
    main()
