import sys

stack=[] # define stack
stack_top=-1 # define stack_top inital value

# define push func
def push(x):
    return stack.append(x)

# define pop func
def pop():
    if len(stack)!=0:
        return stack.pop()
    else:
        return -1

# define size func
def size():
    return len(stack)

# define empty func
def empty():
    if len(stack)==0:
        return 1
    else:
        return 0

# define top func
def top():
    if len(stack)!=0:
        return stack[len(stack)-1]
    else:
        return stack_top
    
# main part
N=int(sys.stdin.readline()) # Batch print
result=[] # result array
if N<1 or N>10000:
    exit(0)

for _ in range(N):
    Input=sys.stdin.readline().split()
    if Input[0]=='push':
        push(Input[1])
    elif Input[0]=='pop':
        result.append(str(pop()))
    elif Input[0]=='size':
        result.append(str(size()))
    elif Input[0]=='empty':
        result.append(str(empty()))
    elif Input[0]=='top':
        result.append(str(top()))

sys.stdout.write('\n'.join(result))