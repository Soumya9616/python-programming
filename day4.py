#16.03.2023
#1:
'''def nearest_palindrome(n):#sys.maxsize for infinite
    i=n+1
    s=str(i)
    if(s==s[::-1]):
        print(i)
    else:
        nearest_palindrome(i)
nearest_palindrome(99)
nearest_palindrome(1221)'''

#2:
'''def max_visit(l,d):
    p=l.count('p')
    o=l.count('o')
    e=l.count('e')
    if p>e and p>o:
        print(d['p'])
    elif e>o:
        print(d['e'])
    else:
        print(d['o'])
max_visit([101,'p',102,'0',302,'p',305,'p'],{'p':'pediatrics','o':'orthopedics','e':'ent'})'''

#3:
'''def matching(m,n):
    for i in m:
        if(i!=' '):
            if(i in n):
                print(i,end="")
matching("I like Python","Java is a very popular language")'''
