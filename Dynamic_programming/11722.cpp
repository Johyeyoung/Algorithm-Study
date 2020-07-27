#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int N, result = -1; cin >> N;
	int arr[1001];
	int dp[1001];

	for(int i = 0; i < N; i++) cin >> arr[i];

	for(int i = 0; i < N; i++){
		dp[i] = 1;
		for(int j = 0; j < i; j++){
			if(arr[j] > arr[i] && dp[j] + 1 > dp[i]){
				dp[i] = dp[j] + 1;
			}
		}
		result = max(result, dp[i]);
	}

	// for(int i = 0; i < N; i++) cout << dp[i] << " ";
	// cout << endl;
	cout << result << endl;

	return 0;
}
