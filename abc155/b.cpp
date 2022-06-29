#include <iostream>
#include <vector>
#include <map>
using namespace std;

int main (){
    int n,flg;
    flg = 1;
    cin >> n;
    vector<int> a(n);

    for(int i = 0; i < n; i++){
        cin >> a[i];
    }

    for (int j = 0; j < n; j++){
        if(a[j] % 2 == 0){
            if(a[j] % 3 != 0 && a[j] % 5 != 0)
                flg = 0;
        }
    } 

    if(flg)
    cout << "APPROVED" << endl;
    else
    cout << "DENIED" << endl;
    return 0;

}