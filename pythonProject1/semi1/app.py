# app.py
#import itemdb
from semi1.itemdb import ItemDb
from semi1.itemmodel import Item


def start():
    itemdb = ItemDb('shopdb');
    print('Start App');
    while True:


        cmd = input('Input CMD(q,i,s,so,u,d)')
        if cmd =='q':
            break

        elif cmd == 'i':
            print('Insert Item');
            try:
                id = int(input('ID:'));
                name = input('Name');
                price = int(input('price'));
                rate = float(input('rate'));
                item = Item(id,name,price,rate);
                itemdb.insert(item);
                print('Inserted OK');
            except Exception as e:
                print('Insert Error');


        elif cmd == 's':
            print('Item select');
            try:
                datas = itemdb.select();
                for data in datas:
                    print('%d %s %d %f' %data);
            except:
                print('Select Error')


        elif cmd == 'so':
            print('Item selectone');
            try:
                id = input('Input id....');
                data = itemdb.selectone(int(id));
                print('%d %s %d %f' % data);
            except:
                print('Select Error')


            print('select one Item');



        elif cmd == 'u':
            print('update Item');
            try:
                id = int(input('ID:'));
                name = input('Name');
                price = int(input('price'));
                rate = float(input('Float'));
                item = Item(id, name, price, rate);
                itemdb.update(item);
            except:
                print('update Error')

        elif cmd == 'd':
            print('delete Item')
            try:
                id = input('Input id:');
                itemdb.delete(int(id))
            except:
                print('delete Error')



    print('End App');

if __name__ == '__main__':
    start()
