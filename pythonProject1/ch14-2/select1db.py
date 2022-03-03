# selectone.py
import sqlite3
con = None;
cs = None;
try:
    con = sqlite3.connect('addr.db');
    cs = con.cursor();
    selectsql = 'SELECT * FROM tb_addr WHERE name = "%s"';
    name = input('입력');
    cs.execute(selectsql % name);
    data = cs.fetchone();
    print('이름은 %s, 전번은 %s, 주소는 %s' % data);
except:
    print('Error');
finally:
    if cs is not None:
        cs.close();
    if con is not None:
        con.close();


'''
CRUD

Create - INSRET
Read - SELECT
Update - 
Delete - 
'''