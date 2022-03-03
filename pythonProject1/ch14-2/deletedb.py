#deleteDB.py
import sqlite3
con = None;
cs = None;
try:
    con = sqlite3.connect('addr.db');
    cs = con.cursor();
    deletesql = 'DELETE FROM tb_addr WHERE name="%s" ';#''와 ""를 혼용해서 쓰면 구분이 잘 된다.
    name = input('Input name : ')
    cs.execute(deletesql % (name));
    con.commit();
except:
    print('Error ...');
finally:
    if cs is not None:
        cs.close();
    if con is not None:
        con.close();


