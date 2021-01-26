from tkinter import * #티킨터 모듈에 있는 함수를 사용

"""기본 프레임 설정"""
root = Tk() # tk창 생성
root.title("JSY GUI") # 제목 설정
root.geometry("640x480")

"""텍스트, 엔트리"""
#텍스트 위젯
txt = Text(root, width=30, height=5) #텍스트 위젯 생성
txt.insert(END, "글자를 입력하세요!") #텍스트 위젯에 기본설정된 글 추가
txt.pack()

#엔트리 => 엔트리는 한줄로 입력을 받는다.(엔터를 쓸 수 없다.)
e = Entry(root, width=30)
e.insert(0, "한 줄만 입력됩니다!")
e.pack()

#텍스트, 엔트리 응용
def btncmd():
    #내용 출력
    # 1: 첫번째 라인, 0: 0번째 column 위치
    print(txt.get("1.0", END)) # 첫번째 줄(1)의 0번째 인덱스부터 문자열을 가져옴
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop() #창이 닫히지 않도록 하는 명령어