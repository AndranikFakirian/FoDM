#include <iostream>
#include <cmath>
using namespace std;

int main ()
{
    int n;
    cin>>n;
    int* p = new int[n];
    for (int i=0;; i++)
    {
        p[int(pow(2, i))]=1; //Sigsegv (source: valgrind), cure - STL methods
        cout<<' '<<int(pow(2, i));
    }

    delete [] p;
    return 0;
}
