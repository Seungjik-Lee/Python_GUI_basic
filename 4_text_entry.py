from tkinter import *

root = Tk()
root.title("SJ GUI")
root.geometry("640x480")
# root.geometry("640x480+100+300") #창의 가로*세로+x좌표+y좌표
# root.resizable(False, False) #x,y값 변경 불가 (창 크기 변경 불가)

#----------------------------------------------------------------------------텍스트 & 앤트리
txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30)
e.pack()
e.insert(0, "한 줄만 입력해요") #0==END

def btncmd(): 
    #내용 출력
    print(txt.get("1.0", END)) #1: 첫 번째 라인, 0: 0번째  colum 위치
    print(e.get())

    #내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()








root.mainloop()