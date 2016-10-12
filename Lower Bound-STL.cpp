#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
   int m, num;
   cin >> m;
   vector <int> v(m);
   for (int i = 0; i < m; i++)
       cin >> v[i];
   int n, val;
   cin >> n;
   for (int i = 0; i < n; i++)
   {
       cin >> val;
       vector <int>::iterator low = lower_bound(v.begin(), v.end(), val);
       if (v[low - v.begin()] == val)
           cout << "Yes " << (low - v.begin() + 1) << endl;
       else
           cout << "No " << (low - v.begin() + 1) << endl;
   }
   return 0;
}
