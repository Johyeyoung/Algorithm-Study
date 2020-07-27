#include <iostream>
using namespace std;
#define MOD 1000000000

int main() {
	int N, sum = 0; cin >> N;
	int dp[101][11] = {0, }; // [자릿수][끝자리 숫자(0~9)]

	// 한 자리 숫자 끝자리가 0일 때 제외 => 모든 값 1로 설정
	for(int i = 1; i <= 9; i++) dp[1][i] = 1;

	// 두 자리 이상 숫자
	// 1) 끝자리 숫자가 0일 때 : 그 앞자리에 1만 올 수 있다.
	// 2) 끝자리 숫자가 9일 때 : 그 앞자리에 8만 올 수 있다.
	// 3) 이외 : 그 앞자리에 해당 숫자-1 or 숫자+1 이 올 수 있다.
	// ※ i - 1 : 세 자리인 경우 맨 마지막 숫자 제외 => 결국 두 자리 숫자의 계단수와 동일
	for(int i = 2; i <= N; i++){
		for(int j = 0; j <= 9; j++){
			if (j == 0) dp[i][j] = dp[i-1][1] % MOD;
			else if(j == 9) dp[i][j] = dp[i-1][8] % MOD;
			else dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % MOD;
		}
	}

	for(int i = 0; i <= 9; i++){
		sum = (sum + dp[N][i]) % MOD;
	}
	cout << sum << endl;



	return 0;
}
