import sys
import codecs

file = codecs.open('C:/Users/Scott/Downloads/IntegerArray.txt', 'r', "utf-8")

def toint(x): return int(x)
array = file.readlines()

for i in range(len(array)):
 array[i] = int(array[i])

print(len(array))

def countsplitinv(b, c):
 n = len(b) + len(c)
 d = []
 i = 0
 j = 0
 z = 0
 for k in range(n):
  #print(n, i, b, j, c, )
  if j == len(c):
   d += b
   break
  else:
   if i == len(b):
    d += c
    break
  if j == len(c) or (i < len(b) and b[i] <= c[j]):
   d.append(b[i])
   i += 1
  else:
   d.append(c[j])
   j += 1
   z += len(b) - i
 print(d, z)
 return d, z

def sort_and_count(a):
 n = len(a)
 if ( n == 1 ):
  return a, 0
 else:
  bn = int(len(a) / 2)
  b, x = sort_and_count( a[:bn])
  c, y = sort_and_count( a[bn:])
  d, z = countsplitinv( b, c )
  #print(z)
  return d, x + y + z

#print(sort_and_count([1, 3, 5, 7, 2, 4, 6, 8]))
print(sort_and_count(array))
