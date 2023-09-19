#include <iostream>
using namespace std;

int main ()
{
    int n;
    cin>>n;
    for (int i=1; i<=n; i++)
    {
        float j=i;
        cout<<scientific<<1/j<<endl;
    }

    return 0;
}
