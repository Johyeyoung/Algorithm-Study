#include <iostream>

#include <vector>

#include <algorithm>

using namespace std;



int main() {

	int n, total = 0;

	cin >> n;

	vector<int> v;

	for (int i = 0; i < n; i++) {

		int m;

		cin >> m;

		v.push_back(m);

	}

	sort(v.begin(), v.end()); // 필요한 시간을 오름차순으로 정렬

	for (int i = 0; i < v.size(); i++) {
    for (int j = i; j >= 0; j--) {
      total += v[j];
    }
	}
	cout << total << endl;
	
	return 0;

}

