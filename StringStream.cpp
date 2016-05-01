#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
   // Complete this function
   vector <int> input;
   stringstream ss(str);
   char ch;
   int i=0;
   while(ss!=NULL)
   {
       input.push_back(0);
       ss>>input[i++]>>ch;
   }
   return input;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}
