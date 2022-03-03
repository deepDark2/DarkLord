import random
def lotto():
    list1 = []
    i = 1
    while(i<=6):
        num = random.randint(1, 46) #1~45

        if num not in list1:
            list1.append(num)
            i = i +1
        else :
            pass
        if len(list1) == 6:
            break
    return list1

lotto_list = lotto()
print(lotto_list)
