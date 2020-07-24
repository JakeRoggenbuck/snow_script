#!/usr/bin/env python3
from termcolor import colored
import argparse
import shlex
import regex

mem = []


class commands:
    def input_(self, mem, c):
        if c[0][-1] == "#":
            mem[int(c[1])] = input(c[2])
            return mem[int(c[1])]
        else:
            mem.append(input(c[1]))
            return mem[-1]

    def int_(self, mem, c):
        if c[0][-1] == "&":
            mem[int(c[1])] = int(mem[int(c[1])])
            return mem[int(c[1])]
        else:
            mem.append(int(mem[int(c[1])]))
            return mem[-1]

    def str_(self, mem, c):
        if c[0][-1] == "&":
            mem[int(c[1])] = str(mem[int(c[1])])
            return mem[int(c[1])]
        else:
            mem.append(str(mem[int(c[1])]))
            return mem[-1]

    def calc_(self, mem, c):
        if c[0][-1] == "#":
            eq = ' '.join(str(mem[int(l[1])]) if l[0] == '$' else str(l) for l in c[2:])
            print(eq)
            mem[int(c[1])] = eval(eq)
            return mem[int(c[1])]
        else:
            eq = ' '.join(str(mem[int(l[1])]) if l[0] == '$' else str(l) for l in c[1:])
            print(eq)
            mem.append(eval(eq))
            return mem[-1]

    def val_(self, mem, c):
        if c[0][-1] == "#":
            mem[int(c[1])] = c[2]
            return mem[int(c[1])]
        else:
            mem.append(c[1])
            return mem[-1]

    def out_(self, mem, c):
        a_ = mem[int(c[1])]
        return a_

    def push_(self, mem, c):
        if c[0][-1] == "#":
            mem[int(c[1])] = str(mem[int(c[2])]) + str(mem[int(c[3])])
            return mem[int(c[1])]
        else:
            mem.append(str(mem[int(c[1])]) + str(mem[int(c[2])]))
            return mem[-1]

    def dump_(self, mem, c):
        if c[0][-1] == "@":
            a_ = mem[int(c[1])]
        else:
            a_ = mem
        return a_

    def type_(self, mem, c):
        a_ = type(mem[int(c[1])])
        return a_

    def is_(self, mem, c):
        if [0][-1] == "#":
            try:
                mem[int(c[1])] = int(mem[int(c[2])]) == int(c[3])
            except:
                mem[int(c[1])] = str(mem[int(c[2])]) == str(c[3])
            return mem[int(c[1])]
        else:
            try:
                mem.append(int(mem[int(c[1])]) == int(c[2]))
            except:
                mem.append(str(mem[int(c[1])]) == str(c[2]))
            return mem[-1]

    def jump_(self, c, cline):
        cline += int(c[1])
        return cline

    def del_(self, mem, c):
        del mem[int(c[1])]
        return mem

    def cp_(self, mem, c):
        mem[int(c[2])] = mem[int(c[1])]
        return mem

    def char_(self, mem, c):
        if c[0][-1] == "#":
            mem[int(c[1])] = chr(int(mem[int(c[2])]))
            return mem[int(c[1])]
        else:
            mem.append(chr(int(mem[int(c[1])])))
            return mem[-1]

    def len_(self, mem, c):
        if c[0][-1] == "#":
            mem[int(c[1])] = len(str(mem[int(c[2])]))
            return mem[int(c[1])]
        else:
            mem.append(len(str(mem[int(c[1])])))
            return mem[-1]

    def ord_(self, mem, c):
        if c[0][-1] == "#":
            mem[int(c[1])] = ord(str(mem[int(c[2])]))
            return mem[int(c[1])]
        else:
            mem.append(ord(str(mem[int(c[1])])))
            return mem[-1]


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str)
    args = parser.parse_args()
    return args


def file_read(filename_args):
    with open(filename_args.filename) as f:
        lines = []
        for line in f:
            line = line.strip()
            if line:
                lines.extend(line.split(";"))
    return lines


def loop(lines):
    ssc = commands()
    cline = 0
    direction = 1
    while cline <= len(lines) - 1:
        try:
            c = shlex.split(lines[cline])
        except:
            exit()
        b = c[0]
        if regex.search("input", b):
            ssc.input_(mem, c)
        elif regex.search("int", b):
            ssc.int_(mem, c)
        elif regex.search("str", b):
            ssc.str_(mem, c)
        elif regex.search("calc", b):
            ssc.calc_(mem, c)
        elif regex.search("val", b):
            ssc.val_(mem, c)
        elif regex.search("out", b):
            print(ssc.out_(mem, c))
        elif regex.search("push", b):
            ssc.push_(mem, c)
        elif regex.search("dump", b):
            ssc.dump_(mem, c)
        elif regex.search("type", b):
            print(ssc.type_(mem, c))
        elif regex.search("is", b):
            ssc.is_(mem, c)
        elif regex.search("jump", b):
            cline = ssc.jump_(c, cline)
        elif regex.search("del", b):
            ssc.del_(mem, c)
        elif regex.search("len", b):
            ssc.len_(mem, c)
        elif regex.search("char", b):
            ssc.char_(mem, c)
        elif regex.search("ord", b):
            ssc.ord_(mem, c)
        elif regex.search("dir", b):
            direction = int(c[1])
        elif regex.search("if", b):
            if not mem[int(c[1])]:
                cline += int(c[2])
        elif regex.search("cp", b):
            ssc.cp_(mem, c)
        else:
            print(colored(f'Command not found "{b}"', "red"))
        cline += direction


if __name__ == "__main__":
    filename_args = parse()
    lines_list = file_read(filename_args)
    loop(lines_list)
