import pyautogui
import sqlite3
import time

if __name__ == "__main__":
    # DB 파일 연결
    conn = sqlite3.connect("mouse_position.db", isolation_level=None)
    c = conn.cursor()

    c.execute("select * from mouse_position")
    data = c.fetchall()
    for row in data:
        print(row)
    
    # 기존 좌표들 삭제
    conn.execute("DELETE FROM mouse_position")

    # 오류시 마우스를 좌상단으로 보내기
    pyautogui.PAUSE = 1
    pyautogui.FAILSAFE = True

    # 마우스 좌표 출력
    while True:
        print("Current Mouse Position : %d, %d" %(pyautogui.position().x, pyautogui.position().y))
        c.execute("INSERT INTO mouse_position(X, Y) VALUES(?,?)",
                  (pyautogui.position().x, pyautogui.position().y))
        time.sleep(1)