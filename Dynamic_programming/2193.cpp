#include <iostream>
using namespace std;


// N = 1 이친수의 개수 : 1
// N = 2 이친수의 개수 : 1
// N = 3 이친수의 개수 : 2
// N = 4 이친수의 개수 : 3
// N = 5 이친수의 개수 : 5
// ... => 규칙 보임! d[N] = d[N-1] + d[N-2]

int main() {
	int N; cin >> N;
	long long int dp[91] = {0, };
	dp[1] = 1;
	dp[2] = 1;

	for(int i = 3; i <= N; i++){
		dp[i] = dp[i - 1] + dp[i - 2];
	}
	cout << dp[N] << endl;

	return 0;
}
