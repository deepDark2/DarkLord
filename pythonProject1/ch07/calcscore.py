import calc
def calcscore(name,*score,**option):
    result = {};
    sum=0
    for s in score:
        sum += s

    result['name'] = name
    result['sum'] = sum
    if option['avg'] == True:
        result['avg'] = sum/len(score)

    return result;






if __name__ == '__main__':
    result = calcscore('kim',90,80,99,avg=True);
    print(result);
    result2 = calc.calc(9,4,6,7,8)#다른 .py파일을 여기로 불러와 import로 선언해 활용이 가능.
    #즉 이 파일도 하나의 모듈이 될 수 있다.
    print(result2)