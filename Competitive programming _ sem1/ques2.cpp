#include<bits/stdc++.h>
using namespace std;

bool isPrime(int num) {
    if (num < 2) {
        return false;
    }
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) {
            return false;
        }
    }
    return true;
}

void printNAlternatePrimes(int n) {
    int count = 0;
    int num = 2;
    vector<int> primes;

    while (count < n) {
        if (isPrime(num)) {
            primes.push_back(num);
            count++;
            num += 2; // Skip the next prime number
        } else {
            num++;
        }
    }

    for (int i = 0; i < primes.size(); i++) {
        cout << primes[i] << " ";
    }
    cout << endl;
}

int main() {
    int n; cin >> n;
     printNAlternatePrimes(n);

    return 0;
}