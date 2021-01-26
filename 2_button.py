from tkinter import * #티킨터 모듈에 있는 함수를 사용

"""기본 프레임 설정"""
root = Tk() # tk창 생성
root.title("JSY GUI") # 제목 설정

"""버튼 위젯"""
btn1 = Button(root, text="버튼 1") # 버튼 객체 생성
btn1.pack() #버튼 객체를 root 윈도우에 추가함

# padx: 버튼 좌우 너비 조절(여백 너비)
# pady: 버튼 상하 너비 조절(여백 너비)
btn2 = Button(root, padx=5, pady=10,text="버튼 23456767")
btn2.pack()
btn3 = Button(root, padx=10, pady=5,text="버튼 3")
btn3.pack()

# width: 버튼 너비(고정크기)
# height: 버튼 높이(고정크기)
btn4 = Button(root, width=10, height=3, text="버튼 44444444")
btn4.pack()

#fg: 글자색
#bg: 배경색
btn5 = Button(root, fg="red", bg="yellow", text="버튼 5")
btn5.pack()

#이미지 버튼 생성
photo = PhotoImage(file="image1.png")
btn6 = Button(root, image=photo)
btn6.pack()

#버튼 동작 예제
#command 속성: 버튼의 동작하는 함수를 인자로 받음
def btncmd():
    print("버튼이 클릭되었습니다!")

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()


root.mainloop() #창이 닫히지 않도록 하는 명령어