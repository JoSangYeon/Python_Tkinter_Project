from tkinter import * #티킨터 모듈에 있는 함수를 사용

"""기본 프레임 설정"""
root = Tk() # tk창 생성
root.title("JSY GUI") # 제목 설정
root.geometry("640x480")

"""레이블""" #글자를 보여준다, 이미지를 보여준다...
lable1 = Label(root, text="안녕하세요")
lable1.pack()

#이미지 레이블
photo = PhotoImage(file="image1.png")
lable2 = Label(root, image=photo)
lable2.pack()

#버튼을 눌렀을때 동작하는 레이블
def change():
    lable1.config(text="또 만나요")

    global photo2
    photo2 = PhotoImage(file="image2.png")
    lable2.config(image=photo2)

btn = Button(root, text="클릭!", command=change)
btn.pack()


root.mainloop() #창이 닫히지 않도록 하는 명령어