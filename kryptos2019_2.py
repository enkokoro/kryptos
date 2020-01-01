from string import ascii_lowercase

def decrypt(keyword, message):
    message = message.lower()
    table = []
    newtable = []
    word = sorted(list(keyword))
    
    for i in range(0, len(keyword)):
        table.append([])
        newtable.append([])
    for i in range(0, len(message)):
        table[i%(len(keyword))].append(message[i])
    
    # reordering
    for i in range(0, len(keyword)):
        newtable[keyword.index(word[i])] = table[i]
    
    # shifting
    shift = "qponmlkihgfedcbazyxwvutsr"
    
    for i in range(0, len(keyword)):
        shifti = 0
        if keyword[i] == 'j':
            shifti = shift.index('i')
        else:
            shifti = shift.index(keyword[i])
        first = newtable[i][0:25-shifti]
        second = newtable[i][25-shifti:25]
        second.extend(first)
        newtable[i] = second
        
    
    # printing
    newnewtable = []
    for i in range(0, 25):
        for t in newtable:
            newnewtable.append(t[i])
    s = "".join(newnewtable)
    print(s)

for c1 in ascii_lowercase:
    for c2 in ascii_lowercase:
        if c2 != c1:
            for c3 in ascii_lowercase:
                if c3 != c2 and c3 != c1:
                    for c4 in ascii_lowercase:
                        if c4 != c3 and c4 != c2 and c4 != c1:
                            decrypt(c1+c2+c3+c4, "TBCIMDWAOOSGEEEDTSSIBANOOCCRRURRRAUAPNHEAHESNMMEVACMNDOCUNTGCISMHBTIEGLIIKREVAFDDETETENONOCAOEENNTDS")
   
  
    