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

ll modFact(ll n){
    ll ret = 1;
   cout << "##factrial## " << endl;
    for(int i = 1; i <= n; i++){
        ret = ret * i % MOD;
    }
    cout << "##factrial## " << ret << endl;
    return ret;
}

ll combn(int n,int r){
   ll num = modFact(n);
   ll tmp;
   cout << "numn "<< num << endl;
    // for(int i = 1; i <= r; i++){
    //     tmp = modPow(i, MOD - 2, MOD);
    //    // cout << i<<"tmp " << tmp << endl;
    //     //cout <<i << "num " << num << endl;
    //     num = num * tmp % MOD;
    //  //   cout << "num  after " << num << endl;
    // }
    // cout << "num n/n "<< num << endl;
    //    for(int i = 1; i <= n-r; i++){
    //     tmp = modPow(i, MOD - 2, MOD);
    //     //cout << i<<"tmp " << tmp << endl;
    //    // cout <<i << "num " << num << endl;
    //     num *= tmp;
    //     num %= MOD;
    //  //   cout << "num  after " << num << endl;
    // }
    tmp = modFact(r);
    tmp = modPow(tmp, MOD - 2, MOD);
    num = num * tmp % MOD;

    tmp = modPow(modFact(n-r), MOD - 2, MOD);
    num = num * tmp % MOD;
    return((int)num);
}



int main (){
int n,a,b;
cin >> n >> a >> b ;  
if(n == 2){
    cout << 0 << endl;
    return 0;
}
ll cnt = modPow(2,n,MOD) - 1;
// cout << cnt << endl  ;
cnt -= combn(n,a);
cnt -= combn(n,b);
if(cnt < 0)
    cnt += MOD;

cout <<  cnt % MOD << endl;

return 0;
}