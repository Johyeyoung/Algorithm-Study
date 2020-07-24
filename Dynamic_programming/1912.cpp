#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int n; cin >> n;
	int result = 0;
	int arr[100001] = {0, };
	int dp[100001] = {0, };


	for(int i = 0; i < n; i++){
		cin >> arr[i];
	}

	dp[0] = arr[0];
	result = dp[0];
	
	for(int i = 1; i < n; i++){
		dp[i] = max(arr[i], dp[i-1] + arr[i]);
		result = max(result, dp[i]);
	}

	cout << result << endl;

	return 0;
}
