import sys
data = sys.stdin.readlines()
test_cases = data[0]
for i in range(1,int(test_cases)+1):
    if int(data[i]) < 10:
        print("What an obedient servant you are!")
    else:
        print("-1")