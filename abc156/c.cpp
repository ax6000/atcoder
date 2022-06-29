#include <iostream>
#include <vector> 
#include <algorithm>
#include <cmath>
using namespace std;

int main (){
int n,tmp;

int sum[100];
cin >> n; 
vector<int> x(n);
for(int i = 0; i < n; i++)
    cin >> x[i];
for(int j = 1; j <= 100; j++){
     tmp = 0;
    for(int k = 0; k < n; k++){
       
        tmp += (int)pow((x[k] - j),2);
    }
    sum[j-1] = tmp;
  //  cout << "sum" << j << ": "<< tmp  << endl; 
}
sort(sum, sum + 99);

cout << sum[0] << endl;

return 0;
}