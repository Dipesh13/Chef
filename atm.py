data = input()
data = map(float,data.split())
if data[1]%5 != 0.0:
    print(data[1])
elif data[1]<data[0]:
    print(data[1])
else:
    print(data[1] - data[0] - 0.50)
