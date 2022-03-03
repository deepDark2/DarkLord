# bank.py

from account import Account, IAccount;

#acc1 Object
iacc1 = IAccount(11335258851,1000,'James',3.4);
#Account에서 str변환해야 잘 출력됨.
#owner는 이미 str로 들어가서 str변환 불필요.
try:
    iacc1.widthraw(30)
    print(iacc1);
except:
    print('잔액 부족')
interest = iacc1.calcinterest();
print(interest)
print(iacc1.accno,' ',iacc1.owner,' ',iacc1.getinterest());

