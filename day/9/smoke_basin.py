import math
import numpy as np


def main():
    with open("input.txt") as f:
        array2d = np.array([[int(x) for x in line.strip()] for line in f])

        # part 1
        minima = ((array2d < shift(array2d, x=1)) & (array2d < shift(array2d, x=-1)) & (array2d < shift(array2d, y=1)) & (array2d < shift(array2d, y=-1)))
        print(np.sum(minima * (array2d + 1)))

        # part 2
        minima_coords = np.transpose(np.nonzero(minima))
        list_basins = [flood_basin(array2d, np.array(coords)) for coords in minima_coords]
        print(math.prod(sorted(list_basins, reverse=True)[:3]))

def shift(arr, x = 0, y = 0):
    res = np.full_like(arr, 9)

    if x > 0:
        res[:,x:] = arr[:,:-x]
        return res
    elif x < 0:
        res[:,:x] = arr[:,-x:]
        return res
    elif y > 0:
        res[y:,:] = arr[:-y,:]
        return res
    elif y < 0:
        res[:y,:] = arr[-y:,:]
        return res
    else:
        return arr

def flood_basin(arr, coords):
    if np.any(coords < 0) or np.any(coords >= np.array(arr.shape)) or arr[tuple(coords)] == 9:
        return 0

    arr[tuple(coords)] = 9

    return 1 + flood_basin(arr, coords+(1,0)) + flood_basin(arr, coords-(1,0)) + flood_basin(arr, coords+(0,1)) + flood_basin(arr, coords-(0,1))


if __name__ == "__main__":
    main()
