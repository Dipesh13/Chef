user_data = raw_input()
for data in user_data:
    data = data.split('\n')
    print (len(data))
    for d in data:
        d = d.split(' ')
        print (len(d))

test_cases = int(user_data[0])
print (test_cases)

# N,Q = map(int,input().split())
# L1 = list(map(float,input().split()))
# for i in range(0,Q):
#     L,R = map(int,input().split())

# N = int(input())
# array = list(map(int,input().split()))
