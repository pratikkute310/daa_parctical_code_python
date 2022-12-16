w = [3,5,5,8,4]
p = [10,20,21,30,16]
ratio = list()
m = 20
n = 5
for i in range(n):
    ratio.append(p[i]/w[i])
z = zip(ratio, p, w)
a = list(z)
a.sort(reverse=True)
profit = 0
for i in a:
    if(i[2]<=m):
        profit+=i[1]
        m-=i[2]
    else:
        profit+=(m/i[2]*i[1])
        break
print(f"Profit : {profit}")