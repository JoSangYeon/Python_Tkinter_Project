"""
Project: 여러 이미지를 합치는 프로그램 작성

파일추가 : 리스트 박스에 파일 추가
선택삭제 : 리스트 박스에서 선택된 항목 삭제
찾아보기 : 저장 폴더를 선택하면 텍스트 위젯에 입력
가로넓이 : 이미지 넓이 지정 (원본유지, 1024, 800, 640)
간격 : 이미지 간의 간격 지정(없음, 좁게, 보통, 넓게)
포맷 : 저장 이미지 포맷 지정(PNG, JPG, BMP)
시작 : 이미지 합치기 작업 실행
진행상황: 현재 진행중인 파일 순서에 맞게 반영
닫기 : 프로그램 종료
"""
import os
from tkinter import *  # 티킨터 모듈에 있는 함수를 사용
import tkinter.ttk as ttk
from tkinter import filedialog  # 로컬 피시에 있는 파일을 불러올 수 있는 모듈
import tkinter.messagebox as msgbox
from PIL import Image #파이썬 이미지 라이브러리

class MyMerger:
    def __init__(self):
        self.root = Tk()  # tk창 생성
        self.root.title("JSY GUI")  # 제목 설정
        self.root.resizable(False, False)  # 창 크기 고정

        """파일 프레임 (파일 추가, 선택 삭제)"""
        self.file_frame = Frame(self.root)
        self.file_frame.pack(fill="x", padx=5, pady=5)

        self.btn_add_file = Button(self.file_frame, text="파일추가", padx=5, pady=5, width=10, command=self.add_file)
        self.btn_add_file.pack(side="left")

        self.btn_del_file = Button(self.file_frame, text="선택삭제", padx=5, pady=5, width=10, command=self.del_file)
        self.btn_del_file.pack(side="right")

        """리스트 프레임"""
        self.list_frame = Frame(self.root)
        self.list_frame.pack(fill="both", padx=5, pady=5)

        scroll = Scrollbar(self.list_frame)
        scroll.pack(side="right", fill="y")

        self.list_file = Listbox(self.list_frame, selectmode="extended", height=15, yscrollcommand=scroll.set)
        self.list_file.pack(side="left", fill="both", expand=True)

        scroll.config(command=self.list_file.yview)

        """저장 경로 프레임"""
        path_frame = LabelFrame(self.root, text="저장경로")
        path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

        self.txt_dest_path = Entry(path_frame)
        self.txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4, padx=5, pady=5)  # ipady = 내부 높이변경

        self.btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=self.browse_dest_path)
        self.btn_dest_path.pack(side="right", padx=5, pady=5)

        """옵션 프레임"""
        option_frame = LabelFrame(self.root, text="옵션")
        option_frame.pack(padx=5, pady=5, ipady=5)
        # 가로 넓이 옵션
        self.lbl_width = Label(option_frame, text="가로넓이", width=8)
        self.lbl_width.pack(side="left", padx=5, pady=5)

        # 가로 넓이 콤보
        self.opt_width = ["원본유지", "1024", "800", "640"]
        self.cmb_width = ttk.Combobox(option_frame, state="readonly", values=self.opt_width, width=10, )
        self.cmb_width.current(0)
        self.cmb_width.pack(side="left", padx=5, pady=5)

        # 간격 옵션
        # 간격 옵션 레이블
        self.lbl_space = Label(option_frame, text="간격", width=8)
        self.lbl_space.pack(side="left", padx=5, pady=5)

        # 간격 옵션 콤보
        self.opt_space = ["없음", "좁게", "보통", "넓게"]
        self.cmb_space = ttk.Combobox(option_frame, state="readonly", values=self.opt_space, width=10, )
        self.cmb_space.current(0)
        self.cmb_space.pack(side="left", padx=5, pady=5)

        # 파일 포맷 옵션
        # 파일 포맷 레이블
        self.lbl_format = Label(option_frame, text="포맷", width=8)
        self.lbl_format.pack(side="left", padx=5, pady=5)

        # 파일 포맷 콤보
        self.opt_format = ["PNG", "JPG", "BMP"]
        self.cmb_format = ttk.Combobox(option_frame, state="readonly", values=self.opt_format, width=10, )
        self.cmb_format.current(0)
        self.cmb_format.pack(side="left", padx=5, pady=5)

        """진행 상황 프로그래스 바"""
        frame_progress = LabelFrame(self.root, text="진행상황")
        frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

        self.p_var = DoubleVar()
        self.progress = ttk.Progressbar(frame_progress, maximum=100, variable=self.p_var)
        self.progress.pack(fill="x")

        """실행 프레임"""
        frame_run = Frame(self.root)
        frame_run.pack(fill="x", padx=5, pady=5)

        self.btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=self.root.quit)
        self.btn_close.pack(side="right", padx=5, pady=5)

        self.btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=self.start)
        self.btn_start.pack(side="right", padx=5, pady=5)

    def run(self):
        """메인 창 실행"""
        self.root.mainloop()  # 창이 닫히지 않도록 하는 명령어

    def add_file(self):
        """
        filedialog.askopenfilenames(): 복수개의 파일을 선택하도록 함
            title : 제목
            filetypes : 파일의 확장자를 설정(튜플 형태로)
            initialdir : 최초의 경로를 설정
            return : Tuple
        """
        files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요",
                                            filetypes=(("PNG 파일", "*.png"), ("모든파일", "*.*")),
                            initialdir=r"C:\Users\조상연\PycharmProjects\TkinterProject\image_merge\Screenshot")

        # 사용자가 선택한 파일들을 목록에 추가함
        for file in files:
            self.list_file.insert(END, file)  # list_file : listbox

    """선택 삭제 함수"""

    def del_file(self):
        """
        Listbox.curselection()를 통해서 삭제할 사진들을 선택하고 뒤에서부터 삭제함
        """
        # list_file에 선택된 사진들
        del_list = self.list_file.curselection()

        # 선택된 파일들을 삭제함
        for idx in reversed(del_list):
            self.list_file.delete(idx)

    """저장 경로 설정 함수"""

    def browse_dest_path(self):
        """
        합병한 이미지를 저장할 경로를 설정하는 함수
        :return:
        """
        folder_selected = filedialog.askdirectory(title="저장할 경로를 설정하세요")  # 폴더를 선택하는 창을 띙움

        if folder_selected == "":
            return
        else:
            self.txt_dest_path.delete(0, END)
            self.txt_dest_path.insert(0, folder_selected)

    def merge_image(self):
        try:
            # 가로 넓이
            img_width = self.cmb_width.get()
            if img_width == "원본유지":
                img_width = -1  # -1일때는 원본 기준으로 이미지 병함
            else:
                img_width = int(img_width)

            # 간격
            img_space = self.cmb_space.get()
            if img_space == "좁게":
                img_space = 30
            elif img_space == "보통":
                img_space = 60
            elif img_space == "넓게":
                img_space = 90
            else:
                img_space = 0

            # 포맷
            img_format = self.cmb_format.get().lower()  # 소문자로 변경

            image_list = self.list_file.get(0, END)  # 모든 파일 목록을 가지고 오기
            images = [Image.open(x) for x in image_list]

            # 이미지 사이즈 리스트에 넣어서 하나씩 처리
            image_sizes = []  # [(width1, height1) , (width2, height2) ... ]
            if img_width > -1:  # width값 변경
                image_sizes = [(int(img_width), int(img_width * x.size[1] / x.size[0])) for x in images]
                # 외항의 곱은 내항의 곱과 같다는 식을 적요해서 적용한 가로 비율에 대한 새로운 세로 비율을 얻어냄
            else:
                # 원본 사이즈 적용
                image_sizes = [(x.size[0], x.size[1]) for x in images]

            # 이미지들의 최대 너비 높이를 찾음
            # size -> size[0]= width, size[1]= height
            widths, heights = zip(*image_sizes)
            max_width, total_heights = max(widths), sum(heights)

            # 스케치북 준비
            if img_space > 0:
                total_heights += img_space * (len(images) - 1)

            result_img = Image.new("RGB", (max_width, total_heights), (255, 255, 255))  # 너비높이, 배경
            y_offset = 0  # y 위치(그림이 합쳐질때의 좌표)

            # 이미지 병합
            for idx, img in enumerate(images):
                # width가 원본유지가 아닐때에는 이미지 크기 조정
                if img_width > -1:
                    img = img.resize(image_sizes[idx])  # 새로운 사이즈 적용

                result_img.paste(img, (0, y_offset))
                y_offset += img.size[1] + img_space  # height의 값 만큼 더해 줌

                prog = (idx + 1) / len(images) * 100  # 실제 percent 정보를 계산
                self.p_var.set(prog)
                self.progress.update()

            # 저장경로 설정
            file_name = "merge_image." + img_format
            dest_path = os.path.join(self.txt_dest_path.get(), file_name)
            result_img.save(dest_path)

            # 작업 완료 알림림
            msgbox.showinfo("알림", "작업이 완료되었습니다.")
        except Exception as err:
            msgbox.showerror("에러", err)

    def start(self):
        """
        :return:
        """
        # 각 옵션들 값을 확인
        # print("가로넓이 :", cmb_width.get())
        # print("간격 : ", cmb_space.get())
        # print("포맷 : ", cmb_format.get())

        # 파일 목록 확인
        if self.list_file.size() == 0:
            msgbox.showwarning("경고", "이미지 파일을 추가하세요!")
            return
        # 저장 경로 확인
        if len(self.txt_dest_path.get()) == 0:
            msgbox.showwarning("경고", "저장 경로를 선택하세요!")
            return

        # 이미지 통합 작업
        self.merge_image()


def main():
    mymerger = MyMerger()
    mymerger.run()


if __name__ == "__main__":
    main()
