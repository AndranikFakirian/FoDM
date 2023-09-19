#include <iostream>
#include <array>
using namespace std;

int main ()
{
    const int n=5;
    array <int, n> arr;
    int a=1;
    arr[0]=a;
    if (n>1)
    {
        int b=1;
        arr[1]=b;
        if (n>2)
        {
            for (int i=2; i<n; i++)
            {
                if (i%2==1)
                {
                    a+=b;
                    arr[i]=a;
                }
                else
                {
                    b+=a;
                    arr[i]=b;
                }
            }
        }
    }
    for (auto i : arr)
    {
        cout<<i<<endl;
    }

    return 0;
}
