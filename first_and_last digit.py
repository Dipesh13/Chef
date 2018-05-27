import sys
data = sys.stdin.readlines()

test_cases = data[0]
for i in range(1,int(test_cases)+1):
    x = list(data[i])
    print(int(x[0])+int(x[-2]))