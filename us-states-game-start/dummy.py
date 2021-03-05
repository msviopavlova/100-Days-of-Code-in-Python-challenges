import pandas

statess = {'state': {34: 'Ohio'},
 'x': {34: 176},
 'y': {34: 52}
         }



x = statess['x']
#print(x)

for key in x:
    print(list(x.values())[0])


state_of = statess["state"]

for key in state_of:
    print(list(state_of.values())[0])