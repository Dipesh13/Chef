import sys
data = sys.stdin.readlines()

test_cases = data[0]


for i in range(1,int(test_cases)+1):
    f = 0
    x = data[i].count('1')
    y = data[i].count('0')
    if x > y:
        print("WIN")
    else:
        print("LOSE")
    i+=1
