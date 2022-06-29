#include <iostream>
using namespace std;
#include <string>
#include <vector>
#include <cmath>

int c(long nb){
	int cnt = 1;
	while(nb > 9){
		nb /= 10;
		cnt += 1;
	}
	return cnt;

}

long long binary_search(long long a,long long b,long long x) {
   long long  left = 0;
	long long right = (long)pow(10,9) + 1;
    /* どんな二分探索でもここの書き方を変えずにできる！ */
    while (right - left > 1) {
        long long mid = left + (right - left) / 2;
        if (a * mid + b * c(mid) > x) right = mid;
        else left = mid;
    }

    /* left は条件を満たさない最大の値、right は条件を満たす最小の値になっている */
    return left;
}

int main()
{
	long long a,b;
	long  long x;
	cin >> a >>b >> x;
	cout << binary_search(a,b,x) << endl;
	return 0;
}
