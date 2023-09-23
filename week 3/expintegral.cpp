#include <iostream>
#include <cmath>
#include "windows.h"
using namespace std;

double eint(double x)
{
    return (1/exp(x*x)+1/exp((x+1)*(x+1)))/2;
}
int main()
{
    cout.precision(1000);
    double integral=0;
    double integral1=0;
    cout<<"Split length = 1"<<endl;
    for (double i=0; i<999; i++)
    {
        integral+=eint(i);
        cout<<"On the segment [0;"<<i<<"] integral = "<<integral<<flush<<endl; //Сходимость ряда доказывается его сравнением с рядом 1/n^2, который сходится как эталон
        if (integral==integral1)
        {
            cout<<"Final iteration = "<<i-1<<endl;
            break;
        }
        integral1=integral;
    }
    Sleep(5000);
    system("cls");
    integral=0;
    bool a=true;
    for (double i=999; i>-1; i--)
    {
        integral+=eint(i);
        if ((integral!=0)&&a)
        {
            cout<<"Initial iteration = "<<i<<endl;
            cout<<"Split length = 1"<<endl;
            a=!a;
        }
        if (!a)
        {
            cout<<"On the segment ["<<i<<"; 1000] integral = "<<integral<<flush<<endl;
        }
    }

    return 0;
}
