#include<stdio.h>
#include<algorithm>
int RGB[1001][3];// RGB 값이 3개이 때문에 범위 1000의 3개를 잡음 0 = r, 1 = g, 2 = 로 생각  틀림 --> 필요 없음
int dp[1001][3] = { 0 };
int min(int a, int b) {
    return a < b ? a : b;
}


int min(int a, int b, int c) {
    if (a < b)
        return a < c ? a : c;
    else
    {
        return b < c ? b : c;
    }
}


int main()
{
	int i, num;
	int rgb[3] = { 0 };
	
	scanf_s("%d", &num);
	scanf_s("%d %d %d", &rgb[0], &rgb[1], &rgb[2]); //rgb 값 순서대로 r,g,b

	dp[0][0] = rgb[0];
	dp[0][1] = rgb[1];
	dp[0][2] = rgb[2];

	for (i = 1; i < num; ++i)
	{
		scanf_s("%d %d %d", &rgb[0], &rgb[1], &rgb[2]);
		dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + rgb[0];
		dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + rgb[1];
		dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + rgb[2];
	}

	printf("%d", min(min(dp[num - 1][0], dp[num - 1][1]), dp[num - 1][2]));


}
