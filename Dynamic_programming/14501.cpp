#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

int main() {
	int N, result = 0; cin >> N;
	int dp[16];
	int T[16];
	int P[16];

	memset(dp, 0, sizeof(dp));
	for(int i = 1; i <= N; i++){
		int day, pay; cin >> day >> pay;
		T[i] = day;
		P[i] = pay;
	}

	for(int i = 1; i <= N; i++){
		int day = i;
		if(day + T[day] <= N) dp[i] = P[i];
		while(day + T[day] <= N){
			day += T[day];
			if(day + T[day] <= N) {
				//day += T[day];
				dp[i] += P[day];
			}
		}
		result = max(result, dp[i]);
	}

	for(int i=1; i<=N; i++)
	cout << dp[i] << " ";
	cout << endl;

	cout << result << endl;

	return 0;
}
