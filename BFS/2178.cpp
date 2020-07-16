#include <iostream>
#include <stdio.h>
#include <cstring> // memset
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
using namespace std;

const int MAX = 101;
int cnt, N, M;;
int map[MAX][MAX];
int visited[MAX][MAX];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

// 갈 수 있는 경로가 여러 개 일 때 최소횟수 어떻게?
// -> 길을 지날때마다 그 길을 몇번에 걸쳐 도달했는지 값 저장
void bfs(int i, int j){
	queue <pair<int, int> > q;

	visited[i][j] = 1;
	q.push(make_pair(i, j));

	while(!q.empty()){
		int y = q.front().first;
		int x = q.front().second;
		q.pop();
		for(int k=0; k<4; k++){
			int newY = y + dy[k];
			int newX = x + dx[k];
			if(0 <= newY && newY < N && 0 <= newX && newX < M){
				if(!visited[newY][newX] && map[newY][newX]){
					map[newY][newX] = map[y][x] + 1;
					visited[newY][newX] = 1;
					q.push(make_pair(newY, newX));
				}

			}
		}
	}

}

int main() {
	cin >> N >> M;
	for(int i=0; i<N; i++){
		string s;
		cin >> s;
		for(int j=0; j<M; j++){
			map[i][j] = s[j] - '0';
		}
	}
	memset(visited, 0, sizeof(visited));
	bfs(0, 0);

	// for(int i=0; i<N; i++){
	// 	for(int j=0; j<M; j++){
	// 		cout << map[i][j] << " ";
	// 	}
	// 	cout << endl;
	// }

	cout << map[N-1][M-1]<< endl;


	return 0;
}

