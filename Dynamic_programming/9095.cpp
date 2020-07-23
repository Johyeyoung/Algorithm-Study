#include <iostream>
using namespace std;

// sol2) dp로 
// dp : n-1 또는 n-2 또는 n-3으로 부분 문제 만들기

int main() {
	int T,n; cin >> T;
	int dp[11];

	dp[0] = 0;
	dp[1] = 1;
	dp[2] = 2;
	dp[3] = 4;

	for(int testCase = 0; testCase < T; testCase++){
		cin >> n;
		for(int i = 4; i <= n; i++){
			dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
		}
		cout << dp[n] << endl;
	}

	return 0;
}
