import sys
data = sys.stdin.readlines()

test_cases = data[0]
list_sort = []
for i in range(1,int(test_cases)+1):
    f = 0
    list_sort.append(data[i])

list_sort = map(int,list_sort)
print(sorted(list_sort))
