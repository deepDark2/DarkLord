import Program

def application():
    while True:
        menuScreen = str(input('q,m,i,v,s,c,d'))
        if menuScreen == 'q':
            print('종료합니다.')
            break
        elif menuScreen == 'm':
            print("데이터베이스를 처음부터 다시 만듭니다...")
            Program.makeIt()
        elif menuScreen =='i':
            try:
                id = int(input('ID를 입력학세요.'))
                name = str(input('이름을 입력하세요.'))
                age = int(input('나이를 입력하세요.'))
                phone = str(input('폰 번호를 입력하세요.'))
                addr = str(input('주소를 입력하세요.'))
                Program.insertIt(id,name,age,phone,addr)
            except:
                print('오류.')
        elif menuScreen =='v':
            for i in Program.viewIt():
                print(i)
        elif menuScreen == 's':
            try:
                id = int(input('검색할 ID를 입력.'))
                print(Program.seletIt(id))
            except:
                print('오류.')
        elif menuScreen == 'c':
            try:
                id = int(input('바꿀 내용의 ID를 입력하세요.'))
                name = str(input('새로운 이름을 입력하세요.'))
                age = int(input('변경할 나이를 입력하세요.'))
                phone = str(input('변경할 폰 번호를 입력하세요.'))
                addr = str(input('새 주소를 입력하세요.'))
                Program.changeIt(name,age,phone,addr,id)
            except:
                print('오류.')
        elif menuScreen == 'd':
            try:
                id = int(input('삭제할 내용의 ID번호를 입력하세요.'))
                Program.deleteIt(id)
            except:
                print('오류.')
        else:
            print('오류.')

if __name__ == '__main__':
    application()