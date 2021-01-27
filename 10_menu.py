from tkinter import * #티킨터 모듈에 있는 함수를 사용

"""기본 프레임 설정"""
root = Tk() # tk창 생성
root.title("JSY GUI") # 제목 설정
root.geometry("640x480")

"""
메뉴

전체적인 메뉴바를 선언한다.
그 메뉴는 root.config(menu=메뉴바 이름)으로 화면에 표시할 수 있음

그리고 menu에도 menu를 추가 할 수 있는데,
add_command():
    label: 이름
    command: 실행 함수

add_separator():
    구분자
    label: 이름

add_radiobutton():
    라디오 버튼
    label: 이름
    
add_cascade():
    메뉴 추가
    label: 추가할 메뉴 이름
    menu: 추가할 메뉴 객체
"""
def create_new_file():
    print("새 파일을 만듭니다.")

# 파일 메뉴
menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator() # 구분자
menu_file.add_command(label="Open File...")
menu_file.add_separator() # 구분자
menu_file.add_command(label="Save All", state="disable") #비활성화
menu_file.add_separator() # 구분자
menu_file.add_command(label="Exit", command=root.quit) #종료

menu.add_cascade(label="File", menu=menu_file)

# Edit 메뉴
menu.add_cascade(label="Edit")

# Language 메뉴 추가(라디오 버튼을 통해서 추가)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C/C++")

menu.add_cascade(label="Language", menu=menu_lang)

# View 메뉴 추가
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")

menu.add_cascade(label="View", menu=menu_view)

"""화면 출력"""
root.config(menu=menu)
root.mainloop() #창이 닫히지 않도록 하는 명령어