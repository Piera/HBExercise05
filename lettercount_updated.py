# -*- coding: utf-8 -*-
from sys import argv

def initial():
    ords = [0] * 26
    return ords

def populate_list(f):
    ords = initial()

    for line in f:
        # line = line.replace(" ","")
        for char in line:
            lower = char.lower()
            if lower >= "a" and lower <= "z":            
                ords[ord(char.lower())-ord('a')] += 1

    return ords

def print_list(ords):
    sorted_ords = sorted([(ords[x], x) for x in range(len(ords))])
    # for i in sorted_ords:
    for count, letter in sorted_ords:
        # count, letter= i
        print "For letter %s the count is %d" % (chr(letter+97), count)

def spark_graph(ords):
    print " ".join(str(item) for item in ords)

def main(filename, spark):
    f = open(filename)
    ords = populate_list(f) 
    if spark:
        spark_graph(ords)
    else:
        print_list(ords)

if __name__ == "__main__":
    script, filename = argv[0:2]
    spark = (len(argv)> 2)
    # if len(argv) > 2:
    #     spark = True
    # else:
    #     spark = False

    main(filename, spark)