/*
===============================================================
              11053번 - 가장 긴 증가하는 부분 수열
===============================================================
시간복잡도 )
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
    vector<int> d(n);
    for (int i=0; i<n; i++) {
        d[i] = 1;
        for (int j=0; j<i; j++) {
            if (a[j] < a[i] && d[j]+1 > d[i]) {
                d[i] = d[j]+1;
            }
        }
    }
    
    cout << *max_element(d.begin(),d.end()) << '\n';
    return 0;
}
