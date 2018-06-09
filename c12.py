import sys
data = sys.stdin.readlines()
# H4(v2)
x = data[0]

for i in range(1,len(data)):
    n,m = map(int,data[i].split())
    ans = 0
    for i in range(1,n+1):
        ans+=i**2
    print(ans%m)
