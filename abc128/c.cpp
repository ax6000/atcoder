
#include <iostream>
using namespace std;
#include <string>
#include <algorithm>
#include <vector>

int main()
{
	int n,m;
	cin >> n >> m;
	vector<int> kk(m);
	vector<vector<int>> s(m,vector<int>(m));
	vector<int> pp(m);
	int zero[10] = {1,2,2,3,3,4,4,5,5,6};
	int one[10]= {1,1,2,2,3,3,4,4,5,5};
	for (int i = 0; i < m; i++)
	{
		cin >> kk[i];
		for (int j = 0; j < kk[i]; j++)
		{
			/* code */
			cin >> s[i][j];
		}
		
	}
	for (int i = 0; i < m; i++)
	{
		cin >> pp[i];
		/* code */
	}
	int ans = 0;

	for (int i = 0; i < 2; i++)
	{
		for (int j = 0; j < 2; j++)
		{
			for (int k = 0; k< 2; k++)
			{
				for (int l = 0; l< 2; l++)
				{
					for (int mm = 0; mm< 2; mm++)
					{
						for (int nn = 0; nn< 2; nn++)
						{
							for (int o = 0; o< 2; o++)
							{
								for (int p = 0; p< 2; p++)
								{
									for (int q = 0; q< 2; q++)
									{

										for (int r = 0; r< 2; r++)
										{
											int swit[10] ={i,j,k,l,mm,nn,o,p,q,r};
											for(int a = 0; a < m; a++){
												int x = 0;
												for(int b = 0;b < kk[a]; b++){
													x ^= swit[kk[b] -1];
												}
												if(x != pp[a]){
													break;
												}
												if(a == m-1)
													ans++;
			}
			}
				
			}
				
			}
			}
				
			}
				
			}
				
			}
		}
	}
	}
	for(int i = n ; i < 10; i++){
		ans /= 2;
	}
	cout << ans << endl;

	
}
