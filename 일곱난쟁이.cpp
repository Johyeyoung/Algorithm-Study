#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	/* 9명 중 7명의 난쟁이 키의 합이 100이 되는 경우 
	 -> 9명의 난쟁이 키의 합 - (특정한 2명의 난쟁이 키) = 100 
	*/
	bool flag = false;
	int sum = 0, n = 9;
	vector<int> v;
	for (int i = 0; i < n; i++) {
		int m;
		cin >> m;
		v.push_back(m);
	}
	sort(v.begin(), v.end());

	for (int i = 0; i < n; i++) sum += v[i];

	for (int i = 0; i < n-1; i++) {
		for (int j = i+1; j < n; j++) {
			if (sum - v[i] - v[j] == 100) {
				v[i] = -1;
				v[j] = -1;
				flag = true;
				break;
			}
		}
		if (flag) break;
	}
	for (int i = 0; i < n; i++) if (v[i] != -1) cout << v[i] << " " << endl;

	return 0;
}
