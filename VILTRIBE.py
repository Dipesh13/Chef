import sys
import re

# VILTRIBE
data = sys.stdin.readlines()
x = int(data[0])

for i in range(1,x+1):
    data_new = list(data[i])
    count_a = 1
    count_b = 1
    data_v1 = []
    for str in data_new:
        data_v1.append(str)
    data_v1 = [d for d in data_v1 if d!='\n']
    # print(data_v1)
    # print(len(data_v1))
    pattern_a  = r"[A](.)?[A]"
    pattern_b = r"[B](.)?[B]"
    pattern_a1 = r"(.)*[A](.)*"
    pattern_b1 = r"(.)*[B](.)*"
    for idx in range(len(data_v1)):
        # if data_new[idx] == 'A':
        #     while data_new[idx] != 'B' or data_new[idx] != 'A':
        #         count_a+=1
        # if data_new[idx] == 'B':
        #     while data_new[idx] != 'A' or data_new[idx] != 'B':
        #         count_b+=1
    print(count_a)
    print(count_b)