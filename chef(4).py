import sys
data = sys.stdin.readlines()

test_cases = data[0]


for i in range(1,2*int(test_cases),2):
    f = 0
    data[i]= data[i].split()
    data[i+1] = data[i+1].split()
    # print(data[i],data[i+1])
    for d in data[i]:
        if d in data[i+1]:
            f+=1
    if f >= len(data[i])/2:
        print("similar")
    else:
        print("dissimilar")
