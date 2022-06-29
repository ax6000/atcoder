#include <iostream>
#include <string>

using namespace std;

int gcd(int a, int b)
{
   if (a%b == 0)
   {
       return(b);
   }
   else
   {
       return(gcd(b, a%b));
   }
}

int main(){
	int x;
	long long cnt;
	cin >> x;
	cnt = 0;
	for (int i = 1; i <= x; i++)
	{
		for (int j = 1; j <= x; j++)
		{
			for (int k = 1; k <= x; k++)
			{
				cnt += (long long)gcd(gcd(i,j),k);
				
			}		
		}
	}
	cout << cnt << endl;
	return 0;
	
}
