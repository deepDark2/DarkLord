balance = 0;#사람 1 의 계좌
def deposit(money):
    global balance
    balance += money;

def inquire():
    return balance;

balance2 = 0;#사람 2 의 계좌
def deposit2(money):
    global balance2
    balance2 += money;

def inquire2():
    return balance2;


result = inquire();#사람 1 의 계좌정보
print(result);
deposit(1000);
result = inquire();
print(result);

result2 = inquire2();#사람 2 의 계좌정보
print(result2);
deposit2(500);
result2 = inquire2();
print(result2);
#80's bank programming...
#이때는 S/W 개발자가 왕 이였던 시절.
#하지만 미래에 객체지향이 등장함에 따라 상황이 뒤집어짐.