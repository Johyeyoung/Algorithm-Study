#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

// 1일 -> 7일 x , 7일 -> 1일로 생각!!!!

int main() {
	int N, per, result = 0; cin >> N;
	int dp[1001];
	int T[1001];
	int P[1001];
	memset(dp, 0, sizeof(dp));

	for(int i = 1; i <= N; i++){
		int day, pay; cin >> day >> pay;
		T[i] = day;
		P[i] = pay;
	}

	for(int i = N; i >= 1; i--){
		per = i + T[i]; // i번째 날에 걸리는 상담기간
		if(per > N + 1) dp[i] = dp[i+1]; // N + 1을 초과한다면 다음날의 이익
		else dp[i] = max(dp[i+1], dp[per] + P[i]); // 초과하지 않는다면
															// 다음날의 이익과 다음 상단의 최대 비용 + 당일의 상담비용 비교 
		result = max(result, dp[i]);
	}

	cout << result << endl;
	return 0;
}
