#include<iostream>
#include<vector>
#include<set>
#include<string>
#include<map>

using namespace std;

int main() {
    map<int, int> d;

    d[2] =5;
    d[1] = 6;
    d[0] = 1;
    d[3] = 8;

    for(const auto& [key, val] : d) {
        cout << key << " : " << val << endl;
    }

    cout << int(-1.7);
}
