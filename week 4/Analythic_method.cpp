#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int main(int argc, char* argv[])
{
    float v0, x0, w0, dt, k;
    long it;
    ifstream f1(argv[1], ios::in);
    f1>>w0;
    f1>>x0;
    f1>>v0;
    f1>>dt;
    f1>>it;
    f1.close();
    ofstream f2(argv[2], ios::out);
    float b = x0;
    float a=v0/w0;
    k=w0*w0;
    for (long i=1; i<=it; i++)
    {
        f2<<x0<<' '<<v0<<' '<<v0*v0/2+x0*x0*k/2<<' '<<(i-1)*dt<<endl;
        x0=a*sin(w0*i*dt)+b*cos(w0*i*dt);
        v0=a*w0*cos(w0*i*dt)-b*w0*sin(w0*i*dt);
    }
    f2.close();


    return 0;
}
