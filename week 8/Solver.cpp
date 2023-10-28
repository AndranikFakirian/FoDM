#include <iostream>
#include <fstream>
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
    virtual ~System() {};
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
    virtual ~Sin_oscillator() {};
    vector <float> f()
    {
        station_derivative={-pow(params[0], 2)*sin(initial_state[1]), initial_state[0]};
        return station_derivative;
    }
};

class Low_vibration_oscillator: public System{
public:
    Low_vibration_oscillator(vector <float> initial_state, vector <float> params, float dt): System(initial_state, params, dt) {};
    virtual ~Low_vibration_oscillator() {};
    vector <float> f()
    {
        station_derivative={-pow(params[0], 2)*initial_state[1], initial_state[0]};
        return station_derivative;
    }
};

template <class Func>
class Method
{
protected:
    float dt;
    float T;
    int iterations;
    vector <vector<float>> states;
    vector <float> params;
    vector <float> state;
public:
    Method (Func &func, float T): T(T)
    {
        this->params=func.get_params();
        this->dt=func.get_dt();
        state=func.get_initial_state();
        states.resize(state.size()+1);
        iterations=int(T/dt)+1;
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
    virtual void step()=0;
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

template <class Func>
class Euler_method: public Method <Func>
{
public:
    Euler_method (Func &func, float T): Method <Func>(func, T) {};
    virtual ~Euler_method() {};
    void step()
    {
        Func func(this->state, this->params, this->dt);
        vector <float> temp=func.f();
        for (int i=0; i<this->state.size(); i++)
        {
            this->state[i]+=temp[i]*this->dt;
        }
    }
};

template <class Func>
class Heun_method: public Method <Func>
{
public:
    Heun_method (Func &func, float T): Method <Func>(func, T) {};
    virtual ~Heun_method() {};
    void step()
    {
        Func func1(this->state, this->params, this->dt);
        vector <float> temp1=func1.f();
        vector <float> temp;
        temp.resize(temp1.size());
        for (int i=0; i<temp1.size(); i++)
        {
            temp[i]=this->state[i]+this->dt*temp1[i];
        }
        Func func(temp, this->params, this->dt);
        temp=func.f();
        for (int i=0; i<this->state.size(); i++)
        {
            this->state[i]+=(temp1[i]+temp[i])*this->dt/2;
        }
    }
};

int main(int argc, char* argv[])
{
    vector <float> initial_state, params;
    float dt, T;
    ifstream f1(argv[1], ios::in);
    int N;
    f1>>N;
    for (int i=0; i<N; i++)
    {
        float temp;
        f1>>temp;
        params.push_back(temp);
    }
    f1>>N;
    for (int i=0; i<N; i++)
    {
        float temp;
        f1>>temp;
        initial_state.push_back(temp);
    }
    f1>>dt;
    f1>>T;
    f1.close();
    ofstream f2(argv[2], ios::out);
    Sin_oscillator so(initial_state, params, dt);
    Low_vibration_oscillator lvo(initial_state, params, dt);
    Euler_method <Sin_oscillator> Eso(so, T);
    Euler_method <Low_vibration_oscillator> Elvo(lvo, T);
    Heun_method <Sin_oscillator> Hso(so, T);
    Heun_method <Low_vibration_oscillator> Hlvo(lvo, T);
    vector <vector<vector<float>>> astates;
    astates.push_back(Eso.result());
    astates.push_back(Elvo.result());
    astates.push_back(Hso.result());
    astates.push_back(Hlvo.result());
    for (auto &i: astates)
    {
        for (auto &j: i)
        {
            for (auto &h: j)
            {
                f2<<h<<' ';
            }
            f2<<endl;
        }
        f2<<endl;
    }
    f2.close();

    return 0;
}
