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
#include <windows.h>
#include <iterator>
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

int DiscrStep (float PB, float R)
{
    int S[2]={-1, 1};
    if (R<PB)
    {
        return S[0];
    }
    else
    {
        return S[1];
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
    int NumSteps0=js1["N0"];
    int NumSteps1=js1["N1"];
    int StepNumSteps=js1["SN"];
    int Rep=js1["R"];
    float PB=js1["PB"];
    int Bords=js1["B"];
    vector <vector <int>> Coordss;
    f1.close();
    int NumSteps=NumSteps0;
    int Num0Steps=0;
    while (NumSteps<NumSteps1) {
        vector <int> Coords;
        for (int i = 0; i < Rep; i++) {
            int Coord=0;
            if (!Coordss.empty())
            {
                Coord=(*(Coordss.end()-1))[i];
            }
            for (int j = Num0Steps; j < NumSteps; j++) {
                uniform_real_distribution<float> uniform_dist(0, 1);
                float R = uniform_dist(e1);
                Coord += DiscrStep(PB, R);
            }
            Coords.push_back(Coord);
        }
        Coords.shrink_to_fit();
        Coordss.push_back(Coords);
        Num0Steps=NumSteps;
        NumSteps+=StepNumSteps;
    }
    Coordss.shrink_to_fit();
    ofstream f2(argv[2]);
    json js2={};
    js2["Coordss"]=Coordss;
    f2<<js2;
    f2.close();

    return 0;
}