from tkinter import * #티킨터 모듈에 있는 함수를 사용

root = Tk() # tk창 생성

root.title("JSY GUI") # 제목 설정
root.geometry("640x480+100+300") # 크기/위치 설정 (가로*세로+x좌표+y좌료)
root.resizable(False, False) #창 크기 변경 (너비, 높이)

root.mainloop() #창이 닫히지 않도록 하는 명령어