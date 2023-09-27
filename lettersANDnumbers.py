#3 BUGS TO FIND
while True: #loop forever
    print('Enter your age:') #string we print
    age = input() #input is a number?
    if age.isdecimal(): #can't be a decimal
        break #stops the program if the input is not what it's expecting
    print('Please eneter a number for your age.') #reprint enter your age
    
while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum(): #this is a letter or a number
        break #stops if not a letter or number 
    print('Passwords can only have letters and numbers.') #final print if if statement not met 