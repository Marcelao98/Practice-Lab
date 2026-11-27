def mysum(*arguments):
    if len(arguments) == 0:
        return arguments
    total = arguments[0]
    for n in arguments[1:]:
        total += n
        return total   
         
def mysum_bigger_than(threshold, *arguments):
    if len(arguments) == 0:
        return arguments
    total = None
    if arguments[0] > threshold:
        total = arguments[0]
    for n in arguments[1:]:
        if n > threshold:
            if total is None:
                total = n
            else:
                total += n

    

        
    return total




  


print(mysum_bigger_than(5,1,2,3,66))