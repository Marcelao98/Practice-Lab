#Okay now it's time for the 5th exercise Pig Latin 
def pig_latin():
    word = input("Type your word here okay")
    print(f"The word is {word}")
    if word[0] in 'aeiou':
        word = word+'way'
    else:
         word = word+word[0]+'ay'
    print(f"The translation in pig latin is {word}")     
           


pig_latin()