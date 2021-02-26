/*
===============================================================
                    9095번 - 1, 2, 3 더하기
===============================================================
시간복잡도) 
1,2,3 총 3가지의 경우에서 선택하는 것이므로 -> O(3^n)
*/

#include <iostream>
using namespace std;
int go(int sum, int goal) {
    if (sum > goal) {
        return 0;
    }
    if (sum == goal) {
        return 1;
    }
    int now = 0;
    for (int i=1; i<=3; i++) {
        now += go(sum+i, goal);
    }
    return now;
}
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        cout << go(0, n) << '\n';
    }
    return 0;
}
