from tkinter import * #티킨터 모듈에 있는 함수를 사용

"""기본 프레임 설정"""
root = Tk() # tk창 생성
root.title("JSY GUI") # 제목 설정
root.geometry("640x480")

"""
스크롤 바

"""
frame = Frame(root)
frame.pack()

# 스크롤바를 생성하고 frame의 왼쪽에 채움
scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# 리스트 박스에 yscrollcommand=scrollbar.set속성을 선언함으로 리스트박스에 스크롤바가 매핑됨
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)
for i in range(1,32): # 1~31일
    listbox.insert(END, str(i)+"일")
listbox.pack(side="left")

# 스크롤바에도 리스트박스를 매핑함
scrollbar.config(command=listbox.yview)

"""화면 출력"""
root.mainloop() #창이 닫히지 않도록 하는 명령어