import sys
data = sys.stdin.readlines()

# PERFCONT
x = int(data[0])
print(data)

for i in range(1,x+1,2):
    data_v1 = data[i]
    # print data_v1

for i in range(2,x+1,2):
    data_v2 = data[i]
    # print data_v2