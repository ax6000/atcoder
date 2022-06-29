
#include <bits/stdc++.h>
using namespace std;

int main()
{
	long double a,b,x;
	cin >> a >> b >> x;

	long  double tantheta = (a*b*b)/(2.0*x);
	tantheta = atan(tantheta) * 180.0 / M_PI;
	cout << fixed;
	cout << setprecision(8) << tantheta << endl;
	return 0;
}
