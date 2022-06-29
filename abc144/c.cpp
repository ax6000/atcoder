

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

vector<long long> divisor(long long n) {
    vector<long long> ret;
    for (long long i = 1; i * i <= n; i++) {
        if (n % i == 0) {
            ret.push_back(i);
            if (i * i != n) ret.push_back(n / i);
        }
    }
  //  sort(ret.begin(), ret.end()); // 昇順に並べる
    return ret;
}

int main()
{
	long long  x,min;
	cin >> x;
	vector<long long> v = divisor(x);

	min = (long long)pow(10,12)+1;
	for(int i = 0; i < v.size(); i++){
		for(int j = 0; j < v.size(); j++){
			if (v[i] * v[j] == x && v[i] + v[j] < min)
				min = v[i] + v[j];
		}
	}

	cout << (min - 2) << endl;
	return 0;
}
