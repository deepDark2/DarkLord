#파일 읽고 쓰기
def filewrite(name, content):
    try:
        f = open(name,'wt');#하드웨어와 애플리케이션 간 파이프 연결
        f.write(content);
    except:
        raise IOError
    finally:
        f.close();#종료할 땐 무조건 H/W , App 간의 파이프 닫기.

def fileread(name):
    f = None;
    try:
        f = open(name,'rt');#여기서 문제가 생기면 f가 안만들어짐.
        text = f.read();
    except FileNotFoundError as fe:
        raise fe;#예외처리 발생시 에러상황 전달.
    except IOError as ie:
        raise ie#이런 식으로 raise를 여러개 동시에 사용 가능.
    finally:
        if f is not None:#f가 안 만들어졌을때 이렇게 대처
            f.close();# 참고로 처음 f에 None로 초기화해 오류 수정함.
    return  text;