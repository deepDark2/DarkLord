#딴따라단~~~쫘라라라락---
import random#python 에서 주어진 모듈인 random 이라는 패키지를 쓰겠다는 선언문.
#이 import 문은 Pycharm에서 해당 모듈을 사용시 자동 생성되니 참고.
#이 패키지는 따로 설치도 가능.
import time


def sendData(data):
    print('Send Data', data);

while True:
    temp = 0;
    temp = random.randint(1, 50);
    #random 모듈 내에서 randint기능의 함수를 이용
    if temp >= 45:
        break;
    sendData(temp);
    time.sleep(3);
#참고로 인터넷 창 등 계~속 열려있고 사용자가 닫아야 꺼지는 프로그램등은 거의 다 while True 상태라고 보면 된다.
print('Terminated ....')

#