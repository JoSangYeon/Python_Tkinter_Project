from tkinter import *
import os

class Note:
    """
    Tkinter 모듈로 만든 메모장
    """
    def __init__(self, root):
        self.root = root
        self. scroll = Scrollbar(self.root)
        self.txt = Text(root)
        self.__set_scorll()
        self.__set_txt()

    def __set_txt(self):
        self.txt.pack(fill="both", expand=True)
        self.txt.config(yscrollcommand=self.scroll.set)
    def __set_scorll(self):
        self.scroll.pack(side="right", fill="y")
        self.scroll.config(command=self.txt.yview)

class Note_Menu():
    """
    Node class의 상단 메뉴
    """
    def __init__(self, root, txt):
        self.root = root
        self.menu = Menu(root)
        self.filename = "mynote.txt"
        self.txt = txt
        self.__create_menu()
        root.config(menu=self.menu)

    def __create_menu(self):
        menu_file = Menu(self.menu, tearoff=0)
        menu_file.add_command(label="열기", command=self.create_file)
        menu_file.add_command(label="저장", command=self.save_file)
        menu_file.add_separator()  # 구분자
        menu_file.add_command(label="닫기", command=self.root.quit)

        self.menu.add_cascade(label="파일", menu=menu_file)

        menu_edit = Menu(self.menu, tearoff=0)
        menu_format = Menu(self.menu, tearoff=0)
        menu_view = Menu(self.menu, tearoff=0)
        menu_help = Menu(self.menu, tearoff=0)

        self.menu.add_cascade(label="편집", menu=menu_edit)
        self.menu.add_cascade(label="서식", menu=menu_format)
        self.menu.add_cascade(label="보기", menu=menu_view)
        self.menu.add_cascade(label="도움말", menu=menu_help)

    def create_file(self):
        """
        상단 메뉴의 파일->열기를 눌렀을때.
        mynote.txt의 내용이 출력됨
        """
        self.txt.delete("1.0", END)  # 기존의 내용 삭제
        if os.path.isfile(self.filename):
            f = open(self.filename, "r", encoding="utf8")
            for line in f.readlines():
                self.txt.insert(END, line)
            f.close()

    def save_file(self):
        """
        상단 메뉴의 파일->저장을 눌렀을 때,
        화면에 입력한 문자열이 mynote.txt에 저장됨
        """
        content = self.txt.get("1.0", END)
        if os.path.isfile(self.filename):
            f = open(self.filename, "w")
            f.write(content)
            f.close()

def main():
    """메모장 main 창 생성"""
    root = Tk()
    root.title("제목없음 - Windows 메모장")
    root.geometry("800x600")

    note = Note(root)
    note_menu = Note_Menu(root, note.txt)

    root.mainloop()

if __name__ == "__main__":
    main()