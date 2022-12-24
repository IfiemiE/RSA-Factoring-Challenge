#!/usr/bin/python3
import sys
import math

num_file = open(sys.argv[1], "r")
N = num_file.read()
N = int(N)
sq = int(math.sqrt(N))

if (sq * sq) == N:
    print("{}={}*{}".format(N, sq, sq))
    exit()

if (N % 2) == 0:
    p = int(N / 2)
    print("{}={}*{}".format(N, p, 2))
    exit()
if (N % 3) == 3:
    p = int(N/3)
    print("{}={}*{}".format(N, p, 3))
    exit()

if (sq % 2) == 0:
    sq_odd = sq - 1
else:
    sq_odd = sq
if (N % sq_odd) == 0:
    p = int(N / sq_odd)
    print("{}={}*{}".format(N, p, sq_odd))
    exit()

kL = 1
kU = (sq_odd // 6)
Lbound2 = kL
Ubound2 = kU
while (Lbound2 <= Ubound2):
    Lbound1 = 6 * kL - 1
    Lbound2 = 6 * kL + 1
    if (N % Lbound1) == 0:
        p = int(N / Lbound1)
        print("{}={}*{}".format(N, p, Lbound1))
        exit()
    if (N % Lbound2) == 0:
        p = int(N / Lbound2)
        print("{}={}*{}".format(N, p, Lbound2))
        exit()
    Ubound1 = 6 * kU - 1
    Ubound2 = 6 * kU + 1
    if (N % Ubound1) == 0:
        p = int(N / Ubound1)
        print("{}={}*{}".format(N, p, Ubound1))
        exit()
    if (N % Ubound2) == 0:
        p = int(N / Ubound2)
        print("{}={}*{}".format(N, p, Ubound2))
        exit()
    kL = kL + 1
    kU = kU - 1

num_file.close()
