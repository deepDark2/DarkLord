# itemdb.py
from semi1 import itemsql
from semi1.db import Db

class ItemDb(Db):
    def __init__(self,dbname):
        super().__init__(dbname);
        super().makeTableitem();

    def insert(self, item):
        cs = None;
        con = None;
        try:
            con = super().connect();
            cs = con.cursor();
            cs.execute(item.insertsql());
            con.commit();
        except:
            raise Exception;
        finally:
            super().close(cs, con);

    def update(self, item):
        cs = None;
        con = None;
        try:
            con = super().connect();
            cs = con.cursor();
            cs.execute(item.udpatesql());
            con.commit();
        except:
            raise Exception;
        finally:
            super().close(cs, con);

    def delete(self, id):
        cs = None;
        con = None;
        try:
            con = super().connect();
            cs = con.cursor();
            cs.execute(itemsql.ITEM_DELETE % (id));
            con.commit();
        except:
            raise Exception;
        finally:
            super().close(cs, con);

    def selectone(self,id):
        con = None;
        cs = None;
        results = None;
        try:
            con = super().connect();
            cs = con.cursor();
            cs.execute(itemsql.ITEM_SELECT_ONE % (id));
            results = cs.fetchone();
        except:
            raise Exception;
        finally:
            super().close(cs, con);
        return results;

    def select(self):
        con = None;
        cs = None;
        results = None;
        try:
            con = super().connect();
            cs = con.cursor();
            cs.execute(itemsql.ITEM_SELECT);
            results = cs.fetchall();
        except:
            raise Exception;
        finally:
            super().close(cs, con);
        return results;





