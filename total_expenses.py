import sys
data = sys.stdin.readlines()
test_cases = data[0]
for i in range(1,int(test_cases)+1):
    data[i] = data[i].split()
    # for data in data[i]:
    if int(data[i][0]) > 1000:
        print(int(data[i][0])*int(data[i][1])*0.9)
    else:
        print(int(data[i][0])*int(data[i][1]))