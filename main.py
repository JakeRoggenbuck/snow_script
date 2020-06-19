import argparse
import shlex

parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str)
args = parser.parse_args()

mem = []
pointer = 0

with open(args.filename, 'r') as f:
    content = f.readlines()
    lines = [line for line in content]
    
for line in lines:
    c = shlex.split(line)
    if c[0] == "input":
        mem.append(input(c[1]))
    elif c[0] == "input#":
        mem[int(c[1])] = input(c[2])
    elif c[0] == "int&":
        mem[int(c[1])] = int(mem[int(c[1])])
    elif c[0] == "str&":
        mem[int(c[1])] = str(mem[int(c[1])])
    elif c[0] == "int":
        mem.append(int(mem[int(c[1])]))
    elif c[0] == "str":
        mem.append(str(mem[int(c[1])]))
    elif c[0] == "calc":
        mem.append(eval(
            str(mem[int(c[1])]) + c[2] + str(mem[int(c[3])])))
    elif c[0] == "calc#":
        mem[int(c[1])] = eval(
            str(mem[int(c[2])]) + c[3] + str(mem[int(c[4])]))
    elif c[0] == "val":
        mem.append(c[1])
    elif c[0] == "val#":
        mem[int(c[1])] = c[2]
    elif c[0] == "out":
        print(mem[int(c[1])])
    elif c[0] == "push":
        mem.append(str(mem[int(c[1])]) + str(mem[int(c[2])]))
    elif c[0] == "push#":
        mem[int(c[1])] = str(mem[int(c[2])]) + str(mem[int(c[3])])
