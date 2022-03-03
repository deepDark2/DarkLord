#예외 처리!(정상적 상황이든 비정산적 상황이든)

cnt=0
while True:

    st = input('input number');

    if st == 'q':
        break;
    try:
        num = int(st);#여기서 오류가 나면 except 부분까지 넘어감
        print(num * 100);
    except ValueError as  e:
        cnt += 1#여기서 예외상황을 처리
        if cnt == 5:
            break;
        print('%d 번째 실패'%cnt)
        print(e)#ValueError처리를 함으로써 원인이 뭔지 알려주고 예외처리를 함.
        print('retry ...');

print('Exit');
print('총 실패 횟수는 ',cnt)
#예외처리를 이렇게 하면 편리하고 메모리도 절약된다.
#비교를 위해 exception 1.py부터 차근차근 확인하고 올 것.