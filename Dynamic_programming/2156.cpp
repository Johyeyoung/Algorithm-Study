#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int n; cin >> n;
	int drink[10001] = {0, };
	int dp[10001] = {0, };

	for(int i = 1; i <= n ; i++){
		cin >> drink[i];
	}

	dp[1] = drink[1];
	dp[2] = drink[1] + drink[2];

	for(int i = 3; i <= n; i++){
		dp[i] = max(dp[i-3] + drink[i-1] + drink[i], dp[i-2] + drink[i]);
		dp[i] = max(dp[i-1], dp[i]); // 아무것도 안 마시는 경우(2번 연속으로 마시지 않는 경우)
		// => 포도주가 극소량일 때 연속해서 2개를 마시면 3번째 포도주를 마실 수 없기 때문
	}

	cout << dp[n] << endl;

	return 0;
}
