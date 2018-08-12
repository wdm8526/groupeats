import random
import sys


# groupeats.py takes in items ranked numberically, and based on their ranking, picks randomly, but skews to the more
# popular items. This was a garbage script written in 2 hours while doing other things.

# importer takes the system arguments and returns a list of filenames
def importer(filenames):
    files = list()
    filecounter = 1
    while filecounter < len(filenames):
        files.append(filenames[filecounter])
        filecounter += 1
    return files


# stripper reads the files and returns a list of items
def stripper(filename):
    with open(filename) as f:
        places = list()
        for line in f:
            line_split = line.split()
            counter = 0
            while counter < int(line_split[1]):
                places.append(line_split[0])
                counter += 1
    return places


#main runs the whole show, including printing out the chosen item.
def main():
    eats = list()
    filelist = importer(sys.argv)
    for file in filelist:
        eats.extend(stripper(file))
    print(eats[random.randint(0, len(eats) - 1)])


main()
