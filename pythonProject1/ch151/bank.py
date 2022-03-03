# bank.py
#여기는 유저 인터페이스 영역으로 쓴다.
from Account import Account;

#acc1 Object
acc1 = Account(1000);
print(acc1);
print(acc1.inquire());
acc1.deposit(15000);
print(acc1);

#acc2 Object(객체)
acc2 = Account(2000);#클래스 내의 함수(이를 '메서드' 라고 부른다) 들을 재사용.
print(acc2);

#클래스와 객체 이용의 장점 : 코드 재사용 및 유지보수
#그리고 현실세계의 개념을 그대로 적용.
#현실반영을 클래스없이도 흉내 낼 순 있는데 대단히 스파게티가 되고 완성도도 떨어짐.
#이 외에도 화사출퇴근, 급여 및 지급일 등등 별에별것 구현 가능.