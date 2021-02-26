/*
===============================================================
					   1759. 암호 만들기
===============================================================
시간 복잡도)
조합 문제(C): 총 길이 L (문자의 종류는 C가지) -> O(2^C * L)
M ≤ 15이므로 15^15 ≤ 1048576 정도이므로 Brute force 재귀로 모든 가짓수 다 check 可
*/

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

go(int n, vector<char> &alpha, string password, int i) {
	// 1. 탈출 조건
	if (password.length() == n) {
		return;
	}


	// 재귀 - 선택 여부 반영
	go(n, alpha, password+alpha[i], i+1);
	go(n, alpha, password, i+1);
}

int main() {
	int n, m;
	cin >> n >> m;
	vector<char> a(m); // 문자를 담기
	for (int i = 0; i < m; i++) {
		cin >> a[i];
	}
	sort(a.begin(), a.end());

	return 0;
}





//-----------------------------------------------------------------------------
// 정답

#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
bool check(string& password) {
    int ja = 0;
    int mo = 0;
    for (char x : password) {
        if (x == 'a' || x == 'e' || x == 'i' || x == 'o' || x == 'u') {
            mo += 1;
        }
        else {
            ja += 1;
        }
    }
    return ja >= 2 && mo >= 1;
}
void go(int n, vector<char>& alpha, string password, int i) {
    if (password.length() == n) {
        if (check(password)) {
            cout << password << '\n';
        }
        return;
    }
    if (i == alpha.size()) return;
    go(n, alpha, password + alpha[i], i + 1);
    go(n, alpha, password, i + 1);
}
int main() {
    int n, m;
    cin >> n >> m;
    vector<char> a(m);
    for (int i = 0; i < m; i++) {
        cin >> a[i];
    }

    sort(a.begin(), a.end());

    go(n, a, "", 0);

    return 0;
}