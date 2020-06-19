import argparse
import shlex

parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str)
args = parser.parse_args()

mem = []

with open(args.filename, 'r') as f:
    content = f.readlines()
    lines = [line for line in content]
    
def m(l):
    return int(c[l])
def sm(l):
    return str(mem[m(l)])
def im(l):
    return int(mem[m(l)])

currentLine = 0
x = [line for line in lines]
linenum = len(x) -1

while currentLine <= linenum:
    c = shlex.split(x[currentLine])
    if c[0] == "input":
        mem.append(input(c[1]))
    elif c[0] == "input#":
        mem[m(1)] = input(c[2])
    elif c[0] == "int&":
        mem[m(1)] = im(1)
    elif c[0] == "str&":
        mem[m(1)] = sm(1)
    elif c[0] == "int":
        mem.append(im(1))
    elif c[0] == "str":
        mem.append(sm(1))
    elif c[0] == "calc":
        mem.append(eval(sm(1) + c[2] + sm(3)))
    elif c[0] == "calc#":
        mem[m(1)] = eval(sm(2) + c[3] + sm(4))
    elif c[0] == "val":
        mem.append(c[1])
    elif c[0] == "val#":
        mem[m(1)] = c[2]
    elif c[0] == "out":
        print(mem[m(1)])
    elif c[0] == "push":
        mem.append(sm(1) + sm(2))
    elif c[0] == "push#":
        mem[m(1)] = sm(2) + sm(3)
    elif c[0] == "dump":
        print(mem)
    elif c[0] == "dump@":
        print(mem[c[1]])
    elif c[0] == "type@":
        print(type(mem[m(1)]))
    elif c[0] == "is_str":
        mem.append(mem[m(1)] == str(c[2]))
    elif c[0] == "is_int":
        mem.append(mem[m(1)] == int(c[2]))
    elif c[0] == "is_str#":
        mem[m(1)] = mem[m(1)] == str(c[2])
    elif c[0] == "is_int#":
        mem[m(1)] = mem[m(1)] == int(c[2])
    elif c[0] == "jump":
        currentLine += int(c[1])
    elif c[0] == "if":
        if not mem[int(c[1])]:
            currentLine += 2
    currentLine += 1

