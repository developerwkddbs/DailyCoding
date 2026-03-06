N=int(input())
if N<1 or N>100000000:
    exit(0)
nums=list(map(int,input().split(' ')))

print(min(nums), max(nums))