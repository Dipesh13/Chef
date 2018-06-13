import sys
data = sys.stdin.readlines()

# STRLBP
x = int(data[0])

data_new_parent = []
for i in range(1,x+1):
    data_new = []
    for str in data[i]:
        data_new.append(str)
    data_new = [str.replace('\n',data_new[0]) for str in data_new]
    data_new_parent.append(data_new)

print(data_new_parent)
# for data in data_new_parent:
#     x = data[0]
#     # print(x)
#     # print(data.count(x))
#     if data.count(x) == len(data) or data.count(x) == len(data)-1:
#         print("uniform")
#     else:
#         if :
#             print("uniform")
#         else:
#             print("non-uniform")