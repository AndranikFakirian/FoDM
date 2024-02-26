#include <cmath>
#include <iomanip>
#include <iostream>
#include <fstream>
#include <map>
#include <random>
#include <string>
#include <ctime>
#include <nlohmann/json.hpp>
#include <set>
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
int main(int argc, char* argv[])
{
    if (argc != 3){
        cerr << "ivalid input arguments" << endl;
        cout << "ivalid input arguments" << endl;
        exit(1234);
    }
    ifstream f1(argv[1]);
    json js1=json::parse(f1);
    //random_device r;
    linear_congruential_engine<unsigned int, 48271, 0, 2147483647> r;
    newSeed<linear_congruential_engine<unsigned int, 48271, 0, 2147483647>> (r);
    //lastSeed<linear_congruential_engine<unsigned int, 48271, 0, 2147483647>> (r);
    //cout<<time(nullptr)<<endl;
    default_random_engine e1(r());
    int k=js1["K"];
    int n=js1["N"];
    int rep=js1["R"];
    set <int> chcklist;
    for (int i=1; i<=k; i++)
    {
        chcklist.insert(i);
    }
    f1.close();
    //vector <int> res;
    int num=0;
    for (int i=0; i<rep; i++)
    {
        set <int> list;
        for (int j=0; j<n; j++)
        {
            uniform_int_distribution<int> uniform_dist(1, k);
            int mean = uniform_dist(e1);
            //res.push_back(mean);
            list.insert(mean);
            if (list==chcklist)
            {
                num++;
                break;
            }
        }
    }
    //res.shrink_to_fit();
    double pb=double(num)/double(rep);
    ofstream f2(argv[2]);
    json js2={};
    js2["PB"]=pb;
    f2<<js2;
    f2.close();

    return 0;
}