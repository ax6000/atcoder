
#include <bits/stdc++.h>
using namespace std;

int main()
{
	int  a,b;
	cin >> a >> b ;
	for (int i = 0; i <=max(a,b); i++)
	{
		if(abs(a - i) == abs(b - i)){
			cout << i<< endl;
			return 0;
		}
		/* code */
	}
	

	cout << "IMPOSSIBLE"<< endl;
	return 0;
}
