 #Decting a face in the given video...
from logging import root
from operator import and_
import cv2
import os.path
from customtkinter import*
from tkinter import *
from tkinter import ttk
from capture_samples_1 import capture_photos
import PIL
from PIL import Image, ImageTk
from os import path

#pop up window 
def capture_photos(root):
    root.geometry("800x500+0+0")
    root.title("Photo Samples")
    set_appearance_mode("dark")
    #root.configure(bg=("gray", "black"))
    varName = StringVar()
    picNo = IntVar()
    def set_val():
        varName.get()
        picNo.get()

    def xit_windo():
        root.quit()   
    
        
    frame = CTkFrame(root, width=330, height=350,corner_radius=15).place(x=240, y=60)
    img1 = Image.open(r"C:\Users\Joe\Desktop\project_gallery\login.png")
    img1 = img1.resize((80, 80), Image.ANTIALIAS)
    photoimage1 = ImageTk.PhotoImage(img1)
    lblimg1 = CTkLabel(frame,image=photoimage1,borderwidth=0, corner_radius=20,fg_color="#292d2e",bg_color="#292d2e").pack(pady=70)
    root.title("Capture Sample")
        #details label
    get_str = CTkLabel(frame, text="Fill in the details", text_font=("algerian", 15, "bold"), bg_color="#292d2e",corner_radius=10).place(x=295, y=150)
        #name label
    name = CTkLabel(frame, text="Name:", text_font=("times new roman", 15, "bold"),bg_color="#292d2e",corner_radius=20,width=40).place(x=240, y=220)
        #entry box 
    txt_name = CTkEntry(frame,placeholder_text="Enter name", textvariable = varName, placeholder_text_color="silver",text_font=("times new roman", 15),border_width=1,bg_color="#292d2e", width=220,height=30,corner_radius=10).place(x=325, y=220)
        #no.of samples label
    sample = CTkLabel(frame, text="No.of Photo samples :", text_font=("times new roman", 15,"bold"), bg_color="#292d2e",width=70).place(x=260, y=280)
        #combobox
    sam_no=CTkOptionMenu(frame,variable = picNo ,fg_color="#353638",bg_color="#292d2e",text_color="silver",text_font=("times new roman",15),values=["7", "14", "28"], width=100, height=30,hover=True).place(x=450, y=280)
    
        #ok button
    ok = CTkButton(frame,command=set_val, text="Ok",text_font=("times new roman", 14),border_width=0,corner_radius=10,bg_color="#292d2e").place(x=320, y=340, width=60, height=40)
        #save button
    xitbtn = CTkButton(frame,bg_color="#292d2e", command = xit_windo, text="Save", text_font=("times new roman", 14), border_width=0,corner_radius=10 ).place(x=450, y=340, width=80, height=40)
    def setNamePic():
            name = varName.get()
            picno = picNo.get()
            return (name, picno)
    root.mainloop()
        # Code behind Button's functionality 
    
    values = setNamePic()
    name = values[0]
    picno = values[1]
    Name = name
    shotsNum = picno
      
    #Locaction to create a new directry
    DIR = r"C:\Users\Joe\Desktop\Train"
    loc2create = os.path.join(DIR, Name)
    os.mkdir(loc2create)

    pic_no = 0

    #wbecam settings:
    vid = cv2.VideoCapture(0) #setting camera
    #dimensions of camera view
    vid.set(3, 400)
    vid.set(4, 1250)      
    #start recording
    while True:
        passed, frame = vid.read()
        reqpath = "C:\\Users\\Joe\\Desktop\\Train\\" + Name + "\\" + "img" + str(pic_no) + '.jpg'
        cv2.imwrite(reqpath, frame)
        stord = cv2.imread(reqpath)
        cv2.imshow("Image taken & strored:", stord)
        pic_no += 1
        print("no. of pictures", pic_no)

        #stop recording
        if pic_no == shotsNum:
             break;

    
    cv2.destroyAllWindows()
def displayScreen():
    sideroot = CTk()
    sideroot.geometry("500x100")
    set_appearance_mode("dark")
    lablfrm1 = CTkLabel(sideroot, bg_color = "black", text = "All pictures taken successfully.", text_font = ("Times New Roman",16, "bold"), fg_color = "white" ).pack(fil = BOTH, expand = True)
    sideroot.mainloop()
    
if __name__ == "__main__":
    root = CTk()
    capture_photos(root)
    
 