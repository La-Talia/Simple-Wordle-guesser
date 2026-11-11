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
    elif flag == '1':
        nwords = []
        nah = True
        for i in words:
            if letter in i and i[position]!=letter:
                nwords.append(i)
        words = nwords
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
    result = input("Enter result code:")
    pro(trial, result)
