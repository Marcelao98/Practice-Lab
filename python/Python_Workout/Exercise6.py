

def pig_sentence():
    sentence= input("TYpe your sentence here")
    pig_sentence=''
    for word in sentence.split():
        if word[0] in 'aeiou':
            pig_sentence += word+ 'way '
        else:
            pig_sentence += word+word[0]+'ay '
    print(f"{pig_sentence}")        



pig_sentence()        