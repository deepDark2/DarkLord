# account.py
'''
class 는
1. 속성
2. 행위
    로 표현한다.
    (현실세계의 모든 것들을 소프트웨어로 모형을 만들어 구현.)
'''

'''
Account class
1. 속성 : balance 등등
2. 행위 : deposit, widthraw 등등
'''

class Account:#class 선언 시 앞글자 대문자로쓰는게 관행.
    #Constructor(생성자, 클래스 초기화)
    def __init__(self, balance):
        self.balance = balance;
    #self : 각각의 계좌를 의미.
    def deposit(self,money):
        self.balance += money;
    def widthraw(self,money):
        self.balance -= money;
    #요게 클래스의 모양.
    def inquire(self):
        return self.balance;
    def __str__(self):#클래스의 내용을 string으로 변환
        return  str(self.balance)#그걸 리턴.
        #str 처리를 한 이유는__str__인데 다른 자료형 오면 오류나서.
    #print 써서 출력해도 되지만 실감나는 실습을 위해 UI 영역을 따로 만들어서 출력한다.
    #같은 패키지 내 bank.py에서 계속.

    #__str__ 만든 이유는 프로그래머 입장에서 빠르게 파악하려고.