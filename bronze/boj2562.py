nums=[int(input()) for _ in range(9)]

max_value=max(nums)
idx=nums.index(max_value)+1

print(max_value)
print(idx)