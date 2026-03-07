# 18870 좌표 압축
import sys

N=int(input())
arr=list(map(int,sys.stdin.readline().split()))

sorted_unique=sorted(set(arr))

compress={value: idx for idx, value in enumerate(sorted_unique)}

sys.stdout.write(' '.join(map(str,(compress[x] for x in arr))))