#include <iostream>
using namespace std;
#include <string>
#include <vector>

int main()
{
	int i;
	string s;
	cin >> i >>s;
	

	for (int j = 0; j < s.size(); j++)
	{
		if(s[j] + i > 90){
			s[j] -= 26;
		}
		s[j] += i;
		/* code */
	}
	
	cout << s << endl;
	return 0;
}
