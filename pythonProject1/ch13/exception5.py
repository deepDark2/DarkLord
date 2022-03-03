#으음!!
import random
import time


def connect(num):
    if num == 5:
        return 1;
        print('Connected');
    else:
        raise IOError;
try:
    n = random.randint(1,10);
    connect(n);
except:
    while True:
        n = random.randint(1, 10);
        try:
            result = connect(n);
            if result == 1:
                break;
        except:
            print('retry ...')
            time.sleep(3)
print('On going ...');



