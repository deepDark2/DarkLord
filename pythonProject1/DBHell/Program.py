import cgi
import sqlite3
import programBase

def connectIt(DBname):
    con = sqlite3.connect(DBname)
    return con

def disconnectIt(cur,con):
    cur.close()
    con.close()

def makeIt():
    try:
        con = sqlite3.connect(programBase.DB_name)
        cur = con.cursor()
        cur.execute(programBase.PREVENT_DUPLICATION)
        cur.execute(programBase.CREATE_TABLE)
        con.commit()
    except:
        Exception

    finally:
        disconnectIt(cur,con)

def insertIt(*data):
    try:
        con = connectIt(programBase.DB_name)
        cur = con.cursor()
        cur.execute(programBase.INSERT_INTO % (data))
        con.commit()
    except:
        raise Exception
    finally:
        disconnectIt(cur,con)

def viewIt():
    try:
        con = connectIt(programBase.DB_name)
        cur = con.cursor()
        cur.execute(programBase.SELECT_FROM)
        table = cur.fetchall()
    except:
        print('오류.')
    finally:
        disconnectIt(cur,con)

    return table

def seletIt(id):
    try:
        con = connectIt(programBase.DB_name)
        cur = con.cursor()
        cur.execute(programBase.SELECT_FROM_WHERE % id)
        table = cur.fetchone()
    except:
        print('오류.')
    finally:
        disconnectIt(cur,con)

    return table

def changeIt(*data):
    try:
        con = sqlite3.connect(programBase.DB_name)
        cur = con.cursor()
        cur.execute(programBase.UPDATE_SET_WHERE % data)
        con.commit()
    except:
        print('오류.')
    finally:
        disconnectIt(cur,con)

def deleteIt(id):
    try:
        con = connectIt(programBase.DB_name)
        cur = con.cursor()
        cur.execute(programBase.DELETE_FROM_WHERE % id)
        con.commit()
    except:
        print('오류.')
    finally:
        disconnectIt(cur,con)

