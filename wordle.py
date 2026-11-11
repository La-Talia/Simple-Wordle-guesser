import word
import random
words = word.words
words = sorted(words)
fix = ['','','','','']
def filt(letter, position, flag):
    global words
    global fix
    nah = False
    if flag == '2':
        fix[position]=letter
        nwords = []
        for i in words:
            if i[position] == letter:
                nwords.append(i)
        words = nwords
        print("--only kept where {0} has {1}. left:{2}".format(position,letter, len(words)))
        print(fix)
    elif flag == '1':
        nwords = []
        nah = True
        for i in words:
            if letter in i and i[position]!=letter:
                nwords.append(i)
        words = nwords
        print("--only kept where {0} don't has {1}, but have it. left:{2}".format(position,letter, len(words)))
    elif nah == False:
        nfixpos=[]
        for o in range(5):
            if fix[o]=='':
                nfixpos.append(o)
        for rpos in nfixpos:
            nwords=[]
            for i in words:
                if i[rpos]!=letter:
                    nwords.append(i)
            words=nwords
        print("--removed all having {0}. left:{1}".format(letter, len(words)))
        print(fix, nfixpos)

def pro(trial, result):
    global words
    for pos in range(5):
        letter = trial[pos]
        position = pos
        flag = result[pos]
        filt(letter, position, flag)

for _ in range(6):
    trial = random.choice(words)
    print(trial)
    print("LEFT:", len(words))
    result = input()
    pro(trial, result)
