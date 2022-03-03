num1 = 10;
num2 = 2.34;
st = 'abc';
sql = 'INSERT INTO TB VALUES(%s,%d,%f)';
print(sql % (st,num1,num2));#DB 이용시 이러한 포매팅 이용!

st2 = 'jmlee@tonsol.com';
#슬라이싱
#위 E-mail주소에서 ID 를 출력

print(st2[0:st2.find('@')])

#도메인(@이후)를 출력
print(st2[st2.find('@')+1:st2.find('.')])


nums = input('input 3 numbers ... ');

print(nums)
lnums = nums.split();#split은 많이 쓰이는 기능이니 참고.
print(lnums)
lnums2 = []
for n in lnums:
    lnums2.append(int(n));
print(lnums2)

#리스트[],튜플(),딕셔너리{} - 자료구조에서 주로 쓰임.
#이 세가지와 함수를 중점적으로 학습해둔다.
#리스트와 튜플 간 변환힐 시 list(), tuple() 함수를 이용해서 변환!
#EX) list(튜플 명)
