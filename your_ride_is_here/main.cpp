#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int Product(string s) {
    long long res = 1;
    for (auto c : s) {
        res *= c - 'A' + 1;
    }
    return res % 47;
}

string Solve(const string s1, string s2) {
    return (Product(s1) == Product(s2)) ? "GO" : "STAY";
}

int main() {
    ofstream fout("ride.out");
    ifstream fin("ride.in");

    if (!fin.good()) {
        cout << "Exception opening/reading file";
        return EXIT_FAILURE;
    }
    string s1, s2;
    fin >> s1 >> s2;
    fout << Solve(s1, s2) << '\n';
    return EXIT_SUCCESS;
}