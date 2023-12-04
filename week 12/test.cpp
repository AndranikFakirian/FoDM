#include <iostream>
#include <fstream>
#include <nlohmann/json.hpp>
#include <vector>
using namespace std;
using json=nlohmann::json;

int main()
{
    ifstream f1("ttjs.json");
    json js=json::parse(f1);
    f1.close();
    cout<<js["params"]<<endl;
    vector <int> v = js["params"];
    for (auto &i: v)
    {
        cout<<i<<' ';
    }
    js["SOX"]="YES!";
    ofstream f2("ttjsc.json");
    f2<<js.dump();
    f2.close();

    return 0;
}
