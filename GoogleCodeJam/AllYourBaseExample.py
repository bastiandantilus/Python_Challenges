import sys

N = int(sys.stdin.readline().strip())
for qw in range(1, N+1):
  print 'Case #%d:' % qw,

  num = sys.stdin.readline().strip()
  values = {num[0]: 1}
  for c in num:
    if c not in values:
      sz = len(values)
      if sz == 1:
        values[c] = 0
      else:
        values[c] = sz
  result = 0
  base = max(len(values), 2)
  for c in num:
    result *= base
    result += values[c]
  print result