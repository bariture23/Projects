#start of code
low = 0
#lowest number
high = 100
#highest number
print('I bet I can guess what number your thinking about!!!') 
print('Think about a number from 0 to 100!')

while True:
    #while loop
    number = (high + low)//2
    #mid
    print('Is your secret number ' + str(number) + ' ?')
    #guesses the user number each time
    a = input("Enter 'high' to show the given number is too high. Enter 'low' to show the given number is too low. Enter 'correct' to show the program guessed the number right.")
    if a == 'correct':
        print('I found it, Your number is', str(number))
        break
    #end of while loop
    elif a == 'low':
        low = number
        #lower number guess
    elif a == 'high':
        high = number
        #higher number guess
    else:
        print('Sorry, I did not understand your input.')
        #end of loop