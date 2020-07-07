#include <iostream>
#include <algorithm>

using namespace std;


int main(){

    int dp[1000001];
    
   int t;
   cin>> t;
   
   dp[1]=0;
   
   for(int i=2 ; i<=t ;i++){
       dp[i]=dp[i-1]+1;
        if(i%3==0){dp[i]=min(dp[i/3]+1,dp[i]);}
       else if(i%2==0){dp[i]=min(dp[i/2]+1,dp[i]);}
   
       
       
       
   }
   
   
   
  cout<< dp[t];
  
  
    return 0;
}
