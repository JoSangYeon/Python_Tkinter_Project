from tkinter import * #티킨터 모듈에 있는 함수를 사용
import tkinter.ttk as ttk
from tkinter import filedialog # 로컬 피시에 있는 파일을 불러올 수 있는 모듈
import tkinter.messagebox as msgbox

"""기본 프레임 설정"""
root = Tk() # tk창 생성
root.title("JSY GUI") # 제목 설정
root.resizable(False, False) #창 크기 고정

"""파일 추가 함수"""
def add_file():
    """
    filedialog.askopenfilenames(): 복수개의 파일을 선택하도록 함
        title : 제목
        filetypes : 파일의 확장자를 설정(튜플 형태로)
        initialdir : 최초의 경로를 설정
        return : Tuple
    """
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요",
            filetypes=(("PNG 파일", "*.png"), ("모든파일", "*.*")),
            initialdir=r"C:\Users\조상연\Pictures\Saved Pictures")

    # 사용자가 선택한 파일들을 목록에 추가함
    for file in files:
        list_file.insert(END, file) #list_file : listbox

"""선택 삭제 함수"""
def del_file():
    """
    Listbox.curselection()를 통해서 삭제할 사진들을 선택하고 뒤에서부터 삭제함
    :return:
    """
    # list_file에 선택된 사진들
    del_list = list_file.curselection()
    
    # 선택된 파일들을 삭제함
    for idx in reversed(del_list):
        list_file.delete(idx)

"""저장 경로 설정 함수"""
def browse_dest_path():
    """
    합병한 이미지를 저장할 경로를 설정하는 함수
    :return:
    """
    folder_selected = filedialog.askdirectory(title="저장할 경로를 설정하세요") #폴더를 선택하는 창을 띙움

    if folder_selected == None:
        return
    else:
        txt_dest_path.delete(0, END)
        txt_dest_path.insert(0, folder_selected)

"""이미지 합병 시작 버튼 함수"""
def start():
    """
    :return: 
    """
    # 각 옵션들 값을 확인
    print("가로넓이 :", cmb_width.get())
    print("간격 : ", cmb_space.get())
    print("포맷 : ", cmb_format.get())

    # 파일 목록 확인
    if list_file.size() == 0:
        msgbox.showwarning("경고", "이미지 파일을 추가하세요!")
        return
    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 선택하세요!")
        return

"""파일 프레임 (파일 추가, 선택 삭제)"""
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, text="파일추가", padx=5, pady=5, width=10, command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, text="선택삭제", padx=5, pady=5, width=10, command=del_file)
btn_del_file.pack(side="right")

"""리스트 프레임"""
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scroll = Scrollbar(list_frame)
scroll.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scroll.set)
list_file.pack(side="left", fill="both", expand=True)

scroll.config(command=list_file.yview)

"""저장 경로 프레임"""
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4, padx=5, pady=5) # ipady = 내부 높이변경

btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

"""옵션 프레임"""
option_frame = LabelFrame(root, text="옵션")
option_frame.pack(padx=5, pady=5, ipady=5)
# 가로 넓이 옵션
lbl_width = Label(option_frame, text="가로넓이", width=8)
lbl_width.pack(side="left", padx=5, pady=5)

# 가로 넓이 콤보
opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(option_frame, state="readonly", values=opt_width, width=10,)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# 간격 옵션
# 간격 옵션 레이블
lbl_space = Label(option_frame, text="간격", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

# 간격 옵션 콤보
opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(option_frame, state="readonly", values=opt_space, width=10,)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

# 파일 포맷 옵션
# 파일 포맷 레이블
lbl_format = Label(option_frame, text="포맷", width=8)
lbl_format.pack(side="left", padx=5, pady=5)

# 파일 포맷 콤보
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(option_frame, state="readonly", values=opt_format, width=10,)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)

"""진행 상황 프로그래스 바"""
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x",padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress.pack(fill="x")

"""실행 프레임"""
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)

"""메인 창 실행"""
root.mainloop() #창이 닫히지 않도록 하는 명령어