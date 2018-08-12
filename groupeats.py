import random
import sys


def stripper(filename):
    with open(filename) as f:
        places = list()
        for line in f:
            line_split = line.split()
            counter = 0
            max = int(line_split[1])
            while counter < max:
                places.append(line_split[0])
                counter += 1
    return places


def main():
    filename = sys.argv[1]
    eats = stripper(filename)
    max_val = len(eats) - 1
    chosen_val = random.randint(0, max_val)
    print(chosen_val, " ", eats[chosen_val])


main()
