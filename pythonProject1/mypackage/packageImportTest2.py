#사용자정의 패키지의 모듈 import하고 테스트
# testPackage에서 myProduct 모듈을 import하고 작업
#from 패키지명 import 모듈명
from testPackage import myProduct,moduleB

myProduct.test1()
moduleB.test5()
#import 패키지명 이렇게 사용도 가능. 해당 패키지의 모든 모듈을 import