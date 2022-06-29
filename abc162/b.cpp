#include <iostream>
#include <string>

using namespace std;

int main(){
	int n;
	long long cnt;
	cin >> n;
	cnt = 0;
	for (int i = 0; i <= n; i++)
	{
		if(i % 3 != 0 && i % 5 != 0){
			cnt += i;
		}
		/* code */
	}
	cout << cnt << endl;
	return 0;
	
}
