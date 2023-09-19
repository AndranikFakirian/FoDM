#include <iostream>
#include <vector>
#include <iterator>
#include <fstream>
using namespace std;
void fibonacci (int n, vector <int> &v)
{
    int a=1;
    v.push_back(a);
    if (n>1)
    {
        int b=1;
        v.push_back(b);
        if (n>2)
        {
            for (int i=2; i<n; i++)
            {
                if (i%2==1)
                {
                    a+=b;
                    v.push_back(a);
                }
                else
                {
                    b+=a;
                    v.push_back(b);
                }
            }
        }
    }
    v.shrink_to_fit();
}
int main ()
{
    int n;
    cin>>n;
    vector <int> v;
    fibonacci(n, v);
    ofstream f("stdvector.bin", ios::binary);
    for (vector <int>::iterator it=v.begin(); it!=v.end(); it++)
    {
        f<<*it<<endl;
    }
    f.close();
}
