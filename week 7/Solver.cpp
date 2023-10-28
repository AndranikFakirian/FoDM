#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

class System {
protected:
    vector <float> initial_state;
    vector <float> params;
    float dt;
    vector <float> station_derivative;
public:
    System(vector <float> initial_state, vector <float> params, float dt): initial_state(initial_state), params(params), dt(dt) {};
    virtual vector <float> f()=0;
    vector <float> get_initial_state()
    {
        return initial_state;
    }
    vector <float> get_params()
    {
        return params;
    }
    float get_dt()
    {
        return dt;
    }
};

class Sin_oscillator: public System{
public:
    Sin_oscillator(vector <float> initial_state, vector <float> params, float dt): System(initial_state, params, dt) {};
    vector <float> f()
    {
        station_derivative={-pow(params[0], 2)*sin(initial_state[1]), initial_state[0]};
        return station_derivative;
    }
};

template <typename Func>
class Euler_method
{
private:
    float dt;
    float T;
    int iterations;
    vector <vector<float>> states;
    vector <float> params;
    vector <float> state;
public:
    Euler_method (Func &func, float T): T(T)
    {
        this->params=func.get_params();
        this->dt=func.get_dt();
        state=func.get_initial_state();
        states.resize(state.size()+1);
        iterations=int(T/dt)+2;
        for (auto &i: states)
        {
            i.resize(iterations);
        }
        for (int i=0; i<iterations; i++)
        {
            states[0][i]=i*dt;
        }
        for (int i=1; i<states.size(); i++)
        {
            states[i][0]=state[i-1];
        }
    }
    void step()
    {
        Func func(state, params, dt);
        vector <float> temp=func.f();
        for (int i=0; i<state.size(); i++)
        {
            state[i]+=temp[i]*dt;
        }
    }
    void integrate()
    {
        for (int i=1; i<iterations; i++)
        {
            step();
            for (int j=1; j<states.size(); j++)
            {
                states[j][i]=state[j-1];
            }
        }
    }
    vector <vector<float>> result()
    {
        integrate();
        return states;
    }
};

int main()
{
    vector <float> state={0, 1};
    vector <float> params={1};
    float dt=0.1;
    float T=1;
    Sin_oscillator s(state, params, dt);
    Euler_method <Sin_oscillator> E(s, T);
    vector <vector<float>> states=E.result();
    for (auto &i: states)
    {
        for (auto &j: i)
        {
            cout<<j<<' '<<endl;
        }
        cout<<endl;
    }
}
