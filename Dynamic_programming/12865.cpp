#include<stdio.h>
#include<algorithm>
using namespace std;
/*
int dp[101][100001];//dp 이용
int wv[101][100001];//상품의  1차 시도는 무게 가치를 같이 구현 해봄 실패
*/
//int N, K; //크기와 가치
int dp[10001]; // 최종 값이 가치의 값이 기 때문에 1차원 사용
int w[101]; //무게 
int v[101]; // 가치

int N, K;
/*
int max(int a, int b) {
	return a > b ? a : b;
}
*/

int main()
{

	
	scanf_s("%d %d", &N, &K);
	
	
	for (int i = 1; i <= N; i++)
	{
		scanf_s("%d %d", &w[i], &v[i]);
	}
    
	for (int i = 1; i <= N; i++)
	{
		for (int j = K; j >=1; j--)
		{
			if (w[i]<=j) { //물건을 넣을 수 있을 때만 
				dp[j] = max(dp[j], dp[j - w[i]] + v[i]);
			}
			
			
		}
		
	}
	printf("%d\n", dp[K]);

	return 0;
}