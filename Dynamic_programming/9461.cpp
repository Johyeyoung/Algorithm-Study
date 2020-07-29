#include <iostream>
using namespace std;
#define INF 100000

int main() {
	int T, N; cin >> T;
	long dp[101];
	dp[0] = 0;
	dp[1] = 1;
	dp[2] = 1;

	for(int testCase = 0; testCase < T; testCase++){
		cin >> N;

		for(int i = 3; i <= N; i++){
			dp[i] = dp[i - 3] + dp[i - 2];
		}
		cout << dp[N] << endl;
	}
	return 0;
}
