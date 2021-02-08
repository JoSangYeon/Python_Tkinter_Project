from pynput import keyboard
from tkinter import *

class MyApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("JSY GUI")  # 제목 설정
        self.root.geometry("320x320")
        self.root.resizable(False, False)  # 창 크기 고정

        with keyboard.Listener(on_press=self.handlePress, on_release=self.handleRelease) as listener:
            listener.join()

        self.root.mainloop()

    def handlePress(key):
        print('Press: {}'.format(key))

    def handleRelease(key):
        print('Released: {}'.format(key))

        # 종료
        if key == keyboard.Key.esc:
            return False



def main():
    myapp = MyApp()

if __name__ == "__main__":
    main()