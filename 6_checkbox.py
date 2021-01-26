from tkinter import * #티킨터 모듈에 있는 함수를 사용

"""기본 프레임 설정"""
root = Tk() # tk창 생성
root.title("JSY GUI") # 제목 설정
root.geometry("640x480")

"""체크 박스"""
# variable: 체크박스의 상태를 저장할 변수를 설정해야함
checkvar = IntVar() #checkvar에 int형으로 값을 저장한다.
checkBox = Checkbutton(root, text="오늘 하루 보지 않기", variable=checkvar)

# checkBox.select() # 선택처리
# checkBox.deselect() # 선택해제 처리
checkBox.pack()

checkvar2 = IntVar()
checkBox2 = Checkbutton(root, text = "일주일동안 보지 않기", variable=checkvar2)
checkBox2.pack()


"""체크 박스 응용"""
def btncmd():
    print(checkvar.get()) # 0: 체크해제, 1:체크됨
    print(checkvar2.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop() #창이 닫히지 않도록 하는 명령어