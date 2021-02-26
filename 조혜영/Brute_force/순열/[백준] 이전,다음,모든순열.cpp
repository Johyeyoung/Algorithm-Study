/*
===============================================================
                    10972번 - 다음 순열
===============================================================
시간복잡도: O(N)
*/

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i=0; i<n; i++) {
        cin >> a[i];
    }
    if (next_permutation(a.begin(),a.end())) {
        for (int i=0; i<n; i++) {
            cout << a[i] << ' ';
        }
    } else {
        cout << "-1";
    }
    cout << '\n';
    return 0;
}







/*
===============================================================
                    10972번 - 다음 순열
===============================================================
시간복잡도: O(N)
next_permutation - 실제 구현 
*/

bool next_permutation(vector<int> &a, int n) {
    // 1) 무엇으로 시작하는 마지막 순열인지- i 찾음 (마지막 순열이므로 내림차순의 시작부분): O(N)
	int i = n-1;
    while (i > 0 && a[i-1] >= a[i]) {
        i -= 1;
    }
    if (i <= 0) { // 모든 원소가 다 내림차순이라는건 제일 마지막 순열임 더이상 없음
        return false;
    }

	// 2) j 찾음: O(N)
    int j = n-1;
    while (a[j] <= a[i-1]) {
        j -= 1;
    }

	// 3) i-1, j 교환: O(1)
    swap(a[i-1], a[j]); 

	// 4) i~n 까지 뒤집기- 오름차순되도록: O(N)
	j = n-1;
    while (i < j) { 
        swap(a[i], a[j]);
        i += 1; 
        j -= 1;
    }
    return true;
}

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i=0; i<n; i++) {
        cin >> a[i];
    }
    if (next_permutation(a,n)) {
        for (int i=0; i<n; i++) {
            cout << a[i] << ' ';
        }
    } else {
        cout << "-1";
    }
    cout << '\n';
    return 0;
}




/*
===============================================================
                    10974번 - 모든 순열
===============================================================
순열 시간복잡도: O(N x N!) - 순열의 개수(N!)만큼 다음 순열연산(N)을 해야돼서
*/






