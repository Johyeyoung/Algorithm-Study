#include <iostream>
using namespace std;

// i -> j 직접 경로 or i -> k -> j 거치는 경로

int main() {
	int N; cin >> N;

	int graph[101][101];

	for(int i = 0; i < N; i++){
		for(int j = 0; j < N; j++){
			cin >> graph[i][j];
		}
	}

	for(int k = 0; k < N; k++){
		for(int i = 0; i < N; i++){
			for(int j = 0; j < N; j++){
				if(graph[i][k] == 1 && graph[k][j] == 1)
					graph[i][j] = 1;

			}
		}
	}

	for(int i = 0; i < N; i++){
		for(int j = 0; j < N; j++){
			cout << graph[i][j] << " ";
		}
		cout << endl;
	}



	return 0;
}

