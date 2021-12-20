import json, re, math, itertools


def depth(l):
    if isinstance(l, list):
        return 1 + max(depth(item) for item in l)
    else:
        return 0

def magnitude(l):
    if isinstance(l, list):
        return 3 * magnitude(l[0]) + 2 * magnitude(l[1])
    else:
        return l

def snail_sum(s1, s2):
    tmp_sum = [s1, s2]

    # reduce
    while True:
        # explode
        if depth(tmp_sum) > 4:
            tmp = re.findall("(\D+|\d+)", json.dumps(tmp_sum))
            level = 0
            for i, s in enumerate(tmp):
                level += s.count('[') - s.count(']')

                if level > 4:
                    if i-1 > 0:
                        tmp[i-1] = str(int(tmp[i-1]) + int(tmp[i+1]))
                    if i+5 < len(tmp):
                        tmp[i+5] = str(int(tmp[i+5]) + int(tmp[i+3]))

                    tmp[i] = tmp[i][:-1]
                    tmp[i+1] = "0"
                    tmp[i+4] = tmp[i+4][1:]

                    del(tmp[i+3])
                    del(tmp[i+2])

                    tmp_sum = eval("".join(tmp))

                    break
        # split
        elif len([x for x in re.findall("(\d+)", json.dumps(tmp_sum)) if int(x) >= 10]):
            tmp = re.findall("(\D+|\d+)", json.dumps(tmp_sum))
            for i, s in enumerate(tmp):
                if re.match("\d\d", s) is not None:
                    tmp[i] = f'[{int(s)//2}, {math.ceil(int(s)/2)}]'

                    tmp_sum = eval("".join(tmp))

                    break
        else:
            break

    return tmp_sum

def main():
    with open("input.txt") as f:
        num_list = [eval(line) for line in f]

    # part 1
    sum_total = num_list[0]
    for number in num_list[1:]:
        sum_total = snail_sum(sum_total, number)
    print(magnitude(sum_total))

    # part 2
    max_magnitude = max(max(magnitude(snail_sum(*x)), magnitude(snail_sum(*x[::-1]))) for x in itertools.combinations(num_list, 2))
    print(max_magnitude)


if __name__ == "__main__":
    main()
