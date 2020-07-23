#include <iostream>
using namespace std;

// sol1) 재귀로 풀기 

int result;
void printSumCount(int n){

	if(n == 0){
		result++;
		return;
	}


	if(n-1 >= 0) printSumCount(n-1);
	if(n-2 >= 0) printSumCount(n-2);
	if(n-3 >= 0) printSumCount(n-3);
}

int main() {
	int T,n; cin >> T;

	for(int testCase = 0; testCase < T; testCase++){
		cin >> n;
		result = 0;
		printSumCount(n);
		cout << result << endl;

	}

	return 0;
}
