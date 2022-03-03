import sqlite3
con = None;
cs = None;
try:
    con = sqlite3.connect('addr.db');
    cs = con.cursor();
    insertsql = 'INSERT INTO tb_addr VALUES ("%s","%s","%s")';
    name = input('Input name : ')
    phone = input('Input phone : ')
    addr = input('Input addr : ')
    cs.execute(insertsql % (name,phone,addr));
    con.commit();
except:
    print('Duplicated ID Error');
finally:
    if cs is not None:
        cs.close();
    if con is not None:
        con.close();


