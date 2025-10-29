#include <stdio.h>

int main(){
    int n;
    double sum = 0;

    printf("input: ");
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        sum += i;
        printf("%lf   %d\n",sum,i);
    }
    printf("sum of %d is %lf",n,sum);
    return 0;
}