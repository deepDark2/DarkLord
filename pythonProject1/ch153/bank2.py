# bank2.py
# python은 java에 비해 class 활용이 제한적이다.
# 하지만 코드 간략화, 재사용, 유지보수, 협업에 많은 도움을 줌.
from ch153.account import Account

accs = [];
accs.append(Account('111',1000,'lee'));
accs.append(Account('222',2000,'kim'));
accs.append(Account('333',3000,'han'));

for acc in accs:
    print('계좌번호 : %s, 계좌주 : %s, 잔액 : %d'% (acc.accno,acc.owner,acc.inquire()));