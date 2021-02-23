/*
===============================================================
                         14501. 퇴사
===============================================================
- 시간 복잡도)
조합 문제(C): 1~N일까지 총 N개의 날짜 (선택하냐 안하냐 종류는 2가지) -> O(2^N)
N ≤ 15이므로 2^15 ≤ 1024*32 정도이므로 Brute force 재귀로 모든 가짓수 다 check 可
- 주의)
index 사용을 0부터 하냐 1부터 하냐에 따라 구현이 어려워지는 경우有, 이 문제는 둘다 쉬움
*/

#include <iostream>
using namespace std;
const int inf = -100000000;
int t[16]; // 상담 소요 기간
int p[16]; // 금액
int n;
int ans = 0;

void go(int day, int sum) {
    if (day == n + 1) { // 퇴사+1일 탈출 (퇴사일(n)은 아직 일할 수 있음. 탈출 x)
        if (ans < sum) ans = sum;
        return;
    }
    if (day > n + 1) { 
        return;
    }
    // 재귀 - 선택할지 말지 
    go(day + 1, sum); // 선택 X
    go(day + t[day], sum + p[day]); // 선택 O
}


int main() {
    cin >> n;
    for (int i = 1; i <= n; i++) { // idx 0번 안쓰는 경우, idx=1은 1일 
        cin >> t[i] >> p[i];
    }
    go(1, 0); // 기준되는 날 1일부터 
    cout << ans << '\n';
    return 0;
}
