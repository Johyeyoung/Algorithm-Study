#include <iostream>
#include <stdio.h>
#include <cstring> // memset
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
using namespace std;

int memo0[41];
int memo1[41];

// fibo(n) = fibo(n-1) + fibo(n-2) 이므로 n-1의 0, 1의 개수 + n-2의 0, 1의 개수
void fibo(int n){
	memo0[0] = 1;
	memo1[0] = 0;

	memo0[1] = 0;
	memo1[1] = 1;

	for(int i=2; i<=n; i++){
		memo0[i] = memo0[i-1] + memo0[i-2];
		memo1[i] = memo1[i-1] + memo1[i-2];
	}
}
int main() {
	int T, N;
	cin >> T;
	for(int testCase=0; testCase<T; testCase++){
		cin >> N;
		memset(memo0, 0, sizeof(memo0));
		memset(memo1, 0, sizeof(memo1));
		fibo(N);
		printf("%d %d\n", memo0[N], memo1[N]);

	}

	return 0;
}
