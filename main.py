from tkinter import *
import qrcode
from PIL import Image, ImageTk

class Qr_Generator:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1000x600+200+50")
        self.root.title("QR Code Generator")
        self.root.resizable(False,False)

        self.var_emp_code=StringVar()
        self.var_name=StringVar()
        self.var_department=StringVar()
        self.var_designation=StringVar()

        # ------ Employee details windows -----------
        emp_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        emp_Frame.place(x=50, y=50, width=550,height=500)

        emp_title = Label(emp_Frame, text="Employee Details", font=("goudy old style",20), bg='#2E8BC0', fg='white').place(x=0,y=0,relwidth=1)
        lbl_id = Label(emp_Frame, text="Employee ID : ", font=('times new roman', 15, 'bold'), bg='white').place(x=50,y=60)
        lbl_name = Label(emp_Frame, text="Full Name : ", font=('times new roman', 15, 'bold'), bg='white').place(x=50,y=100)
        lbl_department = Label(emp_Frame, text="Department : ", font=('times new roman', 15, 'bold'), bg='white').place(x=50,y=140)
        lbl_designation = Label(emp_Frame, text="Designation : ", font=('times new roman', 15, 'bold'), bg='white').place(x=50,y=180)
        
        emp_id = Entry(emp_Frame, font=('times new roman', 15), textvariable=self.var_emp_code, bg='#B1D4E0').place(x=250,y=60)
        emp_name = Entry(emp_Frame, font=('times new roman', 15), textvariable=self.var_name, bg='#B1D4E0').place(x=250,y=100)
        emp_department = Entry(emp_Frame, font=('times new roman', 15), textvariable=self.var_department, bg='#B1D4E0').place(x=250,y=140)
        emp_designation = Entry(emp_Frame, font=('times new roman', 15), textvariable=self.var_designation, bg='#B1D4E0').place(x=250,y=180)

        btn_generator = Button(emp_Frame, text="QR Generate", command=self.Generate, font=('times new roman', 18, 'bold'),bg='#145DA0', fg='white').place(x=120,y=250,width=180,height=30)
        btn_clear = Button(emp_Frame, text="Clear", command=self.clear, font=('times new roman', 18, 'bold'),bg='#778899', fg='white').place(x=312,y=250,width=100,height=30)

        self.msg=''
        self.lbl_msg= Label(emp_Frame, text=self.msg, font=('times new roman', 20, 'bold'), bg='white', fg='green')
        self.lbl_msg.place(x=0, y=300,relwidth=1)

        #---------Employee QR Code window -----------

        qr_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        qr_Frame.place(x=650, y=50, width=300,height=500)

        qr_title = Label(qr_Frame, text="QR Code", font=("goudy old style",20), bg='#2E8BC0', fg='white').place(x=0,y=0,relwidth=1)
        self.qr_code = Label(qr_Frame, text='No QR\nAvailable', font=('times new roman', 15), bg='#4682B4', fg='white', bd=1, relief=RIDGE)
        self.qr_code.place(x=50, y=100, width=200, height=200)

    def clear(self):
        self.var_emp_code.set('')
        self.var_name.set('')
        self.var_department.set('')
        self.var_designation.set('')

        self.msg=''
        self.lbl_msg.config(text=self.msg)

        self.qr_code.config(image='')

    def Generate(self):
        if self.var_name.get()=='' or self.var_emp_code.get()=='' or self.var_department.get()=='' or self.var_designation.get()=='':
            self.msg='All fields are required !!!'
            self.lbl_msg.config(text=self.msg, fg='red')
        else:
            qr_data=(f"Employee ID : {self.var_emp_code.get()}\nEmployee Name : {self.var_name.get()}\nDepartment : {self.var_department.get()}\nDesignation : {self.var_designation.get()}")
            qr_codes = qrcode.make(qr_data)
            qr_codes = qr_codes.resize((200,200))
            qr_codes.save('Employee_QR/Emp_'+str(self.var_emp_code.get())+'.png')
            self.img=ImageTk.PhotoImage(file='Employee_QR/Emp_'+str(self.var_emp_code.get())+'.png')
            self.qr_code.config(image=self.img)
            self.msg='QR Generated Successfully !!!'
            self.lbl_msg.config(text=self.msg, fg='green')


root = Tk()
obj = Qr_Generator(root)
root.mainloop()