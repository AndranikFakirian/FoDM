#include <iostream>
#include <fstream>
using namespace std;

void f(string a = "Anno")
{
    cout<<a<<endl;
}

int main()
{
    f();
    f("Hans, let the gas go!");

    return 0;
}
