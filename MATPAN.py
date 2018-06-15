import sys
import string
data = sys.stdin.readlines()

#MATPAN
x = int(data[0])
y = data[1].split()
# print(y)

val = list(string.ascii_lowercase)
# print(val)

dictionary = dict(zip(val,y))
# print(dictionary)
sum = 0
for i in range(2,2*x+1,2):
    # data[i] = data[i].split()
    char_list = [x for x in data[i] if x!='\n']
    # print(char_list)
    for char in val:
        if char in char_list:
            pass
        else:
            # print(char,dictionary[char])
            sum += int(dictionary[char])

print(sum)
