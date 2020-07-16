#include <iostream>
#include <stdio.h>
#include <cstring> // memset
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
using namespace std;

const int MAX = 1000;
int cnt, N, M;;
int box[MAX][MAX];
int visited[MAX][MAX];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
bool check = false;


// sol1) 최소 날짜가 아님!!!

void bfs(int i, int j){
	queue <pair<int, int> > q;

	visited[i][j] = 1;
	q.push(make_pair(i, j));
	while(!q.empty()){
		int y = q.front().first;
		int x = q.front().second;
		q.pop();
		check = false;
		int num = 0;
		for(int k=0; k<4; k++){
			int newY = y + dy[k];
			int newX = x + dx[k];
			if(0 <= newY && newY < N && 0 <= newX && newX < M){
				if(!visited[newY][newX] && box[newY][newX] == 0){
					check = true;
					num++;
					box[newY][newX] = 1;
					visited[newY][newX] = 1;
					q.push(make_pair(newY, newX));
				}

			}

		}
		// for(int i=0; i<N; i++){
		// 	for(int j=0; j<M; j++){
		// 		cout << box[i][j] << " ";
		// 	}
		// 	cout << endl;
		// }

		if (check) cnt++;
		cout << cnt << endl;

	}

}

int main() {
	cin >> N >> M;
	for(int i=0; i<N; i++){
		for(int j=0; j<M; j++){
			cin >> box[i][j];
		}
	}

	memset(visited, 0, sizeof(visited));

	for(int i=0; i<N; i++){
		for(int j=0; j<M; j++){
			if(box[i][j]){
				bfs(i, j);
			}
		}
	}

	cout << cnt << endl;


	return 0;
}
