def mysum(*arguments):
    if len(arguments) == 0:
        return arguments
    total = arguments[0]
    for n in arguments[1:]:
        total += n
        return total   
         



  


print(mysum('a','b'))      