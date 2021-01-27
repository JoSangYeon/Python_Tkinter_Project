from tkinter import * #티킨터 모듈에 있는 함수를 사용

"""기본 프레임 설정"""
root = Tk() # tk창 생성
root.title("JSY GUI") # 제목 설정
root.geometry("640x480")

"""라디오 버튼"""
#variable이 같은 버튼끼리 같은 라디오 그룹이 됨

Label(root, text="메뉴를 선택하세요").pack()
# 여러개의 선택중 하나를 고르는 버튼
burger_var = IntVar() #int형으로 값을 저장함
btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn_burger2 = Radiobutton(root, text="치즈햄버거", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="치킨햄버거", value=3, variable=burger_var)

btn_burger1.select()
btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="음료를 선택하세요").pack()
#음료수 선택#

drink_var = StringVar() #str형으로 값을 저장함
btn_dringk1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_dringk2 = Radiobutton(root, text="콜라", value="사이다", variable=drink_var)
btn_dringk3 = Radiobutton(root, text="콜라", value="환타", variable=drink_var)

btn_dringk1.select()
btn_dringk1.pack()
btn_dringk2.pack()
btn_dringk3.pack()


"""라디오 버튼 응용"""
def btncmd():
    print(burger_var.get()) #선택된 라디오 항복의 값(value)을 출력
    print(drink_var.get())  # 선택된 라디오 항복의 값(value)을 출력

btn = Button(root, text="주문", command=btncmd)
btn.pack()


root.mainloop() #창이 닫히지 않도록 하는 명령어