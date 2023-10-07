#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int main(int argc, char* argv[])
{
    double v0, x0, w0, dt;
    long it;
    ifstream f1(argv[1], ios::in);
    f1>>w0;
    f1>>x0;
    f1>>v0;
    f1>>dt;
    f1>>it;
    f1.close();
    ofstream f2(argv[2], ios::out);
    double b = x0;
    double a=v0/w0;
    for (long i=1; i<=it; i++)
    {
        f2<<x0<<' '<<v0<<' '<<(i-1)*dt<<endl;
        x0=a*sin(w0*i*dt)+b*cos(w0*i*dt);
        v0=a*w0*cos(w0*i*dt)-b*w0*sin(w0*i*dt);
    }
    f2.close();


    return 0;
}
