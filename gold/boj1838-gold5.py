import sys

data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
arr = data[1:]

SHIFT = 20               # 2^20 = 1,048,576 > 500,000
MASK = (1 << SHIFT) - 1
OFFSET = 1 << 31         # 값 범위 보정용

packed = [((arr[i] + OFFSET) << SHIFT) | i for i in range(n)]
packed.sort()

max_move = 0
for sorted_idx, v in enumerate(packed):
    original_idx = v & MASK
    move = original_idx - sorted_idx
    if move > max_move:
        max_move = move

print(max_move)