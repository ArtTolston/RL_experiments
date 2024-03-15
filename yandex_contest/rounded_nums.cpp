#include<iostream>
#include<vector>
#include<set>
#include<string>
#include<algorithm>
#include<tuple>
#include<map>

using namespace std;

int main() {
    vector<int> a;
    vector<tuple<float, int, int, int>> diffs;
    map<int, int> solution;
    int n = 0, x = 0, sum = 0, base = 0, floor_num = 0, ceil_num = 0;

    cin >> n;
    cin >> x;

    for(int i = 0; i < n; i++) {
        int num = 0;
        cin >> num;
        a.push_back(num);
        sum += num;
    }

    for(int i = 0; i < n; i++) {
        float bi = 1.0 * a[i] * x / sum;
        if(bi >= 0) {
            base += int(bi);
            diffs.push_back(make_tuple((bi - int(bi)), int(bi), 0, i));
            diffs.push_back(make_tuple((1 + int(bi) - bi), int(bi), 1, i));
        } else {
            base += int(bi) - 1;
            diffs.push_back(make_tuple((bi - (int(bi) - 1)), (int(bi) - 1), 0, i));
            diffs.push_back(make_tuple((1 + (int(bi) - 1) - bi), (int(bi) - 1), 1, i));
        }
    }

    floor_num = x - base;
    ceil_num = n - floor_num;

    sort(diffs.begin(), diffs.end(), [](const auto& p1, const auto& p2) { return get<0>(p1) > get<0>(p2); });


    for(int i = 2 * n - 1; i >= 0; i--) {
        tuple<float, int, int, int> t = diffs[i];
        if(solution.find(get<3>(t)) == solution.end()) {
            if((get<2>(t) == 0) && (ceil_num != 0)) {
                solution[get<3>(t)] = get<1>(t);
                ceil_num--;
            } else if((get<2>(t) == 1) && (floor_num != 0)) {
                solution[get<3>(t)] = get<1>(t) + 1;
                floor_num--;
            }
        }

        multiset<int>::iterator s;


    }

    for(const auto& [key, val] : solution) {
        cout << val << " ";
    }

    return 0;
}
