#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char* argv[]) //Заработало только после перемещения этих двух файлов в директорию: libgcc_s_dw2-1.dll libstdc++-6.dll
{
    double v0, x0, w0, dt, t=0, xc=0, vc=0, xy=0, vy=0, xt=0, vt=0;
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
        f2<<x0<<' '<<v0<<' '<<v0*v0/2<<' '<<t<<endl;
        xy=dt*v0-xc;
        vy=dt*(-w0*w0)*x0-vc;
        xt=x0+xy;
        vt=v0+vy;
        xc=(xt-x0)-xy;
        vc=(vt-v0)-vy;
        t+=dt;
        x0=xt;
        v0=vt;
    }
    f2.close();

    return 0;
}
