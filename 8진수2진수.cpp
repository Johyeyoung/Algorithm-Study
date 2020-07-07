#include <iostream>
#include <string>
#include <cmath>
using namespace std;

/* 주어지는 수의 길이는 333,334을 넘지 않는다 
// => 8진수 -> 10진수 -> 2진수로 푸는 방법은 오버플로우 발생 가능성 있음
// => string형으로 다룸 
*/

string octTobin(string s) {
	string result = "";
	for (int i = 0; i < s.length(); i++) {
		string tmp = "";
		switch (s[i])
		{
		case '0':{
				if (i == 0) {
					tmp = "0";
				}
				else {
					tmp = "000";
				}

				break;
			}
		case '1': {
			if (i == 0) {
				tmp = "1";
			}
			else {
				tmp = "001";
			}

			break;
		}
		case '2': {
			if (i == 0) {
				tmp = "10";
			}
			else {
				tmp = "010";
			}

			break;
		}
		case '3': {
			if (i == 0) {
				tmp = "11";
			}
			else {
				tmp = "011";
			}

			break;
		}
		case '4':
			tmp = "100";
			break;
		case '5':
			tmp = "101";
			break;
		case '6':
			tmp = "110";
			break;
		case '7':
			tmp = "111";
			break;

		default:
			break;
		}
		result += tmp;
	}
	return result;
}


int main() {
	string s;
	cin >> s;
	cout << octTobin(s) << endl;

	return 0;
}
