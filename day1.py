#13.03.2023
'''1:a=int(input())
b=int(input())
c=int(input())
if(a==7):
    print(b*c)
elif(b==7):
    print(c)
elif(c==7):
    print(-1)
else:
    print(a*b*c)'''
#2:
'''def converter(r,c):
    if(c=='Euro'):
        print(r*0.01417)
    elif(c=='British Pound'):
        print(r*0.0100)
    elif(c=='Australian Dolar'):
        print(r*0.02140)
    elif(c=='Canedian Dolar'):
        print(r*0.02027)
    else:
        print(-1)
converter(300,'Euro')
converter(300,'British Pound')
converter(300,'Australian Dolar')
converter(300,'Canedian Dolar')'''

#3:
'''a=int(input())
c=int(input())
af=a*37550.0
cf=c*37550.0/3
f=af+cf
tf=f*1.07
ttf=tf-tf*0.1
print("tatal ticket cost:",ttf)'''

#4:
'''def validnoofcoin(x,y,z):
    if((x+y*5)>=z):
        count1=int(z/5)
        count2=z%5
        print('no of 5 rupees coin=',count1,'no of 1 rupees coin=',count2)
    else:
        print(-1)
validnoofcoin(2,4,21)
print('\n')
validnoofcoin(11,2,11)
print('\n')
validnoofcoin(3,3,19)'''
