import time

# 파이썬 이미지 라이브러리
from PIL import ImageGrab

time.sleep(5) # 5초 대기

for i in range(1, 11): # 1 ~ 10 2초간격
    img = ImageGrab.grab() #현재 스크린의 이미지를 가져옴
    img.save("image{}.png".format(i)) #파일로 저장
    time.sleep(2) # 2초 대기