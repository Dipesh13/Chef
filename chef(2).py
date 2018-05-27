import sys
data = sys.stdin.readlines()

test_cases = data[0]

for i in range(1,int(test_cases)+1):
    f = 0
    data[i]= data[i].split()
    print sum(int(i) for i in data[i])
