#15.03.2023
#1:
'''def lt(l1,l2):
    l=[]
    for i in l2:
        l.append((i,l1.index(i)))
    print(l)
    print([(i,l1.index(i))for i in l2])#list comprehension
    print({i:l1.index(i)for i in l2})
lt([9,3,6,1,5,0,8,2,4,7],[6,4,6,1,2,2])'''
            
#2:
'''def ele(s,st):
    l2=[]
    for i in  s:
        l1=[]
        for j in i.split():
            if j not in st:
                l1.append(j)
        l2.append(l1)
    print(l2)
    print([[j for j in i.split() if j not in st]for i in s])
s=['a new world record is set','in the holy city of ayodha','on the eve of diwal tuesday','with over three lakh diya or earthen lamp','lit up simultaneosly on the bank of the saraju river']
st=['for','a','of','the','and','to','in','on','with','was']
ele(s,st)'''

#3:
'''def cm(l):
    m=sum(list(l[:l.index(5)]))+sum(list(l[l.index(8)+1:]))
    l3=list(l[l.index(5):l.index(8)+1])
    st1=''
    for i in l3:
       st1+=str(i)
    n=int(st1)
    print(n+m)
cm([3,2,6,5,1,4,8,9])'''

#4:
'''def rotate(d):
    l1=list(d.keys())
    l2=list(d.values())
    for i in l2:
        c=0
        for j in i:
            c+=int(j)**2
        for z in l1:
            if(l2.index(i)==l1.index(z)):
                if(c%2==0):
                    print(z[-1]+z[:-1])
                else:
                    print(z[-2:]+z[:-2])
rotate({"rhdt":"246","ghftd":"1246"})'''

#5:
'''import cmath
def f(n):
    f=-1
    while n%2==0:
        f=2
        n/=1
    for i in range(3,int(cmath.sqrt(n))+1,2):
        while n%i==0:
            f=i
            n=n/i
    if n>2:
        f=n
    return(int(f))
print(f(10))'''
