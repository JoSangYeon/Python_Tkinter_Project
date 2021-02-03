from tkinter import *  # 티킨터 모듈에 있는 함수를 사용
import tkinter.messagebox as msgbox

class JSY_Login:
    ###User ID/PW data###
    # 튜플로 (id, pw)의 형태로 구성
    # 추후에 mysql 적용해서 구현할 예정
    user = [("admin", "admin"),("whtkddus98", "sy1219")]

    def __init__(self):
        """
        생성자
        """
        ###메인 창 생성###
        self.root = Tk()
        self.root.title("JSY GUI")  # 제목 설정
        self.root.resizable(False, False)  # 창 크기 고정

        ###로그인 화면 로고(?)###
        self.main_logo = Label(self.root, text="JSY Login", font=("courier", 16, "bold"))
        self.main_logo.pack()

        ###ID/PW 입력창###
        self.id_pw_frame = LabelFrame(self.root, text="ID/PW")
        self.id_pw_frame.pack()

        self.id_frame = LabelFrame(self.id_pw_frame, text="ID : ")
        self.id_frame.pack(fill="both", expand=True)
        self.id_entry = Entry(self.id_frame)
        self.id_entry.pack(expand=True)

        self.pw_frame = LabelFrame(self.id_pw_frame, text="PW : ")
        self.pw_frame.pack(fill="both", expand=True)
        self.pw_entry = Entry(self.pw_frame, show="*")
        self.pw_entry.pack(expand=True)

        self.assign_frame = Frame(self.root)
        self.assign_frame.pack(fill="both", expand=True)

        self.btn_login = Button(self.assign_frame, text="로그인", command=self.login)
        self.btn_login.pack(side="right")

        self.btn_assign = Button(self.assign_frame, text="회원가입",
                                 command=lambda: self.assign(self.id_entry.get(), self.pw_entry.get()))
        self.btn_assign.pack(side="left")

        self.start()

    def start(self):
        ###화면 출력 및 실행###
        self.root.mainloop()

    ###회원가입/로그인###
    def login(self):
        print("아이디:",self.id_entry.get())
        print("비밀번호:",self.pw_entry.get())

    def assign(self, id, pw):
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
        ids, pws = list(zip(*(JSY_Login.user)))
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
            JSY_Login.user.append((self.id_entry.get(), self.pw_entry.get()))
            msgbox.showinfo("회원가입", "회원가입이 완료되었습니다.")
            self.assign_window.destroy()

def main():
    myApp = JSY_Login()
    print("asd")

if __name__=="__main__":
    main()