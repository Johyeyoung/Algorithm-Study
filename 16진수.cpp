#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main() {
	string s;
	int result = 0, base = 0, len;
	cin >> s;
	len = s.length();
	for (int i = len-1; i >= 0; i--) {
		switch (s[i])
		{
		case 'A':
		case 'B':
		case 'C':
		case 'D':
		case 'E':
		case 'F':
			result += ((s[i] - '0') - 7) * pow(16, base);
			break;
		default:
			result += (s[i] - '0') * pow(16, base);
			//cout << (s[i] - '0') << " " <<  pow(16, base) << endl;
			break;
		}
		base++;
	}

	cout << result << endl;
	return 0;
}
