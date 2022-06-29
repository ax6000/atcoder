
#include <bits/stdc++.h>
using namespace std;

int main()
{
	int  a;

 	cin >> a;
	 	vector<int>p(a);
	for (int i = 0; i < a ; i++)
	{
		cin >> p[i];
	}
		int first = -1;
		int second = -1;
		for(int i = 1; i <= a; i++){
			if(first == -1 && p[i-1]!= i)
				first = i-1;
			else if(second == -1 && p[i-1]!= i){
				second = i-1;
			}else if(p[i-1] != i){
				cout << "NO" << endl;
				return 0;
			}

		}
	cout << "YES" << endl;

	return 0;
}
