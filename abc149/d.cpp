#include <iostream>
using namespace std;
#include <string>
#include <vector>

int rsp_index(string t, int index){
    if(t[index] == 'r')
        return 2;
    else if(t[index] == 's')
        return 0;
    else 
        return 1;
}

int main (){
int n,k,rsp[3],prev,index;
string t; 
cin >> n >> k >> rsp[0] >> rsp[1] >> rsp[2]; 
vector<vector<long>> dp(k+1,vector<long>(n/k));
for (int i = 0; i < k+1; i++)
{
    for (int j = 0; j < n/k; j++)
    {
        dp[i][j] = 0;
    }
    
}

for (int i = 0; i < k+1; i++)
{
    for (int j = 0; j < n/k; j++)
    {
        
        dp[i][j] = 0;
    }
    
}
dp[0][0] = rsp[rsp_index(t,0)];
prev = rsp_index(t,0);
if(k < n)
for (int i = 0; i < k+1; i++)
{
    for (int j = 0; j < n/k; j++)
    {
        index = i * k + j;
        if(t[index] == 0)
            break;
        dp[i][j] = 0;
        prev = rsp_index(t,index);
    }
}
cin >> t;
cout << score << endl;
return 0;
}