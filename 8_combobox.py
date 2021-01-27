from tkinter import * #티킨터 모듈에 있는 함수를 사용
import tkinter.ttk as ttk

"""기본 프레임 설정"""
root = Tk() # tk창 생성
root.title("JSY GUI") # 제목 설정
root.geometry("640x480")

"""콤보 박스"""
values = [str(i)+"일" for i in range(1,32)] # 1~31까지의 숫자
combobox = ttk.Combobox(root, height=5, values=values)

combobox.set("카드 결제일") #최초 목록 제목 설정
combobox.config(state="readonly") #읽기 전용 설정
combobox.pack()


values = [str(i)+"일" for i in range(1,32)] # 1~31까지의 숫자
r_combobox = ttk.Combobox(root, height=10, values=values, state="readonly")
r_combobox.current(0)
r_combobox.pack()

"""콤보 박스 응용"""
def btncmd():
    print(combobox.get()) #선택된 값을 출력
    print(r_combobox.get()) #선택된 값을 출력

btn = Button(root, text="선택", command=btncmd)
btn.pack()


root.mainloop() #창이 닫히지 않도록 하는 명령어