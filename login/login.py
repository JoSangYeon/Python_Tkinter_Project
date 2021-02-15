from tkinter import *  # 티킨터 모듈에 있는 함수를 사용
import tkinter.messagebox as msgbox
import sqlite3 # 유저 계정정보 연결

class User_Data:
    def __init__(self):
        """db파일 생성"""
        self.conn = sqlite3.connect("user_data.db", isolation_level=None)

        """커서 선언"""
        self.c = self.conn.cursor()

    def get_user_data(self):
        self.c.execute("SELECT * FROM user_table")
        data = self.c.fetchall()

        return data

    def add_user(self, id, pw):
        self.c.execute("INSERT INTO user_table(ID, PW) VALUES(?, ?)", (id, pw))
        return

class JSY_Login:
    ###User ID/PW data###
    # 튜플로 (id, pw)의 형태로 구성
    # 추후에 mysql 적용해서 구현할 예정
    # user = [("admin", "admin"),("whtkddus98", "sy1219")]

    ###유저 data 객체 생성###
    user = User_Data()

    def __init__(self):
        """
        생성자
        """
        ###메인 창 생성###
        self.root = Tk()
        self.root.title("JSY GUI")  # 제목 설정
        self.root.geometry("200x200")
        self.root.resizable(False, False)  # 창 크기 고정

        ###로그인 화면 로고(?)###
        self.main_logo = Label(self.root, text="JSY Login", font=("courier", 16, "bold"))
        self.main_logo.pack(padx=3, pady=3)

        ###ID/PW 입력창###
        self.id_pw_frame = LabelFrame(self.root, text="ID/PW")
        self.id_pw_frame.pack(fill="both", expand=True, padx=3, pady=3)

        self.id_frame = LabelFrame(self.id_pw_frame, text="ID : ")
        self.id_frame.pack(fill="both", expand=True)
        self.id_entry = Entry(self.id_frame)
        self.id_entry.pack(fill="both",expand=True, padx=3, pady=3)

        self.pw_frame = LabelFrame(self.id_pw_frame, text="PW : ")
        self.pw_frame.pack(fill="both", expand=True)
        self.pw_entry = Entry(self.pw_frame, show="*")
        self.pw_entry.pack(fill="both",expand=True, padx=3, pady=3)
        
        """회원가입 / 로그인 버튼"""
        self.assign_frame = Frame(self.root)
        self.assign_frame.pack(fill="both", expand=True, padx=3, pady=3)

        self.btn_login = Button(self.assign_frame, text="로그인", command=self.login)
        self.btn_login.pack(side="right", padx=3, pady=3)

        self.btn_assign = Button(self.assign_frame, text="회원가입",
                                 command=lambda: self.assign(self.id_entry.get(), self.pw_entry.get()))
        self.btn_assign.pack(side="left", padx=3, pady=3)

    def start(self):
        """프로그램 실행"""
        self.root.mainloop()

    def login(self):
        """로그인 버튼 command"""
        id_pw_set = (self.id_entry.get(), self.pw_entry.get())

        if len(id_pw_set[0]) == 0:
            msgbox.showwarning("로그인", "아이디를 입력해주세요")
            return
        elif len(id_pw_set[1]) == 0:
            msgbox.showwarning("로그인", "비밀번호를 입력하세요!")
            return

        if id_pw_set in self.user.get_user_data():
            print("로그인 성공")
        else:
            msgbox.showwarning("로그인", "올바르지 않은 ID/PW입니다.")
            return

    def assign(self, id, pw):
        """회원가입 command"""
        assign_root = assign(self.root)

class assign:
    """
    회원가입을 위한 클래스
    """
    def __init__(self, root):
        self.id_checking = False # 아이디 중복 확인을 위한 변수
        
        self.assign_window = Toplevel(root)
        self.assign_window.resizable(False, False)
        txt = Label(self.assign_window, text="회원가입", font=("courier", 16, "bold"))
        txt.pack()

        self.id_pw_check_frame = LabelFrame(self.assign_window, text="회원가입 ID/PW입력:")
        self.id_pw_check_frame.pack()

        self.id_frame = LabelFrame(self.id_pw_check_frame, text="ID:")
        self.id_frame.pack(fill="both", expand=True)
        self.id_entry = Entry(self.id_frame)
        self.id_entry.pack(side="left")
        self.id_check_btn = Button(self.id_frame, text="중복확인",
                                   command=lambda: self.id_check(self.id_entry.get()))
        self.id_check_btn.pack(side="right")

        self.pw_frame = LabelFrame(self.id_pw_check_frame, text="PW: ")
        self.pw_frame.pack(fill="both", expand=True)
        self.pw_entry = Entry(self.pw_frame, show="*")
        self.pw_entry.pack(fill="both")

        self.check_frame = LabelFrame(self.id_pw_check_frame, text="PW Check: ")
        self.check_frame.pack(fill="both", expand=True)
        self.check_entry = Entry(self.check_frame, show="*")
        self.check_entry.pack(fill="both")

        self.control_frame = Frame(self.assign_window)
        self.control_frame.pack(fill="both", expand=True)
        self.btn_create = Button(self.control_frame, text="생성", command=self.create_id)
        self.btn_create.pack()

    def id_check(self, id):
        ids, pws = zip(*JSY_Login.user.get_user_data())

        if id in ids:
            msgbox.showwarning("회원가입", "이미 사용중인 아이디입니다.")
            self.id_checking = False
        else:
            msgbox.showinfo("회원가입", "사용가능한 아이디입니다.")
            self.id_checking = True

    def create_id(self):
        if len(self.id_entry.get()) == 0:
            msgbox.showwarning("회원가입", "아이디를 입력해주세요")
            return
        
        if len(self.pw_entry.get()) == 0:
            msgbox.showwarning("회원가입", "비밀번호를 입력해주세요")
            return

        if len(self.check_entry.get()) == 0:
            msgbox.showwarning("회원가입", "비밀번호 확인을 입력해주세요")
            return
        
        if not self.id_checking:
            msgbox.showwarning("회원가입", "중복확인을 해주세요!")
            return
        elif self.pw_entry.get() != self.check_entry.get():
            msgbox.showwarning("회원가입", "비밀번호를 재확인해주세요!")
        else:
            JSY_Login.user.add_user(self.id_entry.get(), self.pw_entry.get())
            msgbox.showinfo("회원가입", "회원가입이 완료되었습니다.")
            self.assign_window.destroy()


def main():
    myApp = JSY_Login()
    myApp.start()


if __name__=="__main__":
    main()