#app.py
import itemDB
def start():
    print('Start App');
    while True:
        cmd = input('Input CMD(q,i,s,so,u,d,ch)');

        if cmd == 'q':
            print('프로그램을 종료합니다.')
            break;
        elif cmd == 'i':
            try:
                id = int(input('추가상품 id 입력 : '))
                name = str(input('상품의 이름 입력 : '))
                price = int(input('상품의 가격 입력 : '))
                rate = float(input('상품의 할인율 입력'))
                itemDB.insert(id,name,price,rate)
            except:
                print('오류.')
        elif cmd == 's':
            for items in itemDB.select():
                print('No.%d %s %d원 할인율 : %f'% items)
        elif cmd == 'so':
            try:
                id2 = int(input('검색할 상품의 id를 입력하세요.'))
                print(itemDB.selectone(id2))
            except:
                print('오류.')
        elif cmd == 'u':
            try:
                id = int(input('정보를 바꾸고자 하는 상품 id 입력 : '))
                name = str(input('상품의 새 이름 입력 : '))
                price = int(input('상품의 변경된 가격 입력 : '))
                rate = float(input('상품의 변경된 할인율 입력'))
                itemDB.update(name,price,rate,id)
                print('변경되었습니다.')
            except:
                print('오류.')
        elif cmd == 'd':
            try:
                id = int(input('삭제할 상품 id 입력 : '))
                itemDB.delete(id)
                print('삭제되었습니다.')
            except:
                print('오류.')
        elif cmd == 'ch':
            try:
                id = int(input('조회할 id를 입력'))
                print('No.%d %s %d원'%itemDB.selecttwo(id))

            except:
                print('오류.')
    print('End App');

if __name__ == '__main__':
    start();