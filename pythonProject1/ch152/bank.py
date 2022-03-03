# bank.py

from account import Account;

#acc1 Object
acc1 = Account(11335258851,1000,'James');
#Account에서 str변환해야 잘 출력됨.
#owner는 이미 str로 들어가서 str변환 불필요.
try:
    acc1.widthraw(-500)
    print(acc1);
except:
    print('잔액 부족')


#캡슐화의 목적 : 계좌 잔액 보호, 게임 내에서 치트 금지 등등
# 이름 바꿔야 하는 상황!(참고로 실제로 계좌변경은 안됨.)
#캡슐화 되어 못바꾸는 상황.
acc1.owner = 'Adam';
# acc1.setOwner('Adam')#캡슐화 된 정보 접근법, account.py 참조.
print(acc1)

#화면에 출력하려는데 계좌번호와 이름만 나오게 하려면?
print('계좌 : %s, 이름 : %s' % (acc1.accno,acc1.owner));
#같은 방법으로 계좌 잔액 출력만 하는것도 가능.
print('잔액 : %d'%acc1.getBalance())
#Account.py를 보고 어떤 메서드를 만들어서 사용했는지 확인.

try:
    acc1.deposit(-30)
    print(acc1)
except:
    print('뭘 하려는 거냐')