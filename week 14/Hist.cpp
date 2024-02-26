#include <cmath>
#include <iomanip>
#include <iostream>
#include <fstream>
#include <map>
#include <random>
#include <string>
#include <ctime>
#include <nlohmann/json.hpp>
#include <vector>
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

template <typename T>
class Hist
{
private:
    vector <vector<int>> hist;
    int buckets;
    int bsize;
    int minval;
    int maxval;
public:
    Hist(vector <T> vals, int buckets): buckets(buckets), minval(int(floor(*min_element(vals.begin(), vals.end())))), maxval(int(ceil(*
            max_element(vals.begin(), vals.end()))))
    {
        hist.resize(2);
        hist[0].resize(buckets);
        hist[1].resize(buckets);
        int dval=maxval-minval;
        if (dval%buckets==0)
        {
            bsize=dval/buckets;
        } else {
            bsize=dval/buckets+1;
        }
        for (int i=0; i<buckets; i++)
        {
            hist[0][i]=minval+i*bsize;
        }
        for (auto &i: vals)
        {
            hist[1][floor((i-T(minval))/T(bsize))]++;
        }
    }
    vector <vector <int>> getHist()
    {
        return hist;
    }
};

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
    vector<int> vals;
    for (int i=0; i<n; i++)
    {
        uniform_int_distribution<int> uniform_dist(1, k);
        vals.push_back(uniform_dist(e1));
    }
    vals.shrink_to_fit();
    int buckets;
    cin>>buckets;
    Hist<int> h(vals, buckets);
    vector <vector <int>> hist=h.getHist();
    for (int i=0; i<2; i++)
    {
        for (auto &j: hist[i])
        {
            cout<<j<<' ';
        }
        cout<<endl;
    }

    return 0;
}
