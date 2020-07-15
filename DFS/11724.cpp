#include <iostream>
#include <stdio.h>
#include <cstring> // memset
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

const int MAX = 10000;
vector<int> graph[MAX+1];
int visited[MAX];

void dfs(int node){
	visited[node] = 1;

	for(int i=0; i<graph[node].size(); i++){
		int next = graph[node][i];
		if(!visited[next]) dfs(next);
	}

}

int main() {
	int N, M;
	int cnt = 0;
	cin >> N >> M;
	memset(graph, 0, sizeof(graph));
	memset(visited, 0, sizeof(visited));

	for(int i=0; i<M; i++){
		int u, v;
		cin >> u >> v;
		graph[u].push_back(v);
		graph[v].push_back(u);
	}

	for(int i=1; i<=N; i++){
		if(!visited[i]){
			dfs(i);
			cnt++;
		}
	}

	cout << cnt << endl;

	return 0;
}
