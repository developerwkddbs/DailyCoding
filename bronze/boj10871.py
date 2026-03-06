N,X=map(int, input().split(' '))

A=list(map(int, input().split(' ')))

for nums in A:
    if nums<X:
        print(nums, end=' ')