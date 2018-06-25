import sys
data = sys.stdin.readlines()

# LOSTMAX
x = int(data[0])
for i in range(1,x+1):
    data[i] = data[i].split()
    x = len(data[i])
    # print(x)
    for d in data[i]:
        if int(d) == x-1:
            data[i].remove(d)
    # print(data[i])
    print(max(data[i]))
