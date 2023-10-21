#include <iostream>
#include <vector>
#include <fstream>
#include <map>
using namespace std;

class IntegralSolver
{
private:
    char* input;
    char* output;
    vector <string> equations;
    map <string, float> conditions;
    map <string, vector <float>> vars;
    int N_eq;
    int N_cond;
public:
    IntegralSolver(char* argv[])
    {
        input=argv[1];
        output=argv[2];
        ifstream f1 (input, ios::in);
        f1>>N_eq;
        for (int i=0; i<N_eq; i++)
        {
            string s="";
            char c;
            f1.get(c);
            for (;(f1.get(c))&&(c!='\n');)
            {
                if (c!=' ')
                {
                    s=s+c;
                }
            }
            equations.push_back(s);
        }
        f1>>N_cond;
        for (int i=0; i<N_cond; i++)
        {
            string s="";
            char c;
            f1.get(c);
            for (;(f1.get(c))&&(c!='\n');)
            {
                s=s+c;
            }
            string key="";
            bool a=true;
            string sval="";
            float val;
            for (auto &i: s)
            {
                if (a)
                {
                    if ((i!=' ')&&(i!=' '))
                    {
                        key=key+i;
                    }
                    else
                    {
                        a=!a;
                    }
                }
                else
                {
                    if ((i!=' ')&&(i!='='))
                    {
                        sval=sval+i;
                    }
                }
            }
            val=stof(sval);
            conditions.insert({key, val});
        }
        f1.close();
    }
    ~IntegralSolver()
    {
        delete [] input;
        delete [] output;
    }
    vector <float> func();
    int findinstr(string s, string f)
    {
        //for (int i=0; i
    }
    void Euler_method()
    {
        vector <float>
    }
};
int main(int argc, char* argv[])
{
    IntegralSolver I(argv);
    I.print();

    return 0;
}
