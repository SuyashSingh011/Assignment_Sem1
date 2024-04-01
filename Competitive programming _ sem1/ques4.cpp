#include<bits/stdc++.h>
using namespace std;

int calculateModularExponentiation(int a, int b, int m) {
    int result = 1;

    while (b > 0) {
        if (b % 2 == 1) {
            result = (result * a) % m;
        }
        a = (a * a) % m;
        b /= 2;
    }

    return result;
}

int main() {
    int a, b, m;
   cin>>a>>b>>m;

    int result = calculateModularExponentiation(a, b, m);
    cout<< result << endl;

    return 0;
}