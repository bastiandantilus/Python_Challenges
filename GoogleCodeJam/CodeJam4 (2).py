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
        table = { 'R':0, 'B':0 }
        winners = { 'R':0, 'B':0 }
        s = f.readline()
        s = s.split()
        A = int(s[0])
        score = int(s[1])
        #print (score)
        board = []
        for i in range(A):
            line = [l for l in f.readline() if l in '.RB']
            #print (''.join(line))
            newline = ''
            for i in line:
                if i in ['R', 'B']:
                    newline += i
                else:
                    newline = i + newline
            board.append(newline)
        #print()    
        for i in range(A):
            for color in 'RB':
                if color * score in board[i]:
                    winners[color] = 1
        rotated = []
        for j in range(A):
            column = ''.join([x[j] for x in board])
            rotated.append(column[::-1])
            for color in 'RB':
                if color * score in column:
                    winners[color] = 1
        board = rotated
        #for b in board:
            #print(b)
        #print()
        for i in range(A):
            for j in range(A):
                #print ('checking', i, j, board[i][j], i + score, A)
                if board[i][j] in "RB" and i + score <= A:
                    #print ('testing', i, j)
                    #test1, test2 = True, True
                    d1 = []
                    d2 = []
                    for x in range(A - i):
                        #print(x)
                        if j + x < A:
                            d1 += (board[i+x][j+x])
                        #else:
                        #    test1 = False
                        if j - x >= 0:
                            d2 += (board[i+x][j-x])
                        #else:
                        #    test2 = False
                        #if j + x < A and board[i+x][j+x] != board[i][j]:
                            #print (board[i+x][j+x], "!=", board[i][j])
                            #test1 = False
                        #if j - score >= 0 and board[i+x][j-x] != board[i][j]:
                            #print (board[i+x][j-x], "!=", board[i][j])
                            #test2 = False
                    d1 = ''.join(d1)
                    d2 = ''.join(d2)
                    #if d1: print ("d1", d1, score)
                    #if d2: print ("d2", d2, score)
                    for color in 'RB':
                        if color * score in d1 or color*score in d2:
                            winners[color] = 1
                    #if test1 == True or test2 == True:
                        #print (board[i][j] , " is a winner")
                        #winners[board[i][j]] = 1
                                
        score = "Neither"
        if winners['R'] and winners['B']:
            score = "Both"
        elif winners['R']:
            score = "Red"
        elif winners['B']:
            score = "Blue"       
        
        print ("Case #" + str(_t+1) + ": " + str(score))
    

