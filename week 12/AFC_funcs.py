def Ampl(t, v):
    for i in range(-len(t)+2, 0):
        if ((abs(v[-i])>abs(v[-i+1])) and (abs(v[-i])>abs(v[-i-1]))):
            return abs(v[-i])