"""task3 Левичкин БПМ-19-4"""

from io import StringIO
import csv

def task(csvString):
    q = StringIO(csvString)
    reader = csv.reader(q, delimiter=',')
    g = []
    for row in reader:
        g.append(row)
    for x in g:
        for y in x:
            y = int(y)
    r1 = []
    for x in g:
        if x[0] not in r1:
            r1.append(str(x[0]))
    r2 = []
    for x in g:
        if x[1] not in r2:
            r2.append(str(x[1]))
    q = g
    w = g
    r3 = []
    for i in range(len(q)):
        for j in range(len(g)):
            if i != j and q[i][0] not in r3 and q[i][1] == w[j][0]:
                r3.append(str(q[i][0]))
    r4 = []
    for i in range(len(q)):
        for j in range(len(g)):
            if i != j and q[i][1] not in r4 and q[i][0] == w[j][1]:
                r4.append(str(q[i][1]))
    r5 = []
    for i in range(len(f)):
        for j in range(len(g)):
            if i != j and q[i][1] not in r5 and q[i][0] == w[j][0]:
                r5.append(str(q[i][1]))
    return [r1, r2, r3, r4, r5]