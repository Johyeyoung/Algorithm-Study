#include <iostream>
#include <stdio.h>
#include <cstring> // memset
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
using namespace std;

int main() {
	int N; cin >> N;
	int step[301] = {0, };
	int dp[301] = {0, };

	for(int i = 1; i <= N; i++){
		cin >> step[i];
	}

	dp[1] = step[1];
	// 두 번째 계단 : 한 칸씩 vs 두 칸 한번에
	dp[2] = max(step[1] + step[2], step[2]);
	// 세 번째 계단 : 한 칸 + 두 칸 vs 두 칸 + 한 칸
	dp[3] = max(step[1] + step[3], step[2] + step[3]);


	// 세 번째 계단과 같은 과정이지만 세 계단을 연속해서 밟을 수 없다는 것 고려!!
	// => 두 칸 바로 vs 두 칸 + 한 칸
	for(int i = 4; i <= N; i++){
		dp[i] = max(dp[i - 2] + step[i], dp[i - 3] + step[i - 1] + step[i]);
	}

	//for(int i=1; i<=N; i++) cout << dp[i] << endl;
	cout << dp[N] << endl;

	return 0;
}
