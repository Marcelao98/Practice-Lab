#Okay now it wants me to rebuild the sum function, its gonna take a list of integers and sum them all

def sumit_up(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total    


#result = sumit_up(1,3,4,3,7)
#print(result)


def sumit_up2(parameter = 0, *numbers):
    total = parameter
    for n in numbers:
        total += n
    return total    

#print(sumit_up2(5, *[1,4,6]))

#Oh man i feel like a loser huh, now let's take the average 
def avg_up(*numbers):
    total = 0
    print(f"{len(numbers)}")
    for n in numbers:
        total += n
    return total / len(numbers)   


#print(avg_up(1,2,3))

#Okay now i need to build a function that takes a list of word huh 

def describe_words(*words):
    num_words = []
    for word in sorted(words, key=len):
        num_words.append(len(word))
    info_words = []
    info_words.append(num_words[0])
    info_words.append(num_words[-1])

    print(info_words)
    print(sum(num_words)/ len(num_words))
   






describe_words('apple','banana','asdasdasdasd','the')