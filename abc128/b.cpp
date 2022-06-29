#include <iostream>
using namespace std;
#include <string>
#include <algorithm>
#include <vector>

struct test
{
	int num;
	string name;
	int score;

	bool operator<( const test& right ) const {
        return  name.compare(right.name) == 0 ? score > right.score : name.compare(right.name) < 0 ;
    }

};

int main()
{
	int n;
	cin >> n;
	vector<test> v(n);
	for (int i = 0; i < n; i++)
	{
		/* code */
		v[i].num = i + 1;
		cin >> v[i].name >> v[i].score;
	}

	sort(v.begin(),v.end());
	for (int i = 0; i < n; i++)
	{
		cout << v[i].num << endl;
		/* code */
	}
	
	

	
}
