import sqlite3
con = None;
cs = None;
try:
    con = sqlite3.connect('addr.db');
    cs = con.cursor();
    updatesql = 'UPDATE tb_addr SET phone = "%s",addr = "%s" WHERE name = "%s"  ';
    name = input('Input name : ')
    phone = input('Input phone : ')
    addr = input('Input addr : ')
    cs.execute(updatesql % (phone,addr,name));#순서를 잘 맞춰야 한다!7줄 참조
    con.commit();
except:
    print('Error');
finally:
    if cs is not None:
        cs.close();
    if con is not None:
        con.close();


