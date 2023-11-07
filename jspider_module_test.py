'''def prime(num,fcount=0):
    for f in range(1,num+1):
        if num%f==0:
            fcount +=1
    return fcount==2

for num in range(1,11):
    if prime(num):
        print(num)

num=34576928
while(num!=0):
    rem=num%10
    if prime(rem):
        print(rem)
    num //=10
'''


print("this is due to jspider_module_test : ",__name__)
    
from jspider_module import factorial as f, sumDig 
print(f(4))
print(sumDig(123))

from jspider_module import niven as n, armSD, prodDig as pd 
print(n(4))
print(armSD(123,3))
print(pd(123))

import jspider_module
print(jspider_module.prime(7))
print(jspider_module.composite(9))
print(jspider_module.perfact(28))
print(jspider_module.pronic(12))
print(jspider_module.sunny(8))
print(jspider_module.niven(12))
print(jspider_module.spy(123))
print(jspider_module.neon(9))
print(jspider_module.armstrong(153))
print(jspider_module.disarium(135))
print(jspider_module.strong(145))
print(jspider_module.evilodious(9))
print(jspider_module.happy(19))
print(jspider_module.palindrom(11))
print(jspider_module.palyprime(131))
print(jspider_module.emirp(13))
print(jspider_module.automorphic(25))
print(jspider_module.trimorphic(625))
