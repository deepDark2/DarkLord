#로또 프로그램을 짠다.
#1.프로그램의 흐름을 정의
#2.프로그램의 구조를 만든다.
#3.업무분담 또는 참관
#4.개인 별 실행 완료
import random

listC = []
listU = []
def lottoJackpot():

    countS = 0
    i=0
    import random
    while i < 6:
        print("%d"%(i+1),end=" ")
        User1 = int(input("번째 번호 입력:"))
        if User1>15 or User1<1:
            print("잘못된 입력!")
            continue
        UserC = random.randint(1,15)
        if User1 not in listU and UserC not in listC:
            listU.append(User1)
            listC.append(UserC)
            i += 1
        else:
            print("중복 입력.")
            continue
    print(listU)
    print(listC)
    for i in range(0,len(listU)):
     if listU[i] == listC[i]:
        countS += 1
    return(countS)
def judge(score):
    if score >= 4:
        print("1등")
    elif score == 3:
        print("2등")
    elif score == 2:
        print("3등")
    else:
        print("꽝")
def prize(score):
    tot = 200000
    if score >= 4:
        print("상금 : ",tot * .5,'$')
    elif score == 3:
        print("상금 : ",tot * .3,'$')
    elif score == 2:
        print("상금 : ",tot * .19,'$')
    else:
        print("위로금 : ",tot * .01,'$')


score = lottoJackpot()
judge(score)
prize(score)


