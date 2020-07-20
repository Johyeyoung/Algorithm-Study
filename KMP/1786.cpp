#include <iostream>
#include <stdio.h>
#include <cstring> // memset
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
using namespace std;

vector<int> makeTable(string p){
	int len = p.length();
	vector<int> table(len, 0);
	int j=0; // j : 첫 번째 비교 문자, i : 두 번째 부터 비교 문자(값 계속 늘려나감)
	for(int i=1; i<len; i++){
		while(j > 0 && p[i] != p[j]){
			j = table[j-1]; // 두 문자가 다르다면, j를 앞으로 민다.
		}
		if(p[i] == p[j]){ // 두 문자가 같다면 해당 i의 테이블 값에 j+1값을 저장,
			table[i] == ++j; // j에 1을 더한다.
		}
	}
	return table;
}

void kmp(string parent,string pattern){
	vector<int> table = makeTable(pattern);
	int parentSize = parent.size();
	int patternSize = pattern.size();
	int j=0;
	for(int i=0; i<parentSize; i++){
		while(j > 0 && parent[i] != pattern[j]){
			j = table[j-1];
		}
		if(parent[i] == pattern[j]){
			if(j == patternSize-1){
				j = table[j];
			}
			else{
				j++;
			}
		}
	}
}

int main() {
	return 0;
}

