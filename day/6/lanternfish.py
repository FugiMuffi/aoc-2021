from collections import Counter

def sim(days: int):
    with open("input.txt") as f:

        ctr = Counter([int(x) for x in f.readline().split(',')])
        fish = [ctr[n] for n in range(9)]

        for _ in range(days):
            spawn = fish.pop(0)
            fish[6] += spawn
            fish.append(spawn)

        return sum(fish)

if __name__ == "__main__":
    for days in [80, 256]:
        print(sim(days))
