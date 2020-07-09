#include <iostream>
#include <stdio.h>
#include <vector>
#include <utility>
#include <string>
#include <algorithm>
using namespace std;

/* N을 N이 1이 돨 때까지 N/2로 쪼갠다.
만일 NxN에 있는 숫자가 모두 같다면 쪼갤 필요가 없고 해당 숫자를 출력한다.
*/

const int MAX = 64;
int N;
int arr[MAX][MAX];

void quad(int n, int y, int x){
	if(n == 1){
		cout << arr[y][x];
		return;
	}

	bool same = true;
	for(int i=y; i<y+n; i++){ // NxN에 있는 숫자가 모두 같은지 체크
		if(!same) break;
		for(int j=x; j<x+n; j++){
			if(arr[y][x] != arr[i][j]){
				same = false;
				break;
			}
		}
	}

	if(same){
		cout << arr[y][x];
		return;
	}
	
	cout << "(";
	quad(n/2, y, x); // 왼쪽 위
	quad(n/2, y, x+n/2); // 오른쪽 위
	quad(n/2, y+n/2, x); // 왼쪽 아래
	quad(n/2, y+n/2, x+n/2); // 오른쪽 아래
	cout << ")";

}

int main() {
	scanf("%d", &N);

	for(int i=0; i<N; i++){
		string s;
		cin >> s;
		for(int j=0; j<N; j++){
			arr[i][j] = s[j] - '0';
		}
	}

	quad(N, 0, 0); // arr[0][0]부터 검사
	cout << '\n';
	return 0;

}
