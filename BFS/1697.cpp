#include <iostream>
#include <stdio.h>
#include <cstring> // memset
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
using namespace std;

const int MAX = 100000;
int N, K;
int cnt;
vector<int> move[MAX+1];
int visited[MAX+1];

int bfs(){
	queue<int> q;

	q.push(N);
	visited[N] = 1;

	// bfs 시작
	while(!q.empty()){
		int tmp = q.front();
		q.pop();

		// 수빈이 동생의 위치에 도달했을 경우 리턴
		if(tmp == K) return visited[tmp]-1;

		// 수빈의 현재 위치에 따라 가는 방법 다르게 설정
		// X-1
		if(tmp - 1 >= 0 && !visited[tmp-1]){
			visited[tmp-1] = visited[tmp]+1;
			q.push(tmp-1);
		}

		// X+1
		if(tmp + 1 <= MAX && !visited[tmp+1]){
			visited[tmp+1] = visited[tmp]+1;
			q.push(tmp+1);
		}

		// 2*X
		if(2*tmp <= MAX && !visited[2*tmp]){
			visited[2*tmp] = visited[tmp] + 1;
			q.push(2*tmp);
		}
	}
}

int main() {
	cin >> N >> K;

	memset(visited, 0, sizeof(visited));

	cout << bfs() << endl;

	return 0;
}
