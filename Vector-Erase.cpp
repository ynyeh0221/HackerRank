#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int N = 0;
    cin >> N;
    vector <int> A (N);
    for (int i = 0; i < N; i++)
        cin >> A[i];
    int q1 = 0, q2s = 0, q2e = 0;
    cin>>q1;
    A.erase(A.begin() + q1-1);
    cin>>q2s;
    cin>>q2e;
    A.erase(A.begin() + q2s-1, A.begin()+q2e-1);
    cout<<A.size()<<endl;
    for (int i = 0; i < A.size(); i++)
        cout<<A[i]<<" ";
    return 0;
}
