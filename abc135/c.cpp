
#include <bits/stdc++.h>
using namespace std;

int main()
{
	int  n;

 	cin >> n;
	 	vector<int>a(n+1);
		 vector<int>b(n);
	for (int i = 0; i <= n ; i++)
	{
		cin >> a[i];
	}
	for (int i = 0; i < n ; i++)
	{
		cin >> b[i];
	}
	long long  ans = 0;

	for(int i = 0; i < n; i++){
		if(a[i] >= b[i]){
			ans += b[i];
		}else{
			b[i]-= a[i];
			ans += a[i];
			if(a[i+1] >= b[i]){
				a[i+1] -= b[i];
				ans += b[i];
			}else{
				ans += a[i+1];
				a[i+1] = 0;
			}

		}
	}
	cout << ans << endl;

	return 0;
}
