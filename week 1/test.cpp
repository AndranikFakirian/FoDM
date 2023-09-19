#include <iostream>
#include <fstream>
using namespace std;

int main (int argc, char* argv[])
{
    ofstream f("test.txt", ios::out);
    string a=argv[1];
    int n=stoi(a);
    for (int i=1; i<=n; i++)
    {
        f<<i<<' ';
    }
    f.close();

    return 0;
}
