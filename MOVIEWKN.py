import sys
data = sys.stdin.readlines()
# MOVIEWKN

x = data[0]
# print(len(data))
for i in range(1,len(data),3):
    num_movies = data[i]

scores = []
for i in range(2,len(data),3):
    score = []
    L = data[i].split()
    R = data[i+1].split()

    # print(L,type(L))
    for a,b in zip(L,R):
        score.append(int(a)*int(b))
    scores.append(max(score))

print(scores)
