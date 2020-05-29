attempts = 0
while attempts != 3:
    username = input('Student Number: ')
    Password = input('Password: ')
    if (username == 'jojo') and ( Password== '987'):
        print(' WELCOME TO YOUR ACCOUNT') 
        exit()
    else:
     print('PLEASE TRY AGAIN')
     attempts +=1
    print('TOU CAN NOT LOGIN BECAUSE YOu EXCEEDED YOUR TRIES')
    exit()