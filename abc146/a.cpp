#include <iostream>
using namespace std;
#include <string>
#include <vector>

int main()
{
	string s;
	cin >> s;
	int i;
	int cnt = 0;
	string ss[7]={"MON","TUE","WED","THU","FRI","SAT","SUN"};
	for(i = 0; i < 6; i++){
		if(!(s.compare(ss[i])))
			break;
	}
	for (int j = i; j < 6; j++)
	{
		cnt++;
		/* code */
	}
	
	if(!s.compare("SUN")) cnt +=7;
	cout << cnt << endl;
	return 0;
}
