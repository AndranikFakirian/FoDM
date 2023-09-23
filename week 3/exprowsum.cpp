#include <iostream>
#include <cmath>
#include "windows.h"
using namespace std;

int main()
{
    cout.precision(1000);
    float sum1=0;
    cout<<"Float"<<endl;
    for (unsigned long i=1; i<29; i++)
    {
        sum1+=1/pow(2, i);
        cout<<"Iteration = "<<i<<" Sum = "<<sum1<<flush<<endl;
    }
    Sleep(5000);
    system("cls");
    double sum2=0;
    cout<<"Double"<<endl;
    for (unsigned long i=1; i<60; i++)
    {
        sum2+=1/pow(2, i);
        cout<<"Iteration = "<<i<<" Sum = "<<sum2<<flush<<endl;
    }

    return 0;
}
