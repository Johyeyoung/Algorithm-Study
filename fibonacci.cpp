#include <iostream>

using namespace std;






int main(){
    
    int arr [40][2]; 
    int t;
    cin>> t;
    
    for(int k=0;k<t;k++){
    int n;
    cin>>n;
    
    arr[0][0]=1;
    arr[0][1]=0;
    arr[1][0]=0;
    arr[1][1]=1;
    
  
    
    
    for(int i=2 ;i<= n;i++){
        arr[i][0]=arr[i-1][0]+arr[i-2][0];
        arr[i][1]=arr[i-1][1]+arr[i-2][1];
    }
    
    cout << arr[n][0] <<" "<<arr[n][1]<<endl;
    
    }    
    
    return 0;
}
