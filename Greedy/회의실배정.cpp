#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

/* STL : vector <pair <int, int> > v */

bool sortByEnd(const pair<int, int> &a, const pair<int, int> &b){
	return (a.second < b.second);
}

int main() {
	int N, cnt = 1, min = -1;
	vector <pair <int, int> > vec; // 시작 시간과 끝나는 시간을 요소로 가지는 이중 벡터
	cin >> N;

	for(int i=0; i<N; i++){
		int m1, m2;
		cin >> m1 >> m2;
		vec.push_back(make_pair(m1, m2));
	}

	sort(vec.begin(), vec.end()); // 시작 시간 오름차순
	sort(vec.begin(), vec.end(), sortByEnd); // 끝나는 시간 오름차숨

	// for(int i=0; i<N; i++){
	// 	cout << vec[i].first << " " << vec[i].second<< endl;
	// }
	min = vec[0].second;

	for(int i=1; i<N; i++){
		if(min <= vec[i].first){
			min = vec[i].second;
			cnt++;
		}
	}

	cout << cnt++ << endl;
	return 0;
}
