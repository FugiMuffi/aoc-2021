def game_deterministic(p1, p2):
    score_p1 = 0
    score_p2 = 0

    die = 1
    die_ctr = 0

    while score_p1 < 1000 and score_p2 < 1000:
        if die_ctr % 2:
            p2 = (p2 + 3*die+3 - 1) % 10 + 1
            score_p2 += p2
        else:
            p1 = (p1 + 3*die+3 - 1) % 10 + 1
            score_p1 += p1

        die = (die + 3 - 1) % 100 + 1
        die_ctr += 3

    return min(score_p1, score_p2) * die_ctr


def game_dirac(p1, p2, score_p1=0, score_p2=0, states={}):
    if score_p1 >= 21:
        return (1,0)
    if score_p2 >= 21:
        return (0,1)

    if (p1, p2, score_p1, score_p2) in states:
        return states[(p1, p2, score_p1, score_p2)]

    if score_p1 < 21 and score_p2 < 21:
        res = (0,0)

        for die in [a+b+c for a in [1,2,3] for b in [1,2,3] for c in [1,2,3]]:
            tmp_p1 = (p1 + die - 1) % 10 + 1
            tmp_score_p1 = score_p1 + tmp_p1

            w1,w2 = game_dirac(p2, tmp_p1, score_p2, tmp_score_p1, states)
            res = (res[0]+w2, res[1]+w1)

        states[(p1, p2, score_p1, score_p2)] = res
        return res


def main():
    with open("input.txt") as f:
        p1, p2 = [int(x.strip()[-1:]) for x in f]

    print(game_deterministic(p1, p2))

    print(max(game_dirac(p1, p2)))


if __name__ == "__main__":
    main()
