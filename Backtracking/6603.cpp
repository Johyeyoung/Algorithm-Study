#include <iostream>
#include <stdio.h>
#include <vector>
#include <utility>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;
const int MAX = 13;
int arr[MAX];
int lotto[6];
int k;

// lotto의 길이가 6일 때 종료
void printLotto(int l, int n){
	if(n == 6){
		for(int i=0; i<6; i++) printf("%d ", lotto[i]);
		cout << endl;
		return;
	}
	for(int i=l; i<k; i++){
		lotto[n] = arr[i];
		printLotto(i+1, n+1);
	}

}
int main() {
	int n;
	scanf("%d", &k);

	while(k != 0){
			for(int i=0; i<k; i++) cin >> arr[i];

			printLotto(0, 0);
			printf("\n");
			scanf("%d", &k);
	}
	return 0;
}

