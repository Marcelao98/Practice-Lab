#Okay now it wants me to rebuild the sum function, its gonna take a list of integers and sum them all

def sumit_up(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total    


result = sumit_up(1,3,4,3,7)
print(result)


