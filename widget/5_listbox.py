from tkinter import * #티킨터 모듈에 있는 함수를 사용

"""기본 프레임 설정"""
root = Tk() # tk창 생성
root.title("JSY GUI") # 제목 설정
root.geometry("640x480")

"""리스트 박스"""
# mode: single도 있다.
# height = 0은 모든 요소를 보요줄 만큼의 크기 설정
listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()


#리스트 박스 응용
def btncmd():
    """삭제"""
    listbox.delete(END) # 맨 뒤에 항목을 삭제
    listbox.delete(0) # 맨 앞의 항목을 삭제

    """개수 확인"""
    print("리스트에는", listbox.size(), "개가 있습니다.")

    """항목 확인"""
    print("1~3번째 항목:", listbox.get(0, 2))
    
    """선택된 항목 확인(인덱스 위치로 반환됨)"""
    print("선택된 항목:", listbox.curselection())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop() #창이 닫히지 않도록 하는 명령어