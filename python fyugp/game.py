import random

num=int(input('Guess a number b/w 1 and 20'))
generated_num=random.randint(1,20)
#print generated number
c=True
while c:
    if num==generated_num:
        print('You successfully predicted')
        break;
    if num<generated_num:
            print('You predicted too low')
    if num>generated_num:
            print('You predicted too high')
    num=int(input('enter a number'))

