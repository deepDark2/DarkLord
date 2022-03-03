import random
import time

def connect():
    print('Connected Server ...');
def sendData(data):
    if data == 3:
        raise IOError;
    print('Send Data', data);
def close():
    print('Closed Server ...');


while True:
    temp = 0;
    temp = random.randint(1,5);
    try:
        connect()
        sendData(temp);#raise 발생시 오류는 여기서 발생!
    except:
        print('server error...')
    finally:
        close();
    time.sleep(3);
print('Terminated ....');
