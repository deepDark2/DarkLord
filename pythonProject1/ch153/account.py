# account.py
#UML(Unified Modeling Language)

'''
속성 : accno, balance, owner,
행위 : deposit, widthraw, inwuire
'''


class Account:
    def __init__(self, accno,balance,owner):
        self.__accno = accno;#__처리(캡슐화)를 함으로써 외부에서 함부로 접근 못하게 보호.
        if balance >= 0:
            self.__balance = balance;
        else:
            self.__balance = 0;#상위 클래스에서 제약 걸면 하위에서도 걸린다.
        self.__owner = owner;

    @property
    def owner(self):
        return self.__owner
    @owner.setter
    def owner(self, owner):
        self.__owner = owner;
    def setOwner(self,owner):#통상적으로 get,set을 이름으로 많이 채용, 사용처 마다 규칙 다름.
        self.__owner = owner;
    @property
    def accno(self):
        return self.__accno;#변경 못하는 값을 출력 만 할수있게



    def getBalance(self):
        return self.__balance;
    def deposit(self,money):
        if money < 0:
            raise Exception;
        self.__balance += money;

    def widthraw(self,money):
        if (money <= 0) or (money > self.__balance):
            raise Exception;#if문에서도 raise를 적용 가능. try 문으로 받아줘야 함.
        self.__balance -= money;

    def inquire(self):
        return self.__balance;
    def __str__(self):
        return str(self.__accno)+':'+str(self.__balance)+':'+self.__owner;

#IAccount
'''
속성 : accno, balance, name, interest(이자,balance 의 3.2%)
행위 : deposit, widthraw, inquire, calcurate intereat

Inheritance (상속)
'''

class IAccount(Account):#Account 클래스의 모든 메서드 들을 상속받는다.
    def __init__(self, accno,balance,name,interest):
        super().__init__(accno,balance,name);
        self.__interest = interest;
    def __str__(self):
        return super().__str__()+' '+str(self.__interest);
    def calcinterest(self):
        return super().inquire() * (self.__interest/100)
    def getinterest(self):
        return self.__interest;
    def setinterest(self,interest):
        self.__interest = interest;

    #super() : 상위에 있는 코드 활용, ()안에는 상위 변수가 들어감