def minion_game(string):
    # your code goes here
    vowel = ['A', 'E', 'I', 'O', 'U']
    K = 0
    S = 0
    for i in range (len(string)):
        if string[i] in vowel:
            K +=len(string)-i
        else:
            S +=len(string)-i
    if K>S:
        print("Kevin", K)
    elif S>K:
        print("Stuart", S)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)