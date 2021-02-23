/*
===============================================================
                    14888. 연산자 끼워넣기
===============================================================
시간 복잡도)
조합 문제(C): 총 (N-1)개의 연산자 선택 (연산자의 종류는 4가지) -> O(4^(N-1))
(N-1) ≤ 10이므로 4^10 ≤ 1048576 정도이므로 Brute force 재귀로 모든 가짓수 다 check 可 
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int a[11];
int main() {
	int n // 수의 개수
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    int plus, minus, mul, div;
    cin >> plus >> minus >> mul >> div;

	return 0;
}








#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
pair<int, int> calc(vector<int>& a, int index, int cur, int plus, int minus, int mul, int div) {
    int n = a.size();
    if (index == n) {
        return make_pair(cur, cur);
    }
    vector<pair<int, int>> res;
    if (plus > 0) {
        res.push_back(calc(a, index + 1, cur + a[index], plus - 1, minus, mul, div));
    }
    if (minus > 0) {
        res.push_back(calc(a, index + 1, cur - a[index], plus, minus - 1, mul, div));
    }
    if (mul > 0) {
        res.push_back(calc(a, index + 1, cur * a[index], plus, minus, mul - 1, div));
    }
    if (div > 0) {
        res.push_back(calc(a, index + 1, cur / a[index], plus, minus, mul, div - 1));
    }
    auto ans = res[0];
    for (auto p : res) {
        if (ans.first < p.first) {
            ans.first = p.first;
        }
        if (ans.second > p.second) {
            ans.second = p.second;
        }
    }
    return ans;
}
int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    int plus, minus, mul, div;
    cin >> plus >> minus >> mul >> div;
    auto p = calc(a, 1, a[0], plus, minus, mul, div);
    cout << p.first << '\n';
    cout << p.second << '\n';
    return 0;
}