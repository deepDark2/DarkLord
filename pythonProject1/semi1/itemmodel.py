# itemmodel
from semi1 import itemsql


class Item:
    def __init__(self, id, name, price, rate):
        self.__id = id;
        self.__name = name;
        self.__price = price;
        self.__rate = rate;
    def getid(self):
        return self.__id;
    def setid(self,id):
        self.__id = id;
    def getname(self):
        return self.__name;
    def setname(self,name):
        self.__name = name;
    def getprice(self):
        return self.__price;
    def setprice(self,price):
        self.__price = price;
    def getrate(self):
        return self.__rate;
    def setrate(self,rate):
        self.__rate = rate;
    def insertsql(self):
        return (itemsql.ITEM_INSERT % (self.__id, self.__name, self.__price, self.__rate));

    def udpatesql(self):
        return (itemsql.ITEM_UPDATE % (self.__name, self.__price, self.__rate,self.__id));

    def __str__(self):
        return str(self.__id)+' '+self.__name+' '+str(self.__price)+' '+str(self.__rate);