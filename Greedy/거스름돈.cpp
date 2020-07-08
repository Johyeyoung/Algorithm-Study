#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int yen[6] = {500, 100, 50, 10, 5, 1};
	int N, pay = 0, cnt = 0;
	cin >> N;
	pay = 1000 - N;
	for(int i=0; i<6; i++){
		while(yen[i] <= pay){
			pay -= yen[i];
			cnt++;
		}
	}

	cout << cnt << endl;
	return 0;
}
