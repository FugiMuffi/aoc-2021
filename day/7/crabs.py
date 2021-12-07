from statistics import median, mean

def main():
    with open("input.txt") as f:
        crabs = sorted([int(x) for x in f.readline().split(',')])

        # part 1
        med = int(median(crabs))
        fuel1 = sum([abs(med-x) for x in crabs])

        print(fuel1)

        # part 2
        avg = int(mean(crabs))
        fuel2 = sum([sum(range(abs(avg-x)+1)) for x in crabs])

        print(fuel2)

if __name__ == "__main__":
    main()
