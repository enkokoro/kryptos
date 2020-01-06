#!/usr/bin/env python

from string import ascii_lowercase
def createBox(word):
    one_d_box = []
    for c in word:
        if c not in one_d_box:
            if c == 'j':
                c = 'i'
            one_d_box.append(c)
    for c in ascii_lowercase:
        if c not in one_d_box and c != 'j':
            one_d_box.append(c)
    return one_d_box

def decryptChunk(box1, box2, three):
    i1 = box1.index(three[0])
    i2 = box2.index(three[2])
    return box1[5*(i1//5)+(i1+1)%5]+box2[5*(((i2//5)+1)%5)+(i2%5)]



def decrypt(word1, word2, message, w):
    message = message.lower().replace(" ", "")
    #    2
    # 1  3
    box1 = createBox(word1)
    box2 = createBox(word2)
    m = ""
    for i in range(len(message)//3):
        m+=decryptChunk(box1, box2, message[3*i:3*i+3])
    w.write("%s %s %s\n"%(word1, word2, m))

def scramblehelp(word, accum, add):
    if len(word) == 0:
        add.append(accum)
    if len(word) == 1:
        add.append(accum+word)
    else:
        for i in range(len(word)):
            scramblehelp(word[0:i]+word[i+1:len(word)], accum+word[i], add)

def scramble(word):
    r = []
    scramblehelp(word, "", r)
    return r

def filterlength(word):
    if not word.isalpha():
        return False
    if len(word) > 25:
        return False
    box = createBox(word)
    t = box.index("t")%5
    i = box.index("i")%5
    n = box.index("n")%5
    b = box.index("b")%5
    a = box.index("a")%5
    if t == i or t == n or t == b or t == a:
        return False
    if i == n or i == b or i == a:
        return False
    if n == a:
        return False
    if t != box.index("l")%5 or t != box.index("d")%5 or t != box.index("o")%5 or t != box.index("v")%5:
        return False
    if i != box.index("p")%5 or i != box.index("f")%5 or i != box.index("w")%5:
        return False
    if n != box.index("e")%5 or n != box.index("x")%5:
        return False
    if b != box.index("h")%5:
        return False
    if a != box.index("k")%5 or a != box.index("z")%5:
        return False
    return True

t = scramble("realm")
f = open("/usr/share/dict/words", "r")
output = open("evelynout.txt", "w")
l = list(filter(filterlength, f.read().lower().split()))
#print(l)
f.close()


for w in l:
    decrypt("emerald", w, "VXX CAV TQE GFZ EHV AIX REF NLE FFK QUA ONZ KLN LEW ATZ KMH HKF EIX GBP RHO LHD XZZ KGT AIX RHL LHO NLN GCX ZWP BCX HLE SRB LSH REI LHT MHV UPW ATZ BCX", output)

output.close()
#decrypt("saturday", "diamond", "thirteen", "VXXCAVTQEGFZEHVAIXREFNLEFFKQUAONZKLNLEWATZKMHHKFEIXGBPRHOLHDXZZKGTAIXRHLLHONLNGCXZWPBCXHLESRBLSHREILHTMHVUPWATZBCX")
