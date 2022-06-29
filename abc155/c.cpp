#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

int main (){
    int n,tmp_max,vote_max,vote_cnt;
    cin >> n;
    vote_max = 0; 
    vote_cnt = 0;
    vector<string> most_voted;
    map<string,int> s;
    string tmp;
    for(int i = 0; i < n; i++){
        tmp = "";
        cin >> tmp;
        if(s.count(tmp) == 1){
 //           cout << s[tmp] << endl;
            s[tmp] =s[tmp] + 1;
   //         cout << s[tmp] << endl;
        }
        else
             s.emplace(tmp,1);
        vote_max = max(vote_max, s[tmp]);
    }
 //   cout << "vote_max " << vote_max << endl;
    for(auto itr = s.begin(); itr != s.end(); ++itr) {
        if(itr->second == vote_max)
        most_voted.push_back(itr->first);
    }
    sort(most_voted.begin(),most_voted.end());
    for(auto itr = most_voted.begin(); itr != most_voted.end(); ++itr) {
        cout << *itr << endl;
    }



    return 0;

}