from __future__ import division
import sys
import string


def digits(number, base = 10):
  while number:
    yield number % base
    number //= base

def wp(season):
    return season.count("1") / (len(season) - season.count("."))

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    t = int(f.readline())
    
    for _t in range(t):
        print ("Case #" + str(_t+1) + ": ")               
        N = int(f.readline().strip())
        scores = [f.readline().strip() for _n in range(int(N))]
        WP = []
        OWP = []
        OOWP = []
        WP = [wp(scores[_n]) for _n in range(N)]
        OWP = [sum([wp(
            [scores[_n][x] for x in range(N) if x != _n]
            ) for _n in range(N) if _n != _m]) / (N-1) for _m in range(N)]
        OOWP = [sum([OWP[x] for x in range(N) if x != _n]) / (N-1) for _n in range(N)]

        for _n in range(N):
            print WP[_n], OWP[_n], OOWP[_n]
            print 0.25 * WP[_n] + 0.50 * OWP[_n] + 0.25 * OOWP[_n]
                
    

