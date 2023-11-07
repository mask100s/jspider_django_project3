'''
class py:
    cname='python'
    bname='marathahalli'

p1=py()
p2=py()

def stud(obj,n,s,p):
    obj.name=n
    obj.rollno=s
    obj.profil=p

stud(p1,'mack',101,'fr')
stud(p2,'max',102,'fr')

print(p1.name,p2.profil)
print(py.cname)
print(p1.cname,p2.bname)
'''


class mno:
    @staticmethod
    def smethod():
        print('Hello')

    def omethod(self):
        print(self)

    @classmethod
    def cmethod(cls):
        print(cls)

m1=mno()
m2=mno()

m1.smethod()
m2.smethod()
mno.smethod()

m1.omethod()
m2.omethod()

m1.cmethod()
m2.cmethod()
mno.cmethod()
