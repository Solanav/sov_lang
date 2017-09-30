import sys
import  lib00 as l

def cleann(file):
    instruc = file.read().split(";")
    for x in range(0, len(instruc)):
        print(instruc[x])


def main():
    file0 = open(sys.argv[1], "r")
    cleann(file0)

if __name__=="__main__":
    main()
