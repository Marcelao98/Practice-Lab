#Okay now it's time for the 5th exercise Pig Latin 
def pig_latin():
    word = input("Type your word here okay")
    print(f"The word is {word}")
    if word[0] in 'aeiou':
        word = word+'way'
    else:
         word = word+word[0]+'ay'
    print(f"The translation in pig latin is {word}")     
           

def pig_latin_pont():
    "Pig Latin but now it handles pontuation"
    pword =''
    point =''
    word = input("Type your word here okay")
    print(f"The word is {word}")
    if word[-1] in '.,!?;:"':
        pword = word[:-1]
        point+= word[-1]
        print(f"{pword} and the point is {point}")
    if pword[0] in 'aeiou':
         pword = pword+'way'+point
    else:
         pword = pword + pword[0] + 'ay'+point
    
    print(f"The translation in pig latin is {pword}")

pig_latin_pont()