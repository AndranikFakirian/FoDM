#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <array>
using namespace std;

template <class T>
class Euler
{
public:
    typedef typename T::state_type State;
    static typename T::state_type make_step(State& state, const float dt){
        auto f = T::dfdt(state);
        for (auto it = f.state.begin(); it != f.state.end(); ++it) {
           const int index = distance(f.state.begin(), it);
           f[index] = state[index] + dt*f[index];
        }
        return f;
    }
};

template <typename MP>
class MyState
{
public:
    vector <MP> state;
    const size_t size() const{
        return state.size();
    }

    MP& operator[](int i) { return state[i]; }

    MyState (const vector<MP>& s){
        state=s;
    }
    typedef vector <MP> state_type ;
};

template <typename T>
class MyEquation
{
public:
    static T dfdt(T& s){
        return T (typename T::state_type {s[1], -1*s[0]});
    }
    typedef T state_type ;
};

int main()
{
    MyState<float> init {vector<float>{1.0f, 0.0f}};
    cout << "hello" << endl;
    auto step = Euler<MyEquation<MyState<float>>>::make_step(init, 0.01);
    cout << step[0] << step[1] << endl;
    swap(step, init);
    step = Euler<MyEquation<MyState<float>>>::make_step(init, 0.01);
    cout << step[0] << step[1] << endl;
    return 0;
}
