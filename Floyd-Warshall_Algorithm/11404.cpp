#include <iostream>
#include <algorithm>
using namespace std;
#define INF 100000

int main() {
	int n, m; cin >> n >> m;

	int bus[101][101];
	// 0이 아닌 값으로 배열 초기화할 때 fill 사용!!
	fill(&bus[0][0], &bus[100][101], INF);

	for(int i = 0; i < m; i++){
		int a, b, c; cin >> a >> b >> c;
		bus[a][b] = min(bus[a][b], c); // 시작, 도착 도시가 정해져 있음 => 즉, 유향 그래프
	}

	for(int k = 1; k <= n; k++){
		for(int i = 1; i <= n; i++){
			if (k != i){
				for(int j = 1; j <= n; j++){
					if(j != i && j != k)
					bus[i][j] = min(bus[i][j], bus[i][k] + bus[k][j]);
				}
			}

		}
	}

	for(int i = 1; i <= n; i++){
		for(int j = 1; j <= n; j++){
			if(bus[i][j] == INF) bus[i][j] = 0;
			cout << bus[i][j] << " ";
		}
		cout << endl;
	}

	return 0;
}
