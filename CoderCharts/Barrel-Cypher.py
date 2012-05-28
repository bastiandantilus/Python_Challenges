#!/usr/bin/python
import sys
f = open(sys.argv[1])
t = int(f.readline())
for _t in range(t):
 k = str(f.readline()).strip('\n')
 k = k + k[::-1]
 m = f.readline().strip('\n')
 e, i = "", 0
 for c in range(len(m)):
  if m[c] == " ":
   e += " "
  else:
   o = ord(m[c])-int(k[i % len(k)])
   if o < ord('a'):
    o += 26
   e += chr(o)
   i += 1
 print (e)
