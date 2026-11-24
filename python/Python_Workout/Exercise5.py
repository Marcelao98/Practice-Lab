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

#Okay now it is an alternative version of pig latin, we check to see whether if the word contains two different vowels first


def pig_two():
    word = input("Type your word here")
    pigword = ''
    print(f"The word is {word}")
    count = 0
    for character in word:
        if character.lower() in 'aeiou':
            count+=1
    print(f"{count}")        
    if count == 0:
        pigword = word
    elif count == 1:
        pigword = word[1:]+word[0]+'ay'
    elif count >= 2:
        pigword = word+'way'
    print(f"{pigword}")            
        
        
pig_two()

