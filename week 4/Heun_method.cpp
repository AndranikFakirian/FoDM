#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char* argv[])
{
    double v0, v1, x0, x1, w0, dt, t;
    t=0;
    long it;
    ifstream f1(argv[1], ios::in);
    f1>>w0;
    f1>>x0;
    f1>>v0;
    f1>>dt;
    f1>>it;
    f1.close();
    ofstream f2(argv[2], ios::out);
    for (long i=0; i<it; i++)
    {
        f2<<x0<<' '<<v0<<' '<<t<<endl;
        x1=x0+dt/2*(2*v0-w0*w0*x0*dt);
        v1=v0+dt/2*(-w0*w0*(2*x0+dt*v0));
        t+=dt;
        x0=x1;
        v0=v1;
    }
    f2.close();

    return 0;
}
