import sys
file3 = sys.argv[1]
with open(file3,"r") as file:
    a =[]
    c = file.readlines()
    for digit in c:
        a.append(int(digit.strip()))
b = sorted(a)
hops = 0
hops1 = 0
hops2 = 0
if len(b) % 2 == 0:
    middle = (len(b) // 2)
    first_middle_digit = b[middle]
    for digit in b:
        hop1 = abs(digit - first_middle_digit)
        hops1 = hops1 + hop1
    second_middle_digit = b[middle-1]
    for digit in b:
        hop2 = abs(digit - second_middle_digit)
        hops2 = hops2 + hop2
    if hops1==hops2:
        hops = hops1
    elif hops1 > hops2:
        hops = hops2
    else:
        hops = hops1
else:
    middle = (len(b) // 2)
    middle_digit = b[middle]
    for digit in b:
        hop = abs(digit - middle_digit)
        hops = hops + hop
print(hops)


