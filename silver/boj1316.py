N=int(input())
cnt=0

for _ in range(N):
    word=input()
    visited=set()
    prev=''

    is_group=True

    for c in word:
        if c != prev:
            if c in visited:
                is_group=False
                break
            visited.add(c)
        prev=c
    
    if is_group:
        cnt+=1

print(cnt)