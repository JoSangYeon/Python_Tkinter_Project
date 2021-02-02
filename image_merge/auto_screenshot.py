import keyboard
import time
# 파이썬 이미지 라이브러리
from PIL import ImageGrab

def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab() #현재 스크린의 이미지를 가져옴
    img.save("image{}.png".format(curr_time))  # 파일로

keyboard.add_hotkey("F9", screenshot) # 사용자가 f9를 누르면 스크린샷 저장
keyboard.add_hotkey("ctrl+shift+s", screenshot) # 사용자가 컨트롤+쉬프트+S를 누르면 스크린샷 저장

keyboard.wait("esc") # 사용자가 esc를 누를때 까지 프로그램 수행