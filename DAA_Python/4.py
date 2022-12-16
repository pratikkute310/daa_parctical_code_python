def printlst(lst):
    print()
    for i in lst:
        print(i)
    print()

def min(x, y):
    if(x==None):
        return y
    elif(y==None):
        return x
    if(x<y):
        return x
    else:
        return y

v = 4
lst = [[ None for I in range(v)] for j in range (v)]

for i in range(v):
    lst[i][i] = 0

lst[0][1] = 3
lst[0][3] = 7
lst[1][0] = 8
lst[1][2] = 2
lst[2][0] = 5
lst[2][3] = 1
lst[3][0] = 2

printlst(lst)

for k in range(v):
    printlst(lst)
    for i in range(v):
        if(i==k):
            continue
        for j in range(v):
            if(j==k or i==j):
                continue
            if(lst[i][k]==None or lst[k][j]==None):
                add = None
            else:
                add = lst[i][k]+lst[k][j]
            lst[i][j] = min(lst[i][j], add)

print("Final Grid : ")
printlst(lst)