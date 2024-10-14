n = int(input())
m = int(input())
a = []
if m>0:
    for i in range(1, n+1):
        a.append(i)
    b = a*100000
    digit = a[0]
    ans=[]
    while digit != b[m-1]:
        c = b[0]
        ans.append(c)
        b = b[m-1:]
    ans.append(b[0])
    final_ans = str()
    for element in ans:
        final_ans = final_ans + str(element)
    print(final_ans)
else:
#Если параметр m отрицательный, это движение в обратную сторону по круговому массиву
    for i in range(1, n+1):
        a.append(i)
    a = a[::-1]
    b = a*100000
    digit = a[0]
    m = abs(m)
    ans=[]
    while digit != b[m-1]:
        c = b[0]
        ans.append(c)
        b = b[m-1:]
    ans.append(b[0])
    final_ans = str()
    for element in ans:
        final_ans = final_ans + str(element)
    print(final_ans)
