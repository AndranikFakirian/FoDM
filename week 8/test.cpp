#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

int main(int argc, char* argv[])
{
    ofstream f("tt.txt", ios::out);
    for (int i=1; i<argc; i++)
    {
        f<<argv[i];
    }

    return 0;
}
