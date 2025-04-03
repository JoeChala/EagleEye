import PIL
from customtkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector as ms
from secret_questions_1 import secret_questions


con = ms.connect(host = "localhost",user = "root",password="root",database="passworddb")
cursor1 = con.cursor()
cursor1.execute("select * from admin")
recordlist = list(cursor1.fetchall())




def forgot_pass():
    root = CTk()
    root.title("Forgot Password")
    root.geometry("1350x780+0+0")
    set_appearance_mode("dark")
    #root.configure(bg=("gray", "black"))
    varName = StringVar()
        
        # login frame
    frame = CTkFrame(root, width=340, height=450,corner_radius=15).place(x=500, y=170)
        # login background
        #bg = ImageTk.PhotoImage(image=PIL.Image.open(r"C:\Users\Joe\Desktop\project_gallery\login_bg2.jpg"))
        #lbl_bg = CTkLabel(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)
    get_str = CTkLabel(frame, text="Forgot Password", text_font=("times new roman", 20, "bold","underline"), bg_color="#292d2e",width=100,height=30).pack(pady=230)

#admin_no = CTkLabel(root, text="Admin UID", text_font=("times new roman", 15, "bold"), bg_color="#292d2e",width=100,height=30).pack(pady=1)
    admin=CTkLabel(frame,text="Admin UID", bg_color="#292d2e", text_font=("times new roman", 15, "bold")).place(x=510,y=350)
    txtuser = CTkEntry(frame, text_font=("times new roman", 15, "bold"),textvariable =varName,border_width=1,corner_radius=10,bg_color="#292d2e", width=280,placeholder_text="Enter Admin UID",placeholder_text_color="silver").place(x=525, y=380)
    def proceed():
        for record in recordlist:
            inp = varName.get()
            if inp == record[1]:
                root.destroy()
                secret_questions()
                    
                    
                
            elif varName.get() not in record :
                if recordlist.index(record) == len(recordlist) - 1:
                    messagebox.showerror("Error", "Invalid Admin UID")

    proceednbtn = CTkButton(frame, command=proceed, text="Proceed", text_font=("times new roman", 15, "bold"), border_width=1, bg_color="#292d2e", corner_radius=8, width=120, height=35).place(x=600, y=500)
        



    root.mainloop()
#forgot_pass()      
    
    
