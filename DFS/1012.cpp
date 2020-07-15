#include <iostream>
#include <stdio.h>
#include <cstring> // memset
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

const int MAX = 51;
int M, N;
int map[MAX][MAX];
int visited[MAX][MAX];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

void dfs(int y, int x){
	if (visited[y][x] || !map[y][x]) return;

	visited[y][x] = 1;
	for(int i=0; i<4; i++){
		int newY = y + dy[i];
		int newX = x + dx[i];
		if(0 <= newY && newY < N && 0 <= newX && newX < M) dfs(newY, newX);
	}
}

int main() {
	int T, K;
	cin >> T;
	for(int i=0; i<T; i++){
		cin >> M >> N >> K;
		int cnt = 0;
		memset(map, 0, sizeof(map));
		memset(visited, 0, sizeof(visited));

		for(int j=0; j<K; j++){
			int y, x;
			cin >> x >> y;
			map[y][x] = 1;
		}

		for(int j=0; j<N; j++){
			for(int k=0; k<M; k++){
				if(map[j][k] && !visited[j][k]){
					dfs(j, k);
					cnt++;
				}
			}
		}
		cout << cnt << endl;

	}

	return 0;
}
