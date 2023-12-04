#include <iostream>
#include <fstream>
#include <nlohmann/json.hpp>
#include <vector>
using namespace std;

template <typename T>
int mean(T val)
{
    return (T(0)<val);
}

int main()
{
    float a=1.2;
    cout<<mean(a)<<endl;
    a=0;
    cout<<mean(a)<<endl;
    a=-1.2;
    cout<<mean(a)<<endl;

    return 0;
}
