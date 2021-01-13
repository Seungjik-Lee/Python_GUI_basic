import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("SJ GUI")
root.geometry("640x480")
# root.geometry("640x480+100+300") #창의 가로*세로+x좌표+y좌표
# root.resizable(False, False) #x,y값 변경 불가 (창 크기 변경 불가)

#----------------------------------------------------------------------------프로그레스 바
# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") #결정되지 않은 형태
progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") # 차오르는 형태
progressbar.start(10) #10ms 마다 움직임
progressbar.pack()

def btncmd():
    progressbar.stop() # 작동 중지

btn = Button(root, text="중지", command=btncmd)
btn.pack()


p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101): #1~100
        time.sleep(0.01) #0.01초 대기

        p_var2.set(i) #프로그레스 바의 값 설정
        progressbar2.update() # UI 업데이트
        print(p_var2.get()) 

btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop()