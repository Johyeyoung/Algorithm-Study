nclude <iostream>
#include <stdio.h>
#include <cstring> // memset
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

void dfs(int start, vector<int> node[], int visited[]){
	visited[start] = 1;
	cout << start << " ";

	for(int i=0; i<node[start].size(); i++){
		int next = node[start][i];
		if(!visited[next]) dfs(next, node, visited);
	}
}

void bfs(int start, vector<int> node[], int visited[]){
	queue <int> q;
	q.push(start);
	visited[start] = 1;

	while(!q.empty()){
		int front = q.front();
		q.pop();
		cout << front << " ";
		for(int i=0; i<node[front].size(); i++){
			if (!visited[node[front][i]]){
				q.push(node[front][i]);
				visited[node[front][i]] = 1;
			}

		}
	}

}

int main() {
	int N, M, V;
	cin >> N >> M >> V;
	vector <int> node[N+1];
	int visited[N+1];

	memset(visited, 0, sizeof(visited));

	for(int i=0; i<M; i++){
		int a, b;
		cin >> a >> b;
		node[a].push_back(b);
		node[b].push_back(a);
	}

	for(int i=1; i<=N; i++) sort(node[i].begin(), node[i].end());
	dfs(V, node, visited);
	printf("\n");

	memset(visited, 0, sizeof(visited));

	bfs(V, node, visited);
	printf("\n");

	return 0;
}

