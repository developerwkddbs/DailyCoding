#include <stdio.h>
#include <stdlib.h>

int isPrime(int x){
    if(x<=1) return 0;

    for(int i=2; i*i<=x; i++){
        if(x%i==0) return 0;
    }
    
    return 1;
}

int main(){

    int N; //input value
    int cnt=0; //count value
    int idx[100]; //Will be certified value

    scanf("%d",&N); //Input N

    if(N>0&&N<=100){
        for(int i=0; i<N; i++){
            scanf("%d",&idx[i]);
            if(isPrime(idx[i])) cnt++;
            else continue;
        }
        printf("%d",cnt);
    }

    return 0;
}