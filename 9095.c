#include <stdio.h>

int dp(int n) {
	if(n == 1) {return 1;}
	if(n == 2) {return 2;}
	if(n == 3) {return 4;}
	return dp(n-1) + dp(n-2) + dp(n-3);
}

int main() {
	int T,n;
	scanf("%d",&T);
	while(T>0) {
		T--;
		scanf("%d",&n);
		printf("%d\n",dp(n));
	}
}
