#! python3
# Password Generator 
# By Jeff

import random

upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num =   ['1','2','3','4','5','6','7','8','9','0']
sym =   ('!','@','#','$','%','^','&','*','(',')','[',']','{','}','.','/','<','>','?','-','=','_','+',';',':','|')


print('''Hello, this is your password generator.
How long do you want your password to be?''')
pw_length = int(input())




def inc_sym():
    print('Include symbols? [y/n]')
    global symbols
    symbols = input()
    if symbols == 'y':
        print ('You got it!')
    elif symbols == 'n':
        print ('Understood!')
    else:
        print("Enter a 'y' or 'n'")
        inc_sym()   

inc_sym()

def is_satisfied():
    print('Satisfied? [y/n]')     
    satisfaction = input()
    if satisfaction == 'y' :
        print('Great! Do not forget to change your passwords every few months')
    elif satisfaction == 'n':
        new_pass()
    else:
        print("Error, enter 'y' or 'n'")
        is_satisfied()

def new_pass():
    pw = ('')
    if symbols == 'y': 
        for i in range(pw_length):
            r_num = random.randint(1,4)
            if r_num == 1:
                r_upper_assign = random.randint(0,25)         
                r_upper = upper[r_upper_assign]
                pw += r_upper
            elif r_num == 2:
                r_lower_assign = random.randint(0,25)         
                r_lower = lower[r_lower_assign]
                pw += r_lower
            elif r_num == 3:
                r_num_assign = random.randint(0,9)         
                r_num = num[r_num_assign]
                pw += r_num
            elif r_num == 4:
                r_sym_assign = random.randint(0,25)         
                r_sym = sym[r_sym_assign]
                pw += r_sym
    elif symbols == 'n': 
        for i in range(pw_length):
            r_num = random.randint(1,3)
            if r_num == 1:
                r_upper_assign = random.randint(0,25)         
                r_upper = upper[r_upper_assign]
                pw += r_upper
            elif r_num == 2:
                r_lower_assign = random.randint(0,25)         
                r_lower = lower[r_lower_assign]
                pw += r_lower
            elif r_num == 3:
                r_num_assign = random.randint(0,9)         
                r_num = num[r_num_assign]
                pw += r_num
            
    print('Your new ' + str(pw_length) +' character password is: ' + pw)
    is_satisfied()

new_pass()
   


 
    

