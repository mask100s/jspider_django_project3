#1-prime

def prime(num,fcount=0):
    for f in range(1,num+1):
        if num%f==0:
            fcount+=1
    return fcount==2

#print(prime(7))

#2-composite

def composite(num,fcount=0):
    for f in range(1,num+1):
        if num%f==0:
            fcount+=1
    return fcount>2

#print(composite(9))

#3-perfact

def perfact(num,fsum=0):
    for f in range(1,(num//2)+1):
        if num%f==0:
            fsum+=f
    return num==fsum

#print(perfact(28))

#4-pronic

def pronic(num,n=0):
    while(n*(n+1)<=num):
        if (n*(n+1)==num):
            return True
        else:
            n +=1
    return False

#print(pronic(12))
        
#5-sunny

def sunny(num,n=1):
    while(n**2<=num+1):
        if (n**2==num+1):
            return True
        else:
            n +=1
    return False

#print(sunny(8))

##sumDig

def sumDig(num):
    if num==0:
        return 0
    return num%10+ sumDig(num//10)
        
#6-niven

def niven(num):
    return num%sumDig(num)==0

#print(niven(12))

#7-spy

def prodDig(num,dsum=0):
    if num==0:
        return 1
    return num%10*prodDig(num//10)

def spy(num):
    return sumDig(num)==prodDig(num)

#print(spy(123))

#8-neon

def neon(num):
    return num==sumDig(num**2)

#print(neon(9))

#9-armstrong

def armSD(num,p):
    if num==0:
        return 0
    return (num%10)**p + armSD(num//10,p)

def armstrong(num):
    return num==armSD(num,len(str(num)))

#print(armstrong(153))

#10-disarium

def disSD(num,p):
    if num==0:
        return 0
    return (num%10)**p + armSD(num//10,p-1)

def disarium(num):
    return num==disSD(num,len(str(num)))

#print(disarium(135))

#11-strong

def factorial(rem,fprod=1):
    if rem==0:
        return 1
    return rem*factorial(rem-1)
    
def strongSD(num):
    if num==0:
        return 0
    return factorial(num%10) + strongSD(num//10)

def strong(num):
    return num==strongSD(num)

#print(strong(145))

#12-evil/odious

def eoSD(num):
    if num==0:
        return 0
    return num%2+ eoSD(num//2)

def evilodious(num):
    if eoSD(num)%2==0:
        return "evil"
    else:
        return "odious"

#print(evilodious(9))

#13-happy

def happySD(num):
    if num==0:
        return 0
    return (num%10)**2+ happySD(num//10)

def happy(num):
    while(num>9):
        num=happySD(num)
    return num==1

#print(happy(19))

#14-palindrom

def reverse(num):
    if num==0:
        return 0
    return reverse(num//10)+num%10*(10**(len(str(num))-1))

def palindrom(num):
    return num==reverse(num)

#print(palindrom(11))

#15-palyprime

def palyprime(num):
    return prime(num) and palindrom(num)

#print(palyprime(131))

#16-emirp

def emirp(num):
    return num!=reverse(num) and prime(num) and prime(reverse(num))

#print(emirp(13))

#17-automorphic

def automorphic(num):
    return num==((num**2)%(10**len(str(num))))
                 
#print(automorphic(25))

#18-trimorphic

def trimorphic(num):
    return num==((num**3)%(10**len(str(num))))
                 
#print(trimorphic(625))

print("this is due to jspider_module : ",__name__)

if __name__=='__main__':
    
    print(prime(7))
    print(composite(9))
    print(perfact(28))
    print(pronic(12))
    print(sunny(8))
    print(niven(12))
    print(spy(123))
    print(neon(9))
    print(armstrong(153))
    print(disarium(135))
    print(strong(145))
    print(evilodious(9))
    print(happy(19))
    print(palindrom(11))
    print(palyprime(131))
    print(emirp(13))
    print(automorphic(25))
    print(trimorphic(625))

