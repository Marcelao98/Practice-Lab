#Now this is exercise 3 of python workout, i'm actually enjoying this stuff, it's actaully fun, let's keep going 


def run_timing():
    average_runs = []
    while True:
        print(f"How long did it take for you to run 10km?, we are gonna wait for teh enter")
        run = input()
        if run == '':
            print(sum(average_runs)/len(average_runs))
            break
        else:
            average_runs.append(int(run))


                
run_timing()

        
