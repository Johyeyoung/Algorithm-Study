#include <iostream>
#include <cstring> // memset
using namespace std;

int n, cnt;
int com[101][101] = {0, };
int visited[101];

void dfs(int k){
	if(visited[k] == 1) return;

	visited[k] = 1;
	cnt++;

	for(int i = 1; i <= n; i++){
		if(!visited[i] && com[k][i] == 1){
			dfs(i);
		}
	}



}
int main() {
	int m; cin >> n >> m;

	memset(visited, 0, sizeof(visited));

	for(int i = 0; i < m; i++){
		int a, b; cin >> a >> b;
		com[a][b] = 1;
		com[b][a] = 1;
	}

	dfs(1);

	cout << cnt - 1<< endl;

	return 0;
}
