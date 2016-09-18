#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    long long int N, K;
    cin>>N;
    cin>>K;
    vector <long long int> A (N);
    vector <long long int> zeros;
    for (long long int i = 0; i < N; i++)
    {
        cin >> A[i];
        if (A[i] == 0)
            zeros.push_back(i);
    }
    
    for (long long int kk = 0; kk < K; kk++)
    {
        int type;
        cin >> type;
        if (type == 1)
        {
            long long int ind;
            cin >> ind;
            if (zeros.size() >= ind)
                cout<<zeros[ind-1]<<endl;
            else
                cout<<"NO"<<endl;
        }
        else
        {
            long long int ind, change;
            cin >> ind;
            cin >> change;
            if (A[ind] == 0 && change != 0)
            {
                A[ind] = change;
                zeros.erase(std::remove(zeros.begin(), zeros.end(), ind), zeros.end());
            }
            else if (A[ind] != 0 && change == 0)
            {
                A[ind] = change;
                if (zeros.size() == 0 || ind > zeros[zeros.size()-1])
                    zeros.push_back(ind);
                else if (ind < zeros[0])
                    zeros.insert(zeros.begin()+0, ind);
                else
                {
                    for (long long int i = 1; i < zeros.size(); i++)
                    {
                        if (zeros[i-1] < ind && zeros[i] > ind)
                        {
                            zeros.insert(zeros.begin()+i, ind);
                            break;
                        }
                    }
                }
            }
        }
    }
    return 0;
}
