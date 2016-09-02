T = int(raw_input())
winner = 'Richard'
for t in xrange(T):
    N = int(raw_input())
    if N == 1:
        print winner
    else:
        winner = "Louise"
        binN = bin(N)[2:]
        while binN != '1':
            if '1' in binN[1:]:
                ind = binN[1:].index('1')
                binN = binN[1 + ind:]
                if binN == '1':
                    print winner
                    break
            else:
                binN = binN[:-1]
                if binN == '1':
                    print winner
                    break
            if winner == 'Richard':
                winner = 'Louise'
            else:
                winner = 'Richard'
