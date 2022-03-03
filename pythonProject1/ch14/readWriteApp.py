import  readWrite;

def start():
    # name = input('Intput File Name ..?')
    # content = input('Writr Content')
    # readWrite.filewrite(name,content)
    rname = input('Input read File name..?');
    try:
        rcontent = readWrite.fileread(rname);
        print(rcontent)
    except FileNotFoundError:#readWrite.py 에서 해당 에러상황 raise로 받을 시
        print('File Not Found ...')#이렇게 처리 한다.
    except IOError:
        print('IO Error !!')
    # except :
    #     print('File Not Found...')
#UI를 구현
if __name__ == '__main__':
    start();

#실제 현업에서는 이렇게 모듈로 나눠서 작업하게 된다.
#유저 영역 : 함수 호출 및 입/출력 등을 통해 다른 .py의 함수를 실행.
#컴퓨터 영역 : 유저에 의해 실행되는 프로그램(함수)들을 내장.