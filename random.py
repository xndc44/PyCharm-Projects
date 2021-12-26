def isconsonant(aStand):
    stuartpoint = 0
    kevinpoint = 0

    f = "aeiou"
    g = list(f.upper())
    c = "bcdfghjklmnpqrstvwxyz"
    b = list(c.upper())
    print(len(aStand))

    for j in b:
        for i in range(len(aStand)):
            if j == aStand[i][0]:
                stuartpoint += 1
    for x in g:
        for w in range(len(aStand)):
            if x == aStand[w][0]:
                kevinpoint += 1
    print(kevinpoint)
    print(stuartpoint)
    if (stuartpoint > kevinpoint):
        print("Stuart " + str(stuartpoint))
    elif (kevinpoint > stuartpoint):
        print("Kevin " + str(kevinpoint))
    else:
        print("Draw")


def minion_game(string):
    # your code goes here
    line = []
    for i in range(len(string)):
        for j in range(i, len(string)):
            ans = (string[i:j + 1])
            line.append(ans)
    isconsonant(line)


if __name__ == '__main__':
    s = input()
    a = len(s)
    print(a*(a+1)/2)
    minion_game(s)