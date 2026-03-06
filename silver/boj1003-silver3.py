T=int(input())

# initial value setting
cnt0=[0]*41 # N은 40보다 작거나 같은 자연수 or 0
cnt1=[0]*41 # 그러므로 41(0~40)

# if fibonacci(0) -> 1,1
cnt0[0]=1
cnt1[0]=0

# if fibonacci(1) -> 0,1
cnt0[1]=0
cnt1[1]=1

for i in range(2,41):
    # 0출력 횟수
    cnt0[i]=cnt0[i-1]+cnt0[i-2]
    # 1출력 횟수
    cnt1[i]=cnt1[i-1]+cnt1[i-2]

for _ in range(T):
    n=int(input())
    print(cnt0[n],cnt1[n])