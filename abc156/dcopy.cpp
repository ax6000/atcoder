#include <iostream>
#include <cmath>
using namespace std;
typedef long long ll;
#define MOD 1000000007

ll calc(ll a, ll b, ll p) {
    if (b == 0) {
        return 1;
    } else if (b % 2 == 0) {
        ll d = calc(a, b / 2, p);
        return (d * d) % p;
    } else {
        return (a * calc(a, b - 1, p)) % p;
    }
}

ll modPow(long long a, long long n, long long p) {
  if (n == 1) return a % p;
  if (n % 2 == 1) return (a * modPow(a, n - 1, p)) % p;
  long long t = modPow(a, n / 2, p);
  return (t * t) % p;
}

ll modFact(int n,int from){
    ll ret = 1;
  // cout << "##factrial start## "<< from << endl;
    for(int i = from; i <= n; i++){
        ret = ret * i % MOD;
    }
    //cout << "##factrial end## " << ret << endl;
    return ret;
}

ll combn(int n,int r){
   ll num = modFact(n, n-r+1);
   ll tmp;
  // cout << "numn "<< num << endl;

    tmp = modFact(r, 1);
    tmp = modPow(tmp, MOD - 2, MOD);
    num = num * tmp % MOD;
    return((int)num);
}



int main (){
int n,a,b;
cin >> n >> a >> b ;  
if(n == 2 && a != b){
    cout << 0 << endl;
    return 0;
}
ll cnt = modPow(2,n,MOD) - 1;
// cout << cnt << endl  ;
cnt -= combn(n,a);
cnt -= combn(n,b);
if(cnt < 0)
    cnt += MOD * 2;

cout <<  cnt % MOD << endl;

return 0;
}