import sqlite3

con = sqlite3.connect('addr.db');#저장 공간 생성
cs = con.cursor();
dropsql = 'DROP TABLE IF EXISTS tb_addr';#DROP : 삭제하란 뜻. 만약 tb_addr 테이블이 있다명 삭제하란 뜻.
createsql = """
            CREATE TABLE tb_addr(
            name CHAR(16) PRIMARY KEY,
            phone CHAR(16),
            addr TEXT
            )
            """;#데이터 담을 공간 제작
#테이블 생성, PRIMARY KEY : 중복 입력할 수 없는 명령.
cs.execute(dropsql);
cs.execute(createsql);
con.commit();

cs.close();
con.close();#connect 가 있을 시 반드시 close도 존재!