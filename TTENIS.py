import sys
data = sys.stdin.readlines()
# TTENIS

x = data[0]
for i in range(1,len(data)):
    # print (data[i])
    list_str = []
    for str in data[i]:
        list_str.append(str)
    list_str = [l for l in list_str if l != '\n']
    # print(list_str)
    # print(list_str.count('0'),list_str.count('1'))
    if int(list_str.count('1')) == 11:
        print("WIN")
    elif int(list_str.count('1')) == int(list_str.count('0')) == 10:
        print("Draw")
    else:
        print("Loose")
