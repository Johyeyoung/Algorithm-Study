#include<stdio.h>
int arr[1001];
int dp[1001];

int main() {
	int N;
	int i, j;
	
	int max = 0;
	scanf_s("%d", &N);

	for (i = 0; i < N; i++)
	{
		dp[i] = 1; //ÃÊ±â°ªÀ» 1·Î ÁöÁ¤
		
		scanf_s("%d", &arr[i]);
		for (j = 0; j < i; j++)
		{
			if (arr[i] > arr[j] && dp[i] < dp[j]+1)
				dp[i]++;
		}

		
		if (max < dp[i])
			max = dp[i];
	}
	printf("%d", max);
} 
