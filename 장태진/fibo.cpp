#include<stdio.h>
//int z = 0;// 0에 대한 변수 피보나치만을 사용했다 틀림
//int O = 0; // 1에 대한 변수
int data[100] = {1,1,}; //메모이제이션을 사용하기 위한 초기화

int fibo(int n);

int main() {
	int check; // 몇개 알아 볼지 체크 변수
	int f; // fibo에서 0이랑 1의 개수를 알아볼 변수
	scanf_s("%d", &check);
	for (int i = 0; i < check; i++)
	{
		scanf_s("%d", &f);
		if (f == 0)
		{
			printf("1 0\n");
		}
		else if (f == 1)
			printf("0 1\n");
		else {
			fibo(f);
			printf("%d %d\n", data[f - 2], data[f - 1]);
		}
	}
}

int fibo(int n) {
	if (n <= 2)
		return data[n - 1];
	else if (data[n - 1] > 0)
		return data[n - 1];
	else {
		data[n-1]= fibo(n - 1) + fibo(n - 2);
		return data[n - 1];
	}
}
