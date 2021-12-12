def main():
    with open("input.txt") as f:
        edges = set([tuple(x.strip().split('-')) for x in f])

        vertices = set([a for b in edges for a in b])

        adjacencyDict = {v: set() for v in vertices}
        for (v1, v2) in edges:
            adjacencyDict[v1].add(v2)
            adjacencyDict[v2].add(v1)

        # part 1
        print(len(traverse1(adjacencyDict, 'start')))

        # part 2
        print(len(traverse2(adjacencyDict, 'start')))


def traverse1(adj, vert, path=[]):

    if vert == 'end':
        return [path + ['end']]

    paths = []

    for neighbor in adj[vert] - set([x for x in path if x.islower()]):
        paths += traverse1(adj, neighbor, list(path + [vert]))

    return paths


def traverse2(adj, vert, path=[]):

    if vert == 'end':
        return [path + ['end']]

    paths = []

    path_lower = [x for x in path if x.islower()] + [vert]

    for neighbor in list(adj[vert]):
        if neighbor == 'start':
            continue

        if neighbor not in path_lower or len(set(path_lower)) == len(path_lower):
            paths += traverse2(adj, neighbor, list(path + [vert]))

    return paths


if __name__ == "__main__":
    main()
