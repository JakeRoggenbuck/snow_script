import shlex

mem = ['100', '10', '20', '100']

string = "3 + $1 + 5 + $2"

eq = ' '.join(mem[int(l[1])] if l[0] == '$' else l for l in shlex.split(string))

#for x in shlex.split(string):
#    if x[0] == '$':
#        x = mem[int(x[1])]
#    else:
#        x
#    print(x)
print(eval(eq))
