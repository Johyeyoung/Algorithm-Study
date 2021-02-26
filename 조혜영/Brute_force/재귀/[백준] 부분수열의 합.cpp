/*
===============================================================
                    1882. 부분 수열의 합
===============================================================
*/
#include <iostream>
using namespace std;
int a[20];
int n, m; // 원소의 개수, 지금까지 더한 수
int ans = 0;
// 해당 index꺼 선택할지 말지 
void go(int idx, int sum) {
    if (idx== n) { // 도중에 sum==m이라고 중단되는 경우를 방지, 전체 원소 탐색 
        if (sum == m) {
            ans += 1;
        }
        return;
    }
    // 재귀로 다음 원소 선택여부도 이어서 진행 
    go (idx+1, sum); // 선택 x
    go (idx+1, sum+a[idx]); // 선택 o
}

int main(){
    cin >> n >> m;
    for (int i=0; i<n; i++){
        cin >> a[i];
    }
    go(0, 0);
    if(m == 0) ans -= 1; // 부분수열의 원소의 개수는 무조건 양수!
    cout << ans << '\n';
    return 0;   
}


/* 
===============================================================
                    14225. 부분 수열의 합   
===============================================================
*/
#include <iostream>
using namespace std;
bool c[100000 * 20]; // 부분수열의 합으로 만들 수 check배열
/*
if there is a problem with too large size of array...
sol 1) set을 사용.
sol 2) int d[x]배열에 만든 수를 그냥 다 담고 오름차순한 뒤 다음과 같은 예외를 발견하면 그게 정답. 
       1) d[0] != 1 : 첫번째 원소가 1이 아니라면 1은 만들 수 없는거니까
       2) d[i-1]+1 != d[i] : 오름차순된 상태이므로 다음 숫자와의 비교로
          연속된 숫자인지 확인하고 연속된 수가 아니라면 중간에 못만든 수가 있으니까
          (ans=d[i-1]+1)
*/
int n, m; //수열의 크기, 더한 것의 합 
int a[20];

// 선택을 할지 말지 결정 (조합)
 void go(int idx, int sum){
    if (idx == n){
        c[sum] = true;
        return; // 끝내는 부분
    }
    go(idx+1, sum+a[idx]); // 선택 o
    go(idx+1, sum); // 선택 x
}

int main(){
    cin >> n;
    for (int i=0; i<n; i++) {
        cin >> a[i];
    }
    go(0, 0);
    for (int i=1;; i++) {
        if (c[i] == false) {
            cout << i << '\n';
            break;
        }
    }
    return 0;
}