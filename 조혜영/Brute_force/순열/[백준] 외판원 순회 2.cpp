/*
===============================================================
                    10971번 - 외판원 순회 2
===============================================================
시간복잡도 )
O(N!*N)
*/
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n; 
    int cost[20][20];
    vector<int> route(n);
    int ans = 2147483647; // min

    // 입력받기
    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> cost[i][j];
        }
    }

    // 첫 순열 생성 - 오름차순: 0~(n-1)번째 도시
    for (int i = 0; i < n; i++) {
        route.push_back(i);
    }

    // 각 순열에서 처리해야할 일
    do {
        int sum = 0;
        bool back = true;
        for (int i = 0; i < n-1; i++) { // 바로 next 도시와의 관계 check
            if (cost[route[i]][route[i + 1]] != 0) { // 몇번째 도시인지 정보는 route[i]에 담김
                sum += cost[route[i]][route[i+1]];
            }
            else{ 
				back = false;
				break;
			}
        }
        if (back && cost[route[n-1]][route[0]] != 0) { // 마지막 도시와 첫도시 연결
            sum += cost[route[n-1]][route[0]];
            if (ans > sum) ans = sum;
        }
    } while (next_permutation(route.begin() + 1, route.end())); // 다음 순열 호출

    cout << ans << '\n';
    return 0;
}








/*
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
int a[20][20];
int main() {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &a[i][j]);
        }
    }

    vector<int> d(n);
    for (int i = 0; i < n; i++) {
        d[i] = i;
    }

    int ans = 2147483647;

    do {
        bool ok = true;
        int sum = 0;
        for (int i = 0; i < n - 1; i++) {
            if (a[d[i]][d[i + 1]] == 0) {
                ok = false;
            }
            else {
                sum += a[d[i]][d[i + 1]];
            }
        }
        if (ok && a[d[n - 1]][d[0]] != 0) {
            sum += a[d[n - 1]][d[0]];
            if (ans > sum) ans = sum;
        }
    } while (next_permutation(d.begin() + 1, d.end()));

    printf("%d\n", ans);
    return 0;
}
*/
