from ast import Pass
from msilib.schema import Class
from customtkinter import*
from PIL import Image, ImageTk

class capture_photos:
    
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x500+0+0")
        self.varName = StringVar()
        self.picNo = IntVar()
        #self.root.configure(bg=("gray", "black"))
        set_appearance_mode("dark")
        def set_val():
            self.varName.get()
            self.picNo.get()
        def xit_windo():
            root.quit()
        # frame
        
        frame = CTkFrame(self.root, width=330, height=350,corner_radius=15).place(x=240, y=60)
        img1 = Image.open(r"C:\Users\Joe\Desktop\project_gallery\login.png")
        img1 = img1.resize((80, 80), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = CTkLabel(frame,image=self.photoimage1,borderwidth=0, corner_radius=20,fg_color="#292d2e",bg_color="#292d2e").pack(pady=70)
        self.root.title("Capture Sample")
        #details label
        get_str = CTkLabel(frame, text="Fill in the details", text_font=("algerian", 15, "bold"), bg_color="#292d2e",corner_radius=10).place(x=290, y=150)
        #name label
        name = CTkLabel(frame, text="Name:", text_font=("times new roman", 15, "bold"),bg_color="#292d2e",corner_radius=20,width=40).place(x=240, y=220)
        #entry box 
        txt_name = CTkEntry(frame,placeholder_text="Enter name", textvariable = self.varName, placeholder_text_color="silver",text_font=("times new roman", 15),border_width=1,bg_color="#292d2e", width=220,height=30,corner_radius=10).place(x=325, y=220)
        #no.of samples label
        sample = CTkLabel(frame, text="No.of Photo samples :", text_font=("times new roman", 15,"bold"), bg_color="#292d2e",width=70).place(x=260, y=280)
        #combobox
        sam_no=CTkComboBox(frame,variable = self.picNo ,fg_color="#353638",bg_color="#292d2e",border_width=2,text_color="silver",text_font=("times new roman",15),values=["7", "14", "28"], width=100, height=30,hover=True).place(x=450, y=280)
        #ok button
        ok = CTkButton(frame,command=set_val, text="Ok",text_font=("times new roman", 14),border_width=0,corner_radius=10,bg_color="#292d2e").place(x=320, y=340, width=60, height=40)
        #save button
        xitbtn = CTkButton(frame,bg_color="#292d2e", command = xit_windo, text="Save", text_font=("times new roman", 14), border_width=0,corner_radius=10 ).place(x=450, y=340, width=80, height=40)
    def setNamePic(self):
            name = self.varName.get()
            picno = self.picNo.get()
            return (name, picno)
           
if __name__ == "__main__":
    pass
    root = CTk()
    root.mainloop()
    obj = capture_photos(root)
    funcout = obj.setNamePic()
    print(funcout)
    
    




