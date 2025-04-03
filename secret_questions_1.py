import PIL
from tkinter import ttk
from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector as ms

con = ms.connect(host="localhost", user="root", password="root", database="passworddb")
cursor1 = con.cursor()
cursor1.execute("select * from admin")
recordlist = cursor1.fetchall()
#print(recordlist)

def secret_questions():
    #file_h = open('temp.txt', 'r')
    root = CTk()
    root.title("Forgot Password")
    root.geometry("1350x780+0+0")
    set_appearance_mode("dark")
    txt1=StringVar()
    txt2=StringVar()
    # txtuesr = IntVar()
    # txtpass = StringVar()

    # login background
    #bg = ImageTk.PhotoImage(image=PIL.Image.open(r"C:\Users\Joe\Desktop\project_gallery\login_bg2.jpg"))
    #lbl_bg = CTkLabel(root, image=bg)
    #lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
    # login frame
    frame = CTkFrame(root,corner_radius=15, width=350, height=450).place(x=500, y=170)

    #img1 = Image.open(r"C:\Users\Joe\Desktop\project_gallery\login.png")
    #img1 = img1.resize((100, 100), Image.ANTIALIAS)
    #photoimage1 = ImageTk.PhotoImage(img1)
    #lblimg1 = Label(image=photoimage1, bg="black", borderwidth=0)
    #lblimg1.place(x=520, y=175, width=100, height=100)

    get_str = CTkLabel(frame, text="Secret Questions", text_font=("times new roman", 20, "bold","underline"), bg_color="#292d2e").place(x=585, y=200)
    #print(file_h.read(1))
    #ques1 = recordlist[int(file_h.readline())][3]

    ques1 = CTkLabel(frame, text= "Favourite song", text_font=("times new roman", 15, "bold"),bg_color="#292d2e").place(x=535, y=270)

    txtuesr = CTkEntry(frame, text_font=("times new roman", 15, "bold"), textvariable=txt1,width=270,border_width=1,corner_radius=8,bg_color="#292d2e").place(x=540, y=300)

    ques2 = CTkLabel(frame, text= "First School", text_font=("times new roman", 15, "bold"),bg_color="#292d2e").place(x =520,y = 390)

    txtuesr2 = CTkEntry(frame, text_font=("times new roman", 15, "bold"), textvariable=txt2, width=270,border_width=1,corner_radius=8,bg_color="#292d2e" ).place(x=540, y=420)


    def proceed():
        for record in recordlist:
            inp = txt1.get()
            inp2 = txt2.get()
            #print(record[4])
            #print(record[6])
            if inp.lower() == record[4].lower() and inp2.lower() == record[6].lower():
                # print("check complete")
                # ind = str(recordlist.index(record))
                # file_h.write(ind)
                messagebox.showinfo("Success","Your password is:"+ record[2])
                root.destroy()
                break
                # Success button:
            # opnbtn=Button(source_from_cache,command=self.adminwind,text="Open",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="white",activeforeground="black",activebackground="white")
            # opnbtn.place(x=110,y=350,width=120,height=35)
            elif inp != record[4] and inp2 != record[6]and recordlist.index(record) == len(recordlist) - 1:
                messagebox.showerror("Error", "Wrong answer")
        
    enter = CTkButton(frame, command=proceed,text_color="white",text="Confirm", text_font=("times new roman", 12, "bold"),borderwidth=0,bg_color="#292d2e",corner_radius=9)
    enter.place(x=620, y=500, width=100,height=40)
    root.mainloop()

#secret_questions()