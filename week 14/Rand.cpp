#include <cmath>
#include <iomanip>
#include <iostream>
#include <fstream>
#include <map>
#include <random>
#include <string>
#include <ctime>
#include <nlohmann/json.hpp>
using namespace std;
using json=nlohmann::json;

template <class R>
void newSeed(R &r)
{
    auto T=time(nullptr);
    r.seed(T);
    ofstream sd("Seed.json");
    json jsd={};
    jsd["S"]=T;
    sd<<jsd;
    sd.close();
}

template <class R>
void lastSeed(R &r)
{
    ifstream sd("Seed.json");
    json jsd=json::parse(sd);
    r.seed(jsd["S"]);
}
int main()
{
    //random_device r;
    linear_congruential_engine<unsigned int, 48271, 0, 2147483647> r;
    newSeed<linear_congruential_engine<unsigned int, 48271, 0, 2147483647>> (r);
    //lastSeed<linear_congruential_engine<unsigned int, 48271, 0, 2147483647>> (r);
    cout<<time(nullptr)<<endl;
    default_random_engine e1(r());
    int k;
    int n;
    cin>>n;
    cin>>k;
    for (int i=0; i<n; i++)
    {
        uniform_int_distribution<int> uniform_dist(1, k);
        int mean = uniform_dist(e1);
        cout<<mean<<' ';
    }

    return 0;
}
//3 1 1 2 1 3
//
