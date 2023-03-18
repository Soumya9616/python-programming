#14.03.2023
#1:
'''def count(s):
    list1=[]
    c=0
    n=0
    for i in s:
        if i.isalpha():
            n+=1
        elif i.isdigit():
            c+=1
        else:
            continue
    list1.append(n)
    list1.append(c)
    print(list1)
count('Infosys 123')
count("abcdef")'''

#2:
'''def find_pairs_of_number(l,v):
    count1=0
    d=len(l)
    for i in range(d):
        for j in range(i+1,d+1):
            if((i+j)==v):
                count1+=1
            else:
                continue
    print(count1)
find_pairs_of_number([1,2,3,4,5,6,0,3],6)
find_pairs_of_number([3,4,1,8,5,9,0,6],9)'''

#3:
'''def str1(a):
    l=len(a)
    if(l<2):
        print(-1)
    else:
        print(a[0:2]+a[-2:])
str1("w3resource")
str1("w3")
str1("A")'''

#4:
'''def str2(a):
    if(len(a)<3):
        print(a)
    elif(a[-3:]=='ing'):
        print(a+'ly')
    else:
        print(a+'ing')
str2('sleep')
str2('amazing')
str2('is')'''

#5:
'''def check_double(n):
    n2=2*n
    c=0
    if(len(str(n))==len(str(n2))):
        for i in str(n):
            if(i in str(n2)):
                c+=1
                if(c==len(str(n))):
                    return True
print(check_double(245))'''

#6:
'''def find_more_than_avarage(t):
    avr=sum(list(t))/len(t)
    c=0
    for i in t:
        if(i>avr):
            c+=1
    print(c*11.11)
def generate_frequency(t):
    for i in range(0,26,1):
        print(i,list(t).count(i))
def sort_marks(t):
    print(sorted(t))
find_more_than_avarage((12,18,25,2,5,18,20,20,21))
generate_frequency((12,18,25,2,5,18,20,20,21))
print()
sort_marks((12,18,25,2,5,18,20,20,21))'''

#7:
'''def translate(d,l):
    l1=[]
    for i in l:
        l1.append(d[i])
    print(l1)
translate({'merry':'god','christmas':'jul','happy':'gott','new':'nytt','year':'ar'},['merry','christmas'])'''
        
#8:
'''def ar(a,b):
    list1=[]
    list1=[i for i in range(a,b+1)]
    l1=[list1[i:j+1] for i in range(len(list1))for j in range(i,len(list1))]
    print(l1)
    c=0
    for i in l1:
        if sum(i)%2!=0:
            c+=1
    print(c)
ar(1,3)'''
