#include <iostream>
#include <stdio.h>
#include <cstring> // memset
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

const int MAX = 26;
int N;
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
int map[MAX][MAX];
int visited[MAX][MAX];
int number = 1;
int cnt;

/* 그래프 > 섬의 개수 문제와 비슷한 유형!! */

void search(int y, int x){
	if (!map[y][x] || visited[y][x]) return;

	visited[y][x] = 1;
	cnt++;
	map[y][x] = number;
	for(int i=0; i<4; i++){
		int newY = y + dy[i];
		int newX = x + dx[i];
		if(0 <= newY && newY < N && 0 <= newX && newX < N) search(newY, newX);
	}
}

int main() {
	int tmp = -1;
	vector <int> result;

	cin >> N;
	for(int i=0; i<N; i++){
		string str;
		cin >> str;
		for(int j=0; j<N; j++){
			map[i][j] = str[j] - '0';
		}
	}
	memset(visited, 0, sizeof(visited));

	for(int i=0; i<N; i++){
		for(int j=0; j<N; j++){
			if(map[i][j] && !visited[i][j]){ // 집이 있는 곳과 방문하지 않았던 곳만 탐색!
				cnt = 0;
				search(i, j);
				number++;
				result.push_back(cnt);
			}
		}
	}

	// 출력 확인
	// for(int i=0; i<N; i++){
	// 	for(int j=0; j<N; j++){
	// 		cout << map[i][j] << " ";
	// 	}
	// 	cout << endl;
	// }

	sort(result.begin(), result.end());
	cout << result.size() << endl;
	for(int i=0; i<result.size(); i++) printf("%d\n", result[i]);
	return 0;
}
