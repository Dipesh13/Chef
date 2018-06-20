import sys
data = sys.stdin.readlines()

# LTM40AB
x = int(data[0])
for i in range(1,x+1):
    flag =0
    data[i] = data[i].split()
    data[i] = [d for d in data[i] if d != '\n']
    a,b,c,d = int(data[i][0]),int(data[i][1]),int(data[i][2]),int(data[i][3])
    for idx in range(c,d+1):
        if idx <= b and idx >=a:
            print(idx)
            flag +=1
        else:
            pass
    print(flag)