#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int n; cin >> n;
	int result = 0;
	int tri[501][501] = {0, };

	for(int i=1; i <= n; i++){
		for(int j=1; j <= i; j++){
			cin >> tri[i][j];
		}
	}

	for(int i=2; i <= n; i++){
		for(int j=1; j <= i; j++){
			tri[i][j] = max(tri[i-1][j-1] + tri[i][j], tri[i-1][j] + tri[i][j]);

			result = max(result, tri[i][j]);
		}
	}

	cout << result << endl;


	// 왼쪽 대각선 아래, 오른쪽 대각선 아래 더해서 최대값
	// => 왼쪽 대각선 위, 오른쪽 대각선 위 중 최대값 더하기

	// int dp[501][501] = {0, };
	//
	// for(int i = 1; i <= n; i++){
	// 	for(int j = 1; j <= i; j++){
	// 		cin >> dp[i][j];
	//
	// 		// 맨 왼쪽인 경우 오른쪽 대각선 위 숫자만 더할 수 있음
	// 		if(j == 1) dp[i][j] = dp[i-1][j] + dp[i][j];
	//
	// 		// 맨 오른쪽인 경우 왼족 대각선 위 숫자만 더할 수 있음
	// 		else if(j == i) dp[i][j] = dp[i-1][j-1] + dp[i][j];
	//
	// 		// 중간인 경우 오른쪽 대각선과 왼쪽 대각선의 숫자 중 최대값으로 더함
	// 		dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + dp[i][j];
	//
	// 		result = max(result, dp[i][j]);
	// 	}
	// }
	// cout << result << endl;


	return 0;
}
