import os

file=""
with open(file) as fr:
    for line in fr.readlines():
        line=line.strip().split()