s = int(input())
n = list(map(int,input()))

row,column = 2*s+3,s+3
arr_2d = [[" "]*column for i in range(row)]
answer = [[] for i in range(row)]
for i in range(len(n)):
    if n[i] in [2,3,5,6,7,8,9]:
        for a in range(s):
            arr_2d[0][a+1] = "-"
    if n[i] in [1,2,3,4,7,8,9]:
        for b in range(s):
            arr_2d[b+1][s+1] = "|"
    if n[i] in [4,5,6,8,9]:
        for c in range(s):
            arr_2d[c+1][0] = "|"
    if n[i] in [2,3,4,5,6,8,9]:
        for d in range(s):
            arr_2d[s+1][d+1] = "-"
    if n[i] in [2,6,8]:
        for e in range(s):
            arr_2d[s+2+e][0] = "|"
    if n[i] in [1,3,4,5,6,7,8,9]:
        for f in range(s):
            arr_2d[s+2+f][s+1] = "|"
    if n[i] in [2,3,5,6,8,9]:
        for g in range(s):
            arr_2d[2*s+2][g+1] = "-"
    for x in arr_2d:
        x.append(" ")
    for i in range(row):
        answer[i]= answer[i] + arr_2d[i]
    arr_2d = [[" "]*column for i in range(row)]

for i in answer:
    print("".join(i))
