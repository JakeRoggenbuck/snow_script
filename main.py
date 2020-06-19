import argparse
import shlex

parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str)
args = parser.parse_args()

memory = []
pointer = 0

with open(args.filename, 'r') as f:
    content = f.readlines()
    lines = [line for line in content]
    
for line in lines:
    c = shlex.split(line)
    if c[0] == "input":
        memory.append(input(c[1]))
    elif c[0] == "input#":
        memory[int(c[1])] = input(c[2])
    elif c[0] == "int&":
        memory[int(c[1])] = int(memory[int(c[1])])
    elif c[0] == "str&":
        memory[int(c[1])] = str(memory[int(c[1])])
    elif c[0] == "int":
        memory.append(int(memory[int(c[1])]))
    elif c[0] == "str":
        memory.append(str(memory[int(c[1])]))
    elif c[0] == "calc":
        memory.append(eval(str(memory[int(c[1])]) + c[2] + str(memory[int(c[3])])))
    elif c[0] == "calc#":
        memory[int(c[1])] = eval(str(memory[int(c[2])]) + c[3] + str(memory[int(c[4])]))
    elif c[0] == "val":
        memory.append(c[1])
    elif c[0] == "val#":
        memory[int(c[1])] = c[2]
    elif c[0] == "out":
        print(memory[int(c[1])])
    elif c[0] == "push":
        memory.append(str(memory[int(c[1])]) + str(memory[int(c[2])]))
    elif c[0] == "push#":
        memory[int(c[1])] = str(memory[int(c[2])]) + str(memory[int(c[3])])
