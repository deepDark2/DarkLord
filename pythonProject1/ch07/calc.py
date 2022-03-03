def calc(*data):
    sum = 0;
    for i in data:
        sum += i;
    result = sum/len(data);

    return  result;

print(calc(12,20,53,11,33))


def start():
    print("start application")

    while True:
        num = input('Input Num')
        if num == '0':
            break
        result = calc(int(num),2,4,5,6,7,8)
        print('Result:',result)
    print('stop application')

if __name__ == '__main__':#함수 테스트
    result = calc(15,22,5)
    print(result)
    #여기서 이렇게 테스트해본 후 코드(함수)를 전달.

def calcscore2(name,*score,**option):
    result = {};

    sum = 0;
    for s in score:
        sum += s;

    result['name'] = name;
    result['sum'] = sum;

    if option['avg'] == True:
        result['avg'] = sum/len(score);

    return result;
