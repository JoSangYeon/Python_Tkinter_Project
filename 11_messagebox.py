from tkinter import * #티킨터 모듈에 있는 함수를 사용
import tkinter.messagebox as msgbox

"""기본 프레임 설정"""
root = Tk() # tk창 생성
root.title("JSY GUI") # 제목 설정
root.geometry("640x480")

"""
메세지 박스

showinfo(a, b): title=a, message=b
    a제목에 b내용을 가진 알림 창 출력
    
showwarning(a, b):
    a제목에 b내용을 가진 경고 창 출력
    
showerror(a, b):
    a제목에 b내용을 가진 에러창 출력
    
askokcancel(a,b):
    a제목에 b내용을 가진 확인/취소창 출력

askretrycancel(a, b):
    a제목에 b내용을 가진 다시시도/취소창 출력
    
askyesno(a, b):
    a제목에 b내용을 가진 예/아니오 창 출력
    
askyesnocancel(a, b):
    a제목에 b내용을 가진 예/아니오/취소 창 출력
    
해당 함수들의 출력값은 각가가 True, False, None이다.
"""
#기차 예매 시스템이라 가정
def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")

def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진되었습니다.")

def error():
    msgbox.showerror("에러", "결제 오류가 발생했습니다.")

def okcancel():
    msgbox.askokcancel("확인/취소", "확인 취소 버튼 클릭하세용")
    
def retrycancel():
    response = msgbox.askretrycancel("재시도 / 취소", "다시 시도 취소")
    
    print("응답:", response)
    if response == True: #재시도
        print("예") 
    elif response == False: #취소
        print("아니오")
    else: # None
        print("취소")
    
def yesno():
    msgbox.askyesno("예 / 아니오", "예 아니오")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다.\n종료하시겠습니까?")

    print("응답:", response)
    if response == True:
        print("예")
    elif response == False:
        print("아니오")
    else: # None
        print("취소")

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()
Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()

"""화면 출력"""
root.mainloop() #창이 닫히지 않도록 하는 명령어