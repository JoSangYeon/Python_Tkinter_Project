from tkinter import * #티킨터 모듈에 있는 함수를 사용

"""기본 프레임 설정"""
root = Tk() # tk창 생성
root.title("JSY GUI") # 제목 설정
root.geometry("640x480")

Label(root, text="메뉴를 선택해 주세요").pack(side="top")

Button(root, text="주문하기").pack(side="bottom")

"""
프레임

Frame():
    기본적인 프레임
    relief: 선 모양(soild, sunken, flat....)
    bd = 테두리 크기
    
LanelFrame():
    제목을 가진 프레임
    relief: 선 모양(soild, sunken, flat....)
    bd = 테두리 크기
    
pack()에 관한 내용:
    side = 위치시킬 자리를 정함(상하좌우)
    expand = 꽉차게 할지 않할지 설정
"""
#햄버거 frame#
frame_burger = Frame(root, relief="groove", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈햄버거").pack()
Button(frame_burger, text="치킨햄버거").pack()

#음료 frame#
frame_drink = LabelFrame(root, text="음료")
frame_drink.pack(side="right", fill="both", expand=True)

Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이드").pack()

"""화면 출력"""
root.mainloop() #창이 닫히지 않도록 하는 명령어