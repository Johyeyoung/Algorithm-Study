#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// 그리디 -> 제일 가치가 큰 순서대로 동전을 만든다
// 가치가 K보다 크다면 한 단계 낮은 가치를 더한다.

int main() {
	int N, K, cnt = 0;
	vector <int> v;

	cin >> N >> K;
	for(int i=0; i<N; i++) {
		int m;
		cin >> m;
		v.push_back(m);
	}

	for(int i=N-1; i>=0; i--){
		if (K == 0) break;
		while(K >= v[i]){
			K -= v[i];
			cnt++;
		}
	}

	cout << cnt << endl;

	return 0;
}
