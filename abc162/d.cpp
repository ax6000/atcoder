#include <iostream>
#include <string>

using namespace std;

int main(){
	int n;
	string x;
	long long cnt;
	cin >> n; 
	cin >> x;
	cnt = 0;
	bool dp[n][n];

	for (int  i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			dp[i][j] = !(x[i] == x[j]);
			cout << (x[i] == x[j]) ? 1 : 0;
		}
		cout << endl;
				/* code */
	}
		
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n && j < i; j++)
		{	
			if(!dp[i][j])
				continue;
			for (int k = 0; k < n && k < j; k++)
			{
				if(2 * (j + 1) ==  i + k + 2 )
					continue;
				if(dp[i][j] && dp[j][k] && dp[k][i]){
					// cout << x[i] << x[j] << x[k] << endl;
					// cout << i+1 << ':'<<  j+1 << ':'<< k+1<< endl;
					cnt++;
				}
				
			}		
		}
	}
	cout << cnt << endl;
	return 0;
	
}
