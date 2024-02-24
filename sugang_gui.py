import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import sugang_engine as engine
import keyboard
import pyautogui as macro
from pynput import keyboard

class SugangGui():

    def __init__(self,home):
        self.home = home
        self.key_sets = [
            "q", #디폴트 중지 키는 q
            "c", #디폴트 포인터 설정 키는 c
            "3", #디폴트 클릭 개수
            "1", #디폴트 매크로 속도
            ]
        home.title("수강신청 매크로")
        home.geometry("330x265")
        #home.wm_attributes("-topmost", 2)

        self.macro_point_order = []

        #home frame
        padding = 4
        main_frame = tk.Frame(home)
        main_label_frame = tk.Frame(main_frame)
        body_frame = tk.Frame(main_frame)
        btn_frame = tk.Frame(body_frame)
        list_frame = tk.Frame(body_frame)
        bottom_frame = tk.Frame(main_frame)

        main_frame.pack()
        main_label_frame.pack(side = "top", pady = padding)
        body_frame.pack(side ="top")
        btn_frame.pack(side="left",padx = 20)
        list_frame.pack(side = "right")
        bottom_frame.pack(side = "bottom",pady= 1)

        text_style = tkFont.Font(family="Arial", size = 14)
        title_label = tk.Label(main_label_frame, text = "Sugang gang ver 0.5", font = text_style)
        title_label.pack()

        #매크로 제작 버튼
        btn_make_point = tk.Button(btn_frame, text = "매크로 제작", width = 10,command= self.MakeMacroPoint)
        btn_make_point.pack(side = "top", pady = 5)
        
        # 시작 버튼
        btn_start = tk.Button(btn_frame, text = "매크로 시작", width = 10,command = self.StartMacro)
        btn_start.pack(side = "top",pady = 5)        

        # 삭제 버튼
        btn_delete = tk.Button (btn_frame, text = "순서 삭제", width = 10,command=self.DeleteOrder)
        btn_delete.pack(side = "top", pady = 5)

        # 초기화 버튼
        btn_init = tk.Button(btn_frame, text = "순서 초기화", width = 10,command=self.InitOrder)
        btn_init.pack(side = "top",pady = 5)
        
        #설정 버튼
        btn_setting = tk.Button(btn_frame, text = "키 설정", command= self.SetKeys, width= 10)
        btn_setting.pack(side = "top",pady = 5)

        #리스트 박스
        self.listbox = tk.Listbox(list_frame,width= 24)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # 스크롤바 생성, 연결
        scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)

        #아래 뻘글
        dog_sound = tk.Label(bottom_frame,text = "2024.02.22\nsugang gang ver 0.5\nGit hub : quizoverflow")
        dog_sound.pack(side = "top")
    

    #키보드 리스너
    def on_press(self,key):
            #print('Key %s pressed' %key)
            #print(self.mk)
            set_key = self.key_sets[1]
            amount = int(self.key_sets[2])
            if key == keyboard.KeyCode.from_char(set_key):
                pos = macro.position()
                self.macro_point_order.append(pos)
                #print("현재 저장된 마우스 위치 개수 : ",len(self.order))
                self.count += 1
                self.label.config(text = str(amount - self.count))
                text_data = f"{self.count}번: x = {pos.x} | y = {pos.y}"
                self.listbox.insert(self.count-1,text_data)
                if(self.count == amount):
                    self.listener.stop()
                    self.order_window.destroy()
                    return False

            #esc 눌리면 리스너 종료
            if key == keyboard.Key.esc:
                print("리스너 종료")
                return False
            
    def slide(self,_):
        self.order_window.attributes('-alpha',self.slide_bar.get())

    #매크로 제작
    def MakeMacroPoint(self):
        amount = int(self.key_sets[2])
        self.order =[]
        self.count = 0

        self.order_window = tk.Toplevel(self.home)
        self.order_window.title(f"매크로 제작중\n{self.key_sets[1]}키를 눌러 설정")
        self.order_window.geometry("200x130-0-0")
        self.order_window.resizable(False,False)
        self.order_window.wm_attributes("-topmost",1)
        self.order_window.attributes('-alpha',0.9)

        self.text_label = tk.Label(self.order_window, text= "남은 지정 횟수", font =("Arial",15))
        self.text_label.pack()
        self.label = tk.Label(self.order_window, text= f"{amount - self.count}", font=("Arial", 40))
        self.label.pack()
        self.slide_bar = ttk.Scale(self.order_window, from_ =0.1, to=1.0,value = 1, orient= "horizontal",command= self.slide)
        self.slide_bar.pack(pady=1)


        self.listener = keyboard.Listener(on_press=self.on_press)
        # 리스너 시작
        self.listener.start()
    
    #매크로 시작
    def StartMacro(self):
        mac = engine.Engine(self.key_sets,self.macro_point_order)
        mac.update_start_time()
        mac.EngineStart()
        #엔진 인스턴스 소멸
        #del mac

    #매크로 셀 하나 삭제
    def DeleteOrder(self):
        selectedIdx = self.listbox.curselection()
        self.listbox.delete(selectedIdx)

    #매크로 초기화
    def InitOrder(self):
        self.listbox.delete(0,self.listbox.size()-1)
        
    #설정 버튼 동작
    def SetKeys(self):
        self.set_keys_window = tk.Toplevel(self.home)
        self.set_keys_window.title("키 설정")
        self.set_keys_window.geometry("300x200")
        self.set_keys_window.resizable(False,False)
        self.set_keys_window.wm_attributes("-topmost", 0)

        # frame , entry, label, button


        label_frame = tk.Frame(self.set_keys_window)
        label = tk.Label(label_frame, text = "키 설정",font = 5)

        entry_frame = tk.Frame(self.set_keys_window)
        entry_left_frame = tk.Frame(entry_frame)
        entry_right_frame = tk.Frame(entry_frame)

        quit_key_entry = tk.Entry(entry_right_frame)
        quit_key_entry.insert(0,self.key_sets[0])
        quit_label = tk.Label(entry_left_frame, text= "매크로 종료 키" )

        point_key_entry = tk.Entry(entry_right_frame)
        point_key_entry.insert(0,self.key_sets[1])
        point_label = tk.Label(entry_left_frame,text= "포인터 설정 키")

        point_count_entry = tk.Entry(entry_right_frame)
        point_count_entry.insert(0,self.key_sets[2])
        point_count_label = tk.Label(entry_left_frame, text = "클릭 개수")

        point_speed_entry = tk.Entry(entry_right_frame)
        point_speed_entry.insert(0,self.key_sets[3])
        point_speed_label = tk.Label(entry_left_frame,text = "포인터 속도")

        btn_get_settings = tk.Button(self.set_keys_window, text = "적용하기", command= lambda : self.get_settings_destroy(quit_key_entry,point_key_entry,point_count_entry,point_speed_entry))

        #=== pack ===
        padding = 3
        label_frame.pack(side = "top",pady = 5)
        label.pack()
        entry_frame.pack(side = "top",pady = 5)
        entry_left_frame.pack(side= "left")
        entry_right_frame.pack(side ="right")

        quit_label.pack(side = "top",pady = padding)
        quit_key_entry.pack(side = "top",pady = padding)

        point_count_label.pack(side = "top",pady = padding)
        point_count_entry.pack(side = "top",pady = padding)

        point_label.pack(side = "top",pady = padding)
        point_key_entry.pack(side ="top",pady = padding)

        point_speed_label.pack(side = "top",pady = padding)
        point_speed_entry.pack(side = "top",pady = padding)

        btn_get_settings.pack(side = "top",pady = padding * 3)

    
    def get_settings_destroy(self,entry0, entry1,entry2,entry3):
        self.key_sets[0] = entry0.get()
        self.key_sets[1] = entry1.get()
        self.key_sets[2] = entry2.get()
        self.key_sets[3] = entry3.get()

        for i in self.key_sets:
            print(i)
        
        self.set_keys_window.destroy()
        


    


        


    
        






