#include <iostream>
#include <algorithm>
using namespace std;

// 이전 집의 페인트 값 중 현재 집에 칠할 색을 제외한 min값 + 현재 집 페인트 값

int main() {
	int N; cin >> N;
	int arr[1001][3] = {{0, }};
	int dp[1001][3] = {{0, }};;

	for(int i = 1; i <= N; i++){
		for(int j = 0; j < 3; j++){
			cin >> arr[i][j];
		}
	}

	for(int i=1; i<=N; i++){
		dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]; // r로 칠한 경우
		dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + arr[i][1]; // g로 칠한 경우
		dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]; // b로 칠한 경우
	}
	cout << min(min(dp[N][0], dp[N][1]), dp[N][2]) << endl;

	return 0;
}

}
