#include <iostream>
#include <cmath>
#include "windows.h"
using namespace std;

double factorial(unsigned long n)
{
    double f=1;
    for (unsigned long i=2; i<n; i++)
    {
        f*=i;
    }
    return f;
}
double MLSin(double x, unsigned long n)
{
    double o;
    if (n%2==0)
    {
        o=1;
    }
    else
    {
        o=-1;
    }
    return o*pow(x, 2*n+1)/factorial(2*n+1);
}
int main()
{
    cout.precision(1000);
    double x;
    double sum=0;
    double sum1=0;
    cin>>x;
    for (unsigned long i=0; i<1000; i++) //Начиная где-то с i>1000 для x>=2 результат - nan
    {
        sum+=MLSin(x, i);
        if (sum==sum1)
        {
            cout<<"Final iteration = "<<i-1<<endl;
            break;
        }
        sum1=sum;
    }
    cout<<"Experimental McLauren sin = "<<sum<<endl;
    cout<<"Cmath sin = "<<sin(x)<<endl; //Область сходимости этого степенного ряда: lim {n->+inf} |Cn/Cn+1|=lim {n->+inf} |n+1|=+inf
    Sleep(5000);
    system("cls");
    sum=0;
    bool a=true;
    for (unsigned long i=999; i>-1; i--)
    {
        sum+=MLSin(x, i);
        if ((sum!=0)&&a)
        {
            cout<<"Initial iteration = "<<i<<endl;
            a=!a;
        }
    }
    cout<<"Experimental McLauren sin = "<<sum<<endl;
    cout<<"Cmath sin = "<<sin(x)<<endl;

    return 0;
}
