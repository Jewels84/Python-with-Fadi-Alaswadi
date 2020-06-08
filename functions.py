def liner():
    print('________________')

def Addition(n1,n2):
    print('The answer is', int(n1) + int(n2))

def Subtract(n1,n2):
    print('The answer is', int(n1) - int(n2))

def Multi(n1,n2):
    print('The answer is',int(n1) * int(n2))

def Division(n1,n2):
    print('The answer is',int(n1) / int(n2))

print('*WELOCOME TO CALCULATOR*')
liner()
name = input('Please tell us your name:')
print('Hello ', name ,)

print('''To use the calculater please choose your mathimatical operation'
'1) Addition  .  2)Subtraction  .  3)Multiplication  .  4)Division''')
select= input('Operation No. :')
num1= input ('Now inter your first number:' )
num2=input('and your second number:' )

if int(select)==1:
    Addition(num1,num2)

elif int(select)==2:
    Subtract(num1,num2)

elif int(select)==3:
    Multi(num1,num2)

elif int(select)==4:
    Division(num1,num2)

else:
    print('ERROR TRY AGAIN')# need help with putiing this sentence once the selcetion is wrong