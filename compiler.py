import sys
import  lib00 as l

def cleann(file):
    line = file.read().split("\n")
    for x in range(0, len(line)):
        if "\t" in line:
            temp = line.split("t", 1)
            print(temp)


def main():
    file0 = open(sys.argv[1], "r")
    cleann(file0)

if __name__=="__main__":
    main()
