#include <iostream>
#include <algorithm>
using namespace std;

int main() {

	int N, K;
	cin >> N >> K; // 물품의 수, 버틸수 있는 무게

	int dp[100001] = { 0, };


	int W, V; // 무게, 가치
	for (int i = 0; i < N; i++) {
		cin >> W >> V;
		for (int j = K; j >= 1; j--) {  //중복을 제거하기 위해 뒤에서부터 계산한다.
			if (j >= W) {
				dp[j] = max(dp[j - W] + V, dp[j]);
				// cout << j << ": "<<dp[j] << endl; 
			}
		}
	}

	cout << dp[K];



	return 0;
}