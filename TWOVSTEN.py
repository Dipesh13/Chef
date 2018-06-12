import sys
data = sys.stdin.readlines()

# TWOVSTEN

data = map(int,data)
x = data[0]

flag = 0
def rec(num):
    global flag
    if num % 10 != 0:
        num = num*2
        flag += 1
        rec(num)
    return flag

for i in range(1,x+1):
    if data[i]%5 !=0:
        print ("-1")
    else:
        op = rec(data[i])
        print(str(op))