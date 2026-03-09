import sys

N=int(sys.stdin.readline())
arr=[]

for i in range(N):
    arr.append((int(sys.stdin.readline()),i))

arr.sort()

max_move=0

for i in range(N):
    move=arr[i][1]-i
    max_move=max(max_move, move)

print(max_move+1)