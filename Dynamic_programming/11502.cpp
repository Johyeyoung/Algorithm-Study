#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

int main() {
	int N, num, result = 0; cin >> N;
	int card[1001];
	int dp[1001]; // 해당 idx 개수를 샀을 때 최대 비용

	for(int i = 1; i <= N; i++){
		cin >> card[i];
	}

	memset(dp, 0, sizeof(dp));

	for(int i = 1; i <= N; i++){
		for(int j = 1; j <= i; j++){
			dp[i] = max(dp[i], dp[i - j] + card[j]);
		}
	}

	// for(int i = 1; i <= N; i++) cout << dp[i] << " ";
	// cout << endl;

	cout << dp[N] << endl;
	return 0;
}
