import sys
data = sys.stdin.readlines()

test_cases = data[0]
for i in range(1,int(test_cases)+1):
    if data[i] == 'b' or 'B':
        print("BattleShip")
    elif data[i] == 'c' or 'C':
        print("Cruiser")
    elif data[i] == 'f' or 'F':
        print("Frigate")
    else:
        print("Destroyer")