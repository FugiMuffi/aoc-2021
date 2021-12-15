from collections import Counter

def main():
    with open("input.txt") as f:
        templ = f.readline().strip()
        f.readline()

        rules = {k: v for (k,v) in [x.strip().split(' -> ') for x in f]}

        ctr = Counter([templ[i:i+2] for i in range(len(templ)-1)])

        for i in range(40):
            ctr_tmp = Counter()
            for a,b in ctr.items():
                ctr_tmp[a[0]+rules[a]] += b
                ctr_tmp[rules[a]+a[1]] += b
            ctr = ctr_tmp

            if i+1 in [10, 40]:
                ctr_letters = Counter()
                for a,b in ctr.items():
                    ctr_letters[a[0]] += b
                ctr_letters[templ[-1]] += 1

                print((ctr_letters.most_common()[0][1] - ctr_letters.most_common()[-1][1]))



if __name__ == "__main__":
    main()
