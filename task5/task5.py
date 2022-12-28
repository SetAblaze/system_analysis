"""task5 Левичкин БПМ-19-4"""

import json
import numpy as np

def task(ranking_str_1: str, ranking_str_2:str) -> str:
    rank_1 = json.loads(ranking_str_1)
    rank_2 = json.loads(ranking_str_2)

    ya = r_m(rank_1)
    yat = ya.transpose()

    yb = r_m(rank_2)
    ybt = yb.transpose()

    yab = np.multiply(ya, yb)
    yabt = np.multiply(yat, ybt)

    conflicts = []

    for i in range(yab.shape[0]):
        for j in range(yab[i].shape[1]):
            if int(yab[i,j]) == 0 and int(yabt[i,j]) == 0:
                if (str(j+1),str(i+1)) not in conflicts:
                    conflicts.append((str(i+1),str(j+1)))

    return json.dumps(conflicts)

def r_m(rank_):
    ranks = dict()
    rank_len = r_l(rank_)
    for i, rank in enumerate(rank_):
        if type(rank) is str:
            ranks[int(rank)] = i
        else:
            for r in rank:
                ranks[int(r)] = i

    return np.matrix([[1 if ranks[i+1] <= ranks[j+1] else 0 for j in range(rank_len)] for i in range(rank_len)])

def r_l(rank_) -> int:
    length = 0
    for i in rank_:
        if type(i) is str:
            length+=1
        else:
            length+=len(i)
    return length