# -*- coding: utf-8 -*-
from sys import argv
import string

script, filename = argv

f = open(filename)

# for i in range(ord("a"), ord("z")+1):
#     print i
excludes = set(string.punctuation)
ords = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for line in f:
    line = line.replace(" ","")
    #print line.rstrip()
    for char in line:
        #print 1, char.rstrip()
        # if char == "\n":
        #     print "T"
        #     line = line.replace(char, "")
        #     print line
        # if char in excludes or char.isdigit() or char == "\n":
        #     line = line.replace(char,"")
        # #print char
        #     if 122 >= ord(char.lower()) <= 97:
        #         print "alert!"
        #         line = line.replace(char, "")
        #         print line
        #     if char == "�":
        #         print "oops"

    # for char in line:
        lower = char.lower()
        if lower >= "a" and lower <= "z":            
            print "char:", char, ",,"
            print ord(char.lower())
            ords[ord(char.lower())-97] += 1

for item in ords:
    print item