#include <iostream>
#include <stdio.h>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

/* N-1개 원판을 1에서 2로 옮긴다. 1에 있는 마지막 원판을 3으로 옮긴다.
// 2에 있는 N-1개의 원판을 3으로 옮긴다.
// N-1개의 원판을 옮기는 것을 재귀적으로 푼다.
// -> N-1개를 2로 옮기는 문제는 N-1-1개를 2로 옮기는
*/
vector<pair <int, int> > v;

void hanoi(int n, int fir, int mid, int end){
	if( n == 1) v.push_back(make_pair(fir, end));
	else{
		hanoi(n-1, fir, end, mid);
		v.push_back(make_pair(fir, end));
		hanoi(n-1, mid, fir, end);
	}
}
int main() {
	int n;
	scanf("%d", &n);
	hanoi(n, 1, 2, 3);
	printf("%d\n", v.size());
	for(int i=0; i<v.size(); i++) printf("%d %d\n", v[i].first, v[i].second);


	return 0;
}
