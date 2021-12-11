import numpy as np

def main():
    with open("input.txt") as f:
        array2d = np.array([[int(x) for x in line.strip()] for line in f])

        flash_count = 0
        synced_at = []

        step = 0
        while step < 100 or len(synced_at) < 1:
            # increment all fields
            array2d += 1

            # get indices of all 10s
            tens = np.transpose(np.nonzero(array2d == 10)).tolist()

            # process all 10s
            i = 0
            while i < len(tens):
                (y,x) = tens[i]

                # increment the 3x3 window around a 10
                win = array2d[slice(max(0, y-1), min(10, y+2)), slice(max(0, x-1), min(10, x+2))]
                win += 1

                # add new tens caused by the last action to the processing queue
                new_tens = np.transpose(np.nonzero(win == 10)) + np.array([max(0, y-1), max(0, x-1)])
                tens.extend(new_tens.tolist())

                i += 1

            # reset all fields that are > 9 to 0
            array2d *= (array2d <= 9)

            flash_count += i

            step += 1

            # if all fields are 0 now, store the current step (part 2)
            if np.count_nonzero(array2d) == 0:
                synced_at.append(step)

            # part 1
            if step == 100:
                print(flash_count)

        # part 2
        print(synced_at[0])


if __name__ == "__main__":
    main()
