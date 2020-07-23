#include <iostream>
#include <algorithm>
using namespace std;

// N에서 -1 또는 /2, /3의 과정을 거쳐 1까지 최소 횟수로 만든다.
// -> 부분 문제로 생각하기!
// => N-1을 1로 만드는 횟수의 최솟값 + 1 or N/2를 1로 만드는 횟수의 최솟값  + 1
// or N/3을 1로 만드는 횟수의 최솟값  + 1

int main() {
	int N; cin >> N;
	int dp[1000001];
	dp[0] = dp[1] = 0;

	for(int i=2; i<=N; i++){
		dp[i] = dp[i-1] + 1;
		if(i % 2 == 0) dp[i] = min(dp[i], dp[i /  2] + 1);
		if(i % 3 == 0) dp[i] = min(dp[i], dp[i / 3] + 1);
	}

	cout << dp[N] << endl;

	return 0;
}
