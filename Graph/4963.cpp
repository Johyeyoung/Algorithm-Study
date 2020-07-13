#include <iostream>
#include <stdio.h>
#include <cstring> // memset
using namespace std;
int w, h;
const int MAX = 50;
int arr[MAX][MAX];
int visited[MAX][MAX];
int dx[] = {-1, 1, 0, 0, 1, -1, 1, -1};
int dy[] = {0, 0, 1, -1, 1, 1, -1, -1}; // 방향 탐색

// 가로 세로, 대각선으로 연결되어 있는 지 판별
// 방문한 경우 visited 배열에 1로 저장
void search(int y, int x){
	// 바다인 경우와 이미 방문한 경우 탐색 종료
	if(!arr[y][x] || visited[y][x]) return;

	visited[y][x] = 1; // 탐색 성공 -> 1로 저장

	// 가로 세로 대각선 탐색
	for(int i=0; i<8; i++){
		int newX = x + dx[i];
		int newY = y + dy[i];
		if(0 <= newX && newX < w && 0<= newY && newY < h){
			search(newY, newX);
		}
	}
}

int main() {
	cin >> w >> h;
	while( (w != 0) && (h != 0)){
		for(int i=0; i<h; i++){
			for(int j=0; j<w; j++){
				scanf("%d", &arr[i][j]);
			}
		}
		int cnt = 0;
		memset(visited, 0, sizeof(visited)); // visited 배열 0으로 초기화
		for(int i=0; i< h; i++){
			for(int j=0; j<w; j++){
				if(arr[i][j] && !visited[i][j]){ // 섬인 동시에 탐색하지 않은 경우에만 탐색 시작
					search(i, j);
					cnt++;
				}
			}
		}
		printf("%d\n", cnt);
		cin >> w >> h;

	}
	return 0;
}

