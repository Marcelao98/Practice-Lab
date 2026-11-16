#Now it's Ubbi DUbbi hahaha

def ubbi_dubi(word):
    ubbi_word = []
    for c in word:
        if c  in 'aeiou':
            ubbi_word.append(f"{c}ub")
        else:
            ubbi_word.append(f"{c}") 

       
    return ''.join(ubbi_word)    

Ubbi_word = ubbi_dubi("The")          
print(Ubbi_word)