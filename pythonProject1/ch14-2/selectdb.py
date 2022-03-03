# selectdb.py
import sqlite3
con = None;
cs = None;
try:
    con = sqlite3.connect('addr.db');
    cs = con.cursor();
    selectsql = 'SELECT * FROM tb_addr';
    cs.execute(selectsql);
    datas = cs.fetchall();
    for data in datas:
        print('이름은 %s, 전번은 %s, 주소는 %s' % data);
except:
    print('Error');
finally:
    if cs is not None:
        cs.close();
    if con is not None:
        con.close();


