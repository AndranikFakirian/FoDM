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

template <class R>
int fS(vector <R> res, vector <R> phr)
{
    if (res.size()<phr.size())
    {
        return -1;
    }
    vector <R> chck;
    int ps=phr.size();
    int rs=res.size();
    chck.resize(ps);
    for (int i=0; i<ps; i++)
    {
        chck[i]=res[i+rs-ps];
    }
    if (chck==phr)
    {
        return rs;
    }
    else
    {
        return -1;
    }
}
int main(int argc, char* argv[])
{
    ifstream f1(argv[1]);
    json js1=json::parse(f1);
    //random_device r;
    linear_congruential_engine<unsigned int, 48271, 0, 2147483647> r;
    newSeed<linear_congruential_engine<unsigned int, 48271, 0, 2147483647>> (r);
    //lastSeed<linear_congruential_engine<unsigned int, 48271, 0, 2147483647>> (r);
    //cout<<time(nullptr)<<endl;
    default_random_engine e1(r());
    vector <int> voc=js1["Voc"];
    vector <int> phr=js1["Phr"];
    int rep=js1["R"];
    f1.close();
    float al=0;
    for (int i=0; i<rep; i++)
    {
        vector <int> res;
        int num=-1;
        for (; num==-1;)
        {
            uniform_int_distribution<int> uniform_dist(1, voc.size());
            int mean = voc[uniform_dist(e1)-1];
            res.push_back(mean);
            num=fS(res, phr);
        }
        res.shrink_to_fit();
        al+=float(num);
    }
    al=al/float(rep);
    ofstream f2(argv[2]);
    json js2={};
    js2["AvLen"]=al;
    f2<<js2;
    f2.close();

    return 0;
}