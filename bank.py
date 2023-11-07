class bank:
    bnak_Name='SBI'
    branch_Name='Marathahalli'
    ifsc_Code='SBIN000123'
    ROI=0.06

    def __init__(self,name,mob,accno,pin,bal):
        self.name=name
        self.mob=mob
        self.accno=accno
        self.pin=pin
        self.bal=bal

    @staticmethod
    def validate():
        return int(input('Enter 4-digit pin : '))

    def deposite(self):
        if self.pin==self.validate():
            amount=int(input('Enter amount : '))
            self.bal +=amount
            print('Amount deposited successfully')
        else:
            print('Incorrect pin')

    def withdraw(self):
        if self.pin==self.validate():
            amount=int(input('Enter amount : '))
            if self.bal>=amount:
                self.bal -=amount
                print('Amount debited successfully')
            else:
                print('Insufficent balance')
        else:
            print('Incorrect pin')

    def check_Bal(self):
        if self.pin==self.validate():
            print(f"{self.name}'s account balance is {self.bal}")
        else:
            print('Incorrect pin')

    def change_Pin(self):
        if self.pin==self.validate():
            pin1=int(input('Enter new pin : '))
            pin2=int(input('Confirm new pin : '))
            if pin1==pin2:
                self.pin =pin1
                print('Pin changed successfully')
            else:
                print('Pin not matching')
        else:
            print('Incorrect pin')

    @classmethod
    def change_ROI(cls):
        cls.ROI=float(input('Enter new ROI : '))
        print('ROI changed successfully')


p1=bank('Ram',9999999999,2354679801,2222,10000)
p2=bank('Sham',9999999990,3245768910,3333,20000)

'''
p1.check_Bal()
p1.deposite()
p1.check_Bal()


p2.check_Bal()
p2.withdraw()
p2.check_Bal()


print(p1.pin)
p1.change_Pin()
print(p1.pin)
p1.check_Bal()


print(bank.ROI,p1.ROI,p2.ROI)
bank.change_ROI()
print(bank.ROI,p1.ROI,p2.ROI)

print(bank.ROI,p1.ROI,p2.ROI)
p1.change_ROI()
print(bank.ROI,p1.ROI,p2.ROI)
'''
