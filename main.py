
from sugang_engine import *
from sugang_gui import *
import tkinter as tk

"""
수강 신청 매크로 ver 0.5
수정 날짜 2024.02.21
구현된 기능 : 이삭줍기c

설치 필요 라이브러리 puautogui , keyboard
1)윈도우 + R 눌러서 cmd 입력 후 엔터
2)pip install pyautogui 입력
3)pip install keyboard 입력q

기타 사항
이삭줍기 모드에서 포인터 위치 개수는 숭실대 기준으로 3개..아마두?
랜덤 속도 조절가능
q
"""

def main():
    root = tk.Tk()
    root.resizable(False,False)
    gui = SugangGui(root)
    root.mainloop()

if __name__ == "__main__":
    main()