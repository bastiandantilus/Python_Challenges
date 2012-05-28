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
    # A-small.in

    for _t in range(t):
        s = f.readline().strip()
        number = "1"
        mapped = {s[0]:0}
        digit = 0
        digitlist = '10234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for char in s[1:]:
            if char not in mapped:
               digit += 1
               mapped[char] = digit
            number += digitlist[mapped[char]]
        score = int(number, max(2, digit+1))

        print ("Case #" + str(_t+1) + ": " + str(score))
    

