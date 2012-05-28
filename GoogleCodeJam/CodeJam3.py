import sys

def digits(number, base = 10):
  while number:
    yield number % base
    number //= base

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    t = int(f.readline())    
    for _t in range(t):
        s = f.readline()
        s = s.split()
        A = int(s[0])
        B = int(s[1])
        board = []
        for i in range(A):
             board.append(f.readline())
             print board
        
        print ("Case #" + str(_t+1) + ": " + str(score))
    

