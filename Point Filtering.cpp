#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    long long int N, b;
    cin >> N;
    cin >> b;
    vector <bool> in_b (N);
    vector <vector <double>> points (N, vector<double> (4, 0 ));
    vector <vector <double>> sorted_points (N, vector<double> (4, 0 ));
    for (long long i = 0; i < N; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            cin >> points[i][j];
            sorted_points[i][j] = points[i][j];
        }
    }
    struct pred1 {
    bool operator()(vector <double> const & a, vector <double> const & b) const {
        return a[0] < b[0];
    }
    };
    struct pred {
    bool operator()(vector <double> const & a, vector <double> const & b) const {
        return a[3] > b[3];
    }
    };
    sort(points.begin(), points.end(), pred1());
    sort(sorted_points.begin(), sorted_points.end(), pred());
    for (long long i = 0; i < b; i++)
        in_b[(int)(sorted_points[i][0])-1] = true;
    long long to_use = b;

    char ty;
    
while (cin >> ty)
{
    
    long long int ind;
    cin >> ind;
    if (ty == 'F' || ty == 'f')
    {
        if (in_b[ind-1])
            cout << ind << " = (" << fixed  <<  setprecision(3) << round(points[ind-1][1] * 1000.0) / 1000.0 << "," << round(points[ind-1][2] * 1000.0) / 1000.0 << "," << round(points[ind-1][3] * 1000.0) / 1000.0 << ")" <<endl;
        else
            cout << "Point doesn\'t exist in the bucket." <<endl;
    }
    else
    {
        if (in_b[ind-1])
        {
            if (to_use >= N)
                cout << "No more points can be deleted."<<endl;
            else
            {
                in_b[ind-1] = false;
                in_b[(int)(sorted_points[to_use][0])-1] = true;
                to_use ++;
                cout << "Point id "+ to_string(ind) +" removed." << endl;
            }
        }
        else
            cout << "Point doesn\'t exist in the bucket." << endl;
    }
}
    return 0;
}
