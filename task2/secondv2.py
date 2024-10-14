from math import *
import sys
circle_file = sys.argv[1]
points_file = sys.argv[2]
with open(circle_file, "r") as file:
    lines = file.readlines()
    centers = []
    for i in range(0, len(lines), 2):
        numbers = lines[i].split()
        a = int(numbers[0])
        b = int(numbers[1])
        numbers = lines[i + 1].split()
        e = int(numbers[0])
with open(points_file, "r") as f:
    lines = f.readlines()
    points = []
    for line in lines:
        numbers = line.split()
        c = int(numbers[0])
        d = int(numbers[1])
        lenth = sqrt(((a-c)**2) + ((b-d)**2))
        if lenth==int(e):
            print(0)
        elif lenth>int(e):
            print(2)
        else:
            print(1)









