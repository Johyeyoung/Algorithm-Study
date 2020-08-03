#include <string>
#include <vector>
#include <iostream>
using namespace std;

// 이 문제의 키포인트는 2행이 고정되어 있다는 점!!
// 따라서 위, 아래 대각선, 두 칸 대각선만 비교하면 된다.

int main(){
	int t, n, result = 0; cin >> t;
	int arr[2][100001] = {0, };
	int dp[2][100001] = {0, };

	for(int testCase = 0; testCase < t; testCase++){
		cin >> n;
		for(int i = 0; i <= 1; i++){
			for(int j = 1; j <= n; j++){
				cin >> arr[i][j];
			}
		}

		dp[0][1] = arr[0][1];
		dp[1][1] = arr[1][1];

		for(int j = 2; j <= n; j++){
			dp[0][j] = arr[0][j] + max(dp[1][j-1], dp[1][j-2]); // 대각선, 두번째 대각선
			dp[1][j] = arr[1][j] + max(dp[0][j-1], dp[0][j-2]); // 대각선, 두번째 대각선 
			result = max(dp[0][j], dp[1][j]);
		}

		cout << result << endl;
	}



}
