from tkinter import *

"""메모장 main 창 생성"""
root = Tk()
root.title("제목없음 - Windows 메모장")
root.geometry("800x600")

"""스크롤 바"""
scroll = Scrollbar(root)
scroll.pack(side="right", fill="y")
"""텍스트 위젯"""
txt = Text(root) #텍스트 위젯 생성
txt.pack(fill="both", expand=True)
txt.config(yscrollcommand=scroll.set)
"""텍스트 위젯"""
scroll.config(command=txt.yview)
"""스크롤 바"""

"""상단 메뉴 구현"""
menu = Menu(root)

def create_file():
    """
    상단 메뉴의 파일->열기를 눌렀을때.
    mynote.txt의 내용이 출력됨
    """
    global txt
    txt.delete("1.0", END) #기존의 내용 삭제
    f = open("mynote.txt", "r")
    for line in f.readlines():
        txt.insert(END, line)
    f.close

def save_file():
    """
    상단 메뉴의 파일->저장을 눌렀을 때,
    화면에 입력한 문자열이 mynote.txt에 저장됨
    """
    global txt
    content = txt.get("1.0", END)
    f = open("mynote.txt", "w")
    f.write(content)
    f.close()

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=create_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator() #구분자
menu_file.add_command(label="닫기", command=root.quit)

menu.add_cascade(label="파일", menu=menu_file)

menu_edit = Menu(menu, tearoff=0)
menu_format = Menu(menu, tearoff=0)
menu_view = Menu(menu, tearoff=0)
menu_help = Menu(menu, tearoff=0)

menu.add_cascade(label="편집", menu=menu_edit)
menu.add_cascade(label="서식", menu=menu_format)
menu.add_cascade(label="보기", menu=menu_view)
menu.add_cascade(label="도움말", menu=menu_help)
"""상단 메뉴 구현"""

"""메모장 실행"""
root.config(menu=menu)
root.mainloop()
"""메모장 실행"""