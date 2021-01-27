from tkinter import * #티킨터 모듈에 있는 함수를 사용
import tkinter.ttk as ttk
import time

"""기본 프레임 설정"""
root = Tk() # tk창 생성
root.title("JSY GUI") # 제목 설정
root.geometry("640x480")

"""프로그래스 바"""
"""
mode:
    "indeterminate": 언제 끝날지 모르는 작업에 대한 모드(왔다갔다...)
    "determinate": 특정 작업에 대한 진행도를 표현하는 모드(0~100까지 이동)
length:
    프로그래스바의 길이
variable:
    값을 저장하는 var(보통 DoubleVar를 사용)
"""
progressbar1 = ttk.Progressbar(root, maximum=100, mode="indeterminate")
progressbar1.start(10) #10ms 마다 움직인다.
progressbar1.pack()

progressbar2 = ttk.Progressbar(root, maximum=100, mode="determinate")
progressbar2.start(20) #20ms 마다 움직인다.
progressbar2.pack()

"""프로그래스 바 응용"""
def btncmd():
    progressbar1.stop() #작동 중지

btn = Button(root, text="중지", command=btncmd)
btn.pack()

""" 진짜 작동하는 것 처럼 만들기 """
p_var2 = DoubleVar()
progressbar3 = ttk.Progressbar(root, maximum=100, mode="determinate", length=150, variable=p_var2)
progressbar3.pack()


def btncmd2():
    for i in range(1, 101): # 1 ~ 100
        time.sleep(0.01) # 0.01초 대기
        p_var2.set(i) # 프로그래스바의 값 설정
        progressbar3.update() #GUI가 업데이트 됨
        print(p_var2.get()) #프로그래스바의 값을 가져옴

btn2 = Button(root, text="시작", command=btncmd2)
btn2.pack()


root.mainloop() #창이 닫히지 않도록 하는 명령어