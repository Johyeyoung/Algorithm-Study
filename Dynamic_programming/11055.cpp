#include <iostream>
using namespace std;

#define MAX 1000

int arr[MAX + 1]; // 수열
int dp[MAX + 1];
// dp[i] : 수열 맨 처음부터 i-1번째까지에서 가장 큰 증가하는 부분 수열의 길이


int main()
{

	int n; 
	cin >> n;
	

	for (int i = 1; i <= n; ++i)
	{
		cin >> arr[i];
	}

	int result = 0; // 최대값 저장
	for (int i = 1; i <= n; ++i) 
	{
		dp[i] = arr[i]; 
		for (int j = 0; j < i; ++j) 
		{
			if (arr[j] < arr[i] && dp[i] < dp[j] + arr[i])
				
			{
				dp[i] = dp[j] + arr[i]; 
			}
		}
 
		if (result < dp[i]) result = dp[i];
		
	}

	cout << result << "\n";
}
