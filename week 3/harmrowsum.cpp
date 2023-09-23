#include <iostream>
using namespace std;

int main()
{
    cout.precision(1000);
    float sum1=0;
    for (float i=1; i<9999999; i++)
    {
        sum1+=1/i;
    }
    cout<<sum1<<endl;
    double sum2=0;
    for (double i=1; i<9999999; i++)
    {
        sum2+=1/i;
    }
    cout<<sum2<<endl;
    //Точность у этих двух типов данных разная - double точнее и занимает в 2 раза большую ячейку памяти
    cout<<"Size of float = "<<sizeof(float)<<" bytes"<<endl;
    cout<<"Size of double = "<<sizeof(double)<<" bytes"<<endl;

    return 0;
}
