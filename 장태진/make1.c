#include<stdio.h>
#define MAX_SIZE 16382
int min(int a, int b) {

	return a > b ? b : a;
}


int main() {

	int N, i;

	int dp[1000001] = { 0,};

	scanf_s("%d", &N);

	dp[1] = 0;

	for (i = 2; i <= N; i++)
	{
		dp[i] = dp[i - 1] + 1;
		if (i % 2 == 0) dp[i] = min(dp[i], dp[i / 2] + 1);
		if (i % 3 == 0)dp[i] = min(dp[i], dp[i / 3] + 1);
	}


	printf("%d\n", dp[N]);
}
