from tkinter import * #티킨터 모듈에 있는 함수를 사용

"""기본 프레임 설정"""
root = Tk() # tk창 생성
root.title("JSY GUI") # 제목 설정
root.geometry("640x480")

"""
그리드
격자 모양으로 위젯을 위치시킬 수 있다.

row: 행 좌표
column: 열 좌표
rowspan: 행으로 해당 수만큼 아래로 늘림
columnspan: 열으로 해당수 만큼 오른쪽으로 늘림
sticky: E,W,S,N(각각 동서남북) 각 좌표의 빈 공간을 각각의 방향으로 늘림
padx: 좌우의 간격을 넓힘
pady: 상하의 간격을 넓힘
"""
# btn1 = Button(root, text="버튼1")
# btn2 = Button(root, text="버튼2")
# btn1.grid(row=0, column=0)
# btn2.grid(row=1, column=1)

"""키패드 만들기"""
#첫번째 줄
btn_f16 = Button(root, text="F16", width=5, height=2)
btn_f17 = Button(root, text="F17", width=5, height=2)
btn_f18 = Button(root, text="F18", width=5, height=2)
btn_f19 = Button(root, text="F19", width=5, height=2)

btn_f16.grid(row=0,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_f17.grid(row=0,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_f18.grid(row=0,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_f19.grid(row=0,column=3, sticky=N+E+W+S, padx=3, pady=3)

#두번째 줄
btn_clear = Button(root, text="clear", width=5, height=2)
btn_equal = Button(root, text="=", width=5, height=2)
btn_div = Button(root, text="/", width=5, height=2)
btn_mul = Button(root, text="*", width=5, height=2)

btn_clear.grid(row=1,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_equal.grid(row=1,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_div.grid(row=1,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_mul.grid(row=1,column=3, sticky=N+E+W+S, padx=3, pady=3)

#세번째 줄
btn_7 = Button(root, text="7", width=5, height=2)
btn_8 = Button(root, text="8", width=5, height=2)
btn_9 = Button(root, text="9", width=5, height=2)
btn_sub = Button(root, text="-", width=5, height=2)

btn_7.grid(row=2,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_8.grid(row=2,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_9.grid(row=2,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_sub.grid(row=2,column=3, sticky=N+E+W+S, padx=3, pady=3)

#네번째 줄
btn_4 = Button(root, text="4", width=5, height=2)
btn_5 = Button(root, text="5", width=5, height=2)
btn_6 = Button(root, text="6", width=5, height=2)
btn_add = Button(root, text="+", width=5, height=2)

btn_4.grid(row=3,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_5.grid(row=3,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_6.grid(row=3,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_add.grid(row=3,column=3, sticky=N+E+W+S, padx=3, pady=3)

#다섯번째 줄
btn_1 = Button(root, text="1", width=5, height=2)
btn_2 = Button(root, text="2", width=5, height=2)
btn_3 = Button(root, text="3", width=5, height=2)
btn_enter = Button(root, text="enter", width=5, height=2)

btn_1.grid(row=4,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_2.grid(row=4,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_3.grid(row=4,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_enter.grid(row=4,column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3) #rowspan: 현재위치로부터 아래쪽으로 몇줄을 더함

#여섯번째 줄
btn_0 = Button(root, text="0", width=5, height=2)
btn_dot = Button(root, text=".", width=5, height=2)

btn_0.grid(row=5,column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3) #columnspan: 현재 위치로부터 오른쪽으로 몇줄을 더함
btn_dot.grid(row=5,column=2, sticky=N+E+W+S, padx=3, pady=3)


"""화면 출력"""
root.mainloop() #창이 닫히지 않도록 하는 명령어