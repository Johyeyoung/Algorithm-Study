#include <iostream>
#include <cstring>
using namespace std;

int main(){
	int t, N, M, result = 0; cin >> t;
	int bridge[31][31];
	for(int testCase = 0; testCase < t; testCase++){
		cin >> N >> M;
		memset(bridge, 0, sizeof(bridge));

		for(int i = 1; i <= M; i++){
			bridge[1][i] = i;
		}

		for(int i = 2; i <= N; i++){
			for(int j = i; j <= M; j++){
				for(int k = j; k >= i; k--){
					bridge[i][j] += bridge[i-1][k-1];
				}

			}
		}

		cout << bridge[N][M] << endl;
	}



}
