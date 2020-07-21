#include <iostream>
#include <stdio.h>
#include <cstring> // memset
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
using namespace std;

vector <int> result;

vector<int> makeTable(string p){
	int len = p.length();
	vector<int> table(len, 0);
	int j=0; // j : 첫 번째 비교 문자, i : 두 번째 부터 비교 문자(값 계속 늘려나감)
	for(int i=1; i<len; i++){  // while : j, i 위치 문자열이 다를 때
		while(j > 0 && p[i] != p[j]){ // j를 하나씩 계속 앞으로 이동하여 확인해봐야하므로
			j = table[j-1]; // 두 문자가 다르다면, j를 앞으로 민다
		}                 // (j-1에 있는 테이블 값으로 j재설정)
		if(p[i] == p[j]){ // 두 문자가 같다면 해당 i의 테이블 값에 j+1값을 저장,
			table[i] = ++j; // j에 1을 더한다.
		}
	}
	return table;
}

void kmp(string parent, string pattern){
	int parentSize = parent.length();
	int patternSize = pattern.length();
	vector <int> table = makeTable(pattern);
	int j = 0;
	for(int i=0; i<parentSize; i++){
		while(j > 0 && parent[i] != pattern[j]){
			j = table[j-1];
		}
		if(parent[i] == pattern[j]){
			if(j == patternSize-1){
				result.push_back(i-patternSize + 2);
				j = table[j];
			}
			else{
				j++;
			}
		}
	}
}

int main() {
	string T,P;
	getline(cin, T);
	getline(cin, P); // 공백도 입력받기 위해

	kmp(T, P);
	printf("%d\n", result.size());
	for(int i=0; i<result.size(); i++) printf("%d ", result[i]);
	printf("\n");

	return 0;
}
