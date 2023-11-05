#include <iostream>
#include <vector>
#include <fstream>
using namespace std;
template <typename T>
vector <T> operator +(vector <T> &a, vector <T> &b)
{
    bool t=true;
    int N=0;
    int N1=0;
    if (a.size()>b.size())
    {
        N1=b.size();
        N=a.size();
    }
    else
    {
        N=b.size();
        N1=a.size();
        t=!t;
    }
    vector <T> c;
    for (int i=0; i<N; i++)
    {
        if (i>=N1)
        {
            if (t)
            {
                c.push_back(a[i]);
            }
            else
            {
                c.push_back(b[i]);
            }
        }
        else
        {
            c.push_back(a[i]+b[i]);
        }
    }
    return c;
}

template <typename Q, typename P>
vector <Q> operator *(P k, vector <Q> a)
{
    vector <Q> b;
    for (auto &i: a)
    {
        b.push_back(k*i);
    }
    return b;
}

template <typename Q, typename P>
vector <Q> operator *(vector <Q> a, P k)
{
    vector <Q> b;
    for (auto &i: a)
    {
        b.push_back(k*i);
    }
    return b;
}

int main()
{
    vector <float> a={1, 2.2, 3};
    vector <float> b={1, 2.2};
    int k=2;
    vector <float> c=a+b;
    for (auto &i: c)
    {
        cout<<i<<' ';
    }
    cout<<endl;
    c=k*c;
    for (auto &i: c)
    {
        cout<<i<<' ';
    }
    cout<<endl;
    c=c*k;
    for (auto &i: c)
    {
        cout<<i<<' ';
    }

    return 0;
}
