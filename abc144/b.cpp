#include <iostream>
using namespace std;
#include <string>
#include <vector>

int main()
{
	int x;
	cin >> x;
	for(int i = 1; i < 10; i++){
		for(int j = 1; j < 10; j++){
			if(x == i * j){
					cout << "Yes" << endl;
					return 0;
			}

		}
	}
	cout << "No" << endl;
	return 0;
}
