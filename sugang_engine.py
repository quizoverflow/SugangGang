import pyautogui as macro
import time
import random as rand
from pynput import keyboard
import keyboard as key
import tkinter as tk
import tkinter.ttk as ttk
from datetime import datetime
    

class Engine():
    def __init__(self,key_setting,loc):
        self.key_sets = key_setting
        self.quit_key = key_setting[0]
        self.set_key = key_setting[1]
        self.amount = int(key_setting[2])
        self.speed = int(key_setting[3])
        self.location = loc

        self.macro_count = 0
        self.keep_going= True

        self.engine_window = tk.Toplevel()
        self.engine_window.title("매크로 동작중")
        self.engine_window.geometry("260x200-0-0")
        self.engine_window.resizable(False,False)
        self.engine_window.wm_attributes("-topmost",1)
        self.engine_window.attributes('-alpha',0.9)

        self.text_label = tk.Label(self.engine_window, text= f"<{self.quit_key}키를 눌러 중지할 수 있습니다>", font =("Arial",9))
        self.text_label.pack()
        self.count_label = tk.Label(self.engine_window, text= f"{self.macro_count}회 작동", font=("Arial", 20))
        self.count_label.pack()
        self.current_time_label = tk.Label(self.engine_window,font=("Arial",12))
        self.current_time_label.pack()
        self.timer_label = tk.Label(self.engine_window,font = ("Arial",12))
        self.timer_label.pack()
        self.slide_bar = ttk.Scale(self.engine_window, from_ =0.1, to=1.0,value = 1, orient= "horizontal",command= self.slide)
        self.slide_bar.pack(pady=1)

        self.update_current_time()
        self.start_time = datetime.now()
        
        # 리스너 시작
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

    def slide(self,_):
        self.engine_window.attributes('-alpha',self.slide_bar.get())

    def update_current_time(self):
        # 현재 시각 업데이트
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.current_time_label.config(text="현재 시각\n" + current_time)
        self.engine_window.after(1000, self.update_current_time)  # 1초마다 업데이트

    def update_start_time(self):
        # 창 실행 시간 업데이트
        start_time_str = self.start_time.strftime("%Y-%m-%d %H:%M:%S")
        self.timer_label.config(text="시작 시간: " + start_time_str)
    
    def on_press(self,key):
            if key == keyboard.KeyCode.from_char(self.quit_key):
                self.listener.stop()
                self.keep_going = False
                return False
            #esc 눌려도 리스너 종료
            if key == keyboard.Key.esc:
                self.listener.stop()
                self.keep_going = False
                return False
            
    def EngineStart(self):
        idx = 0
        while self.keep_going == True:
            macro.moveTo(self.location[idx])
            idx += 1
            idx %= self.amount
            if idx == 0:
                self.macro_count += 1
                self.count_label.config(text = f"{self.macro_count}회 작동")
            macro.click()
            time.sleep(rand.uniform(0.5/self.speed,2/self.speed))
        



"""
class Hook(threading.Thread):
    def __init__(self):
            super(Hook, self).__init__()  # parent class __init__ 실행
            self.daemon = True  # 데몬쓰레드로 설정
            self.event = False  # f4가 눌리면 event 발생
            key.unhook_all()  # 후킹 초기화
            key.add_hotkey('q', print, args=['\nq was pressed'])  # q가 눌리면 print 실행
    def run(self):  # run method override
        print('Hooking Started')
        while True:
            k = key.read_hotkey(suppress=False)  # hotkey를 계속 읽음
            if k == 'q':  # q 받은 경우
                self.event = True  # event 클래스 변수를 True로 설정
                break  # 반복문 탈출)
                
class Picking():
    def __init__(self,key_setting):
        print("이삭줍기 모드")
        self.points = int(input("포인터 위치 개수 입력"))
        self.location = []

    def GetLocation(self):
        for i in range(self.points):
            print(f"2초 내로 {i} 번 째 위치로 마우스를 이동하세요")
            time.sleep(2)
            loc = macro.position()
            self.location.append(loc)
        print("위치 선정이 종료되었습니다.")    
    def pick(self):
        idx = 0
        while True:
            if key.is_pressed('q'):
                sys.exit()
            macro.moveTo(self.location[idx])
            idx = idx + 1
            idx = idx % self.points
            macro.click()
            time.sleep(rand.uniform(0.5,2))

if __name__ == '__main__':             
    hook = Hook()
    picker = Picking()
    hook.start()
    picker.GetLocation()
    picker.pick()
    hook.join()
    key.unhook_all()
"""