# 파이썬에서 제공되는 패키지를 import하고 작업
import urllib.request as request

url = "https://t1.daumcdn.net/daumtop_chanel/op/20200723055344399.png"
myimgPath = "daum.png"
request.urlretrieve(url,myimgPath)