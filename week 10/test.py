import json
DTAT={'APPLE': 2, 'BANANA': 4, 'VODKA': 'UNLIMITED', 'params': [1, 2, 3, 4]}
with open('ttjs.json', 'w') as jsout:
    json.dump(DTAT, jsout)
DATA={}
with open('ttjs.json') as jsin:
    DATA=json.load(jsin)
print(DATA)