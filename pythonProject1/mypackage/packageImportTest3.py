#다른 패키지에 있는 .py 파일 내의 기능을 이용하기!
#testPackage 패키지의 모든 모듈을 import 하기



import testPackage

testPackage.moduleA.test2()
testPackage.moduleB.test5()

#import 패키지명
#->

#해당 import 대상 패키지 파일 내의 __init__.py 에서 from . import 모듈 명 으로 import 선언(등록)을 해야 한다.
#이해안된다면 testPackage 내의 __init__.py를 열어서 확인할 것.
#testPackage 에서 mpProduct 모듈을 등록하지 않아서 사용할 수 없다.
# testPackage.myProduct.test1() 쓰고싶다면 등록작업 해보든가.