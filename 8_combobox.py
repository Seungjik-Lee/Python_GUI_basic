import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("SJ GUI")
root.geometry("640x480")
# root.geometry("640x480+100+300") #창의 가로*세로+x좌표+y좌표
# root.resizable(False, False) #x,y값 변경 불가 (창 크기 변경 불가)

#----------------------------------------------------------------------------콤보 박스
values = [str(i) + "일" for i in range(1, 32)] #1~31 까지의 숫자
combobox = ttk.Combobox(root, height=5, values=values) #목록 5개 보여주기
combobox.pack()
combobox.set("카드 결제일") #최초 목록 제목 설정, 버큰 클릭을 통한 값 설정도 가능

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly") #읽기 전용, 목록10개 보여주기
readonly_combobox.current(0) #0번째 인덱스 값 선택
readonly_combobox.pack()


def btncmd():
    print(combobox.get()) #선택된 값 표시
    print(readonly_combobox.get())

btn = Button(root, text="선택", command=btncmd)
btn.pack()


root.mainloop()