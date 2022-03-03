#예외 처리!(정상적 상황이든 비정산적 상황이든)
while True:
    st = input('input number');

    if st == 'q':
        break;
    # if st.isalpha():
    #     print('retry...')
    #     continue;
    # else:
    #     print(st)
    num = int(st);
    print(num * 100);


print('Exit');