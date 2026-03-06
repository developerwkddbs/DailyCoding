import sys

T = int(sys.stdin.readline())
results = []

for _ in range(T):
    ps = sys.stdin.readline().strip()
    stack = []
    is_vps = True

    for idx in ps:
        if idx == "(":
            stack.append(idx)
        else:  # idx == ")"
            if stack:
                stack.pop()
            else:
                is_vps = False
                break

    if is_vps and not stack:
        results.append("YES")
    else:
        results.append("NO")

print("\n".join(results))