from tkinter import *

root = Tk()
root.title("SJ GUI")
# root.geometry("640x480+100+300") #창의 가로*세로+x좌표+y좌표
# root.resizable(False, False) #x,y값 변경 불가 (창 크기 변경 불가)

#--------------------------------------------------------------------------------------버튼 만들기
btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼2") #padx = 넓이, pady = 높낮이
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4") #고정된 크기
btn4.pack()

btn4 = Button(root, fg="red", bg="yellow", text="버튼5")
btn4.pack()

photo = PhotoImage(file="GUI_basic/img.png") #이미지로 버튼 만들기
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요")

btn7 = Button(root,text="동작하는 버튼", command=btncmd) 
btn7.pack()

root.mainloop()