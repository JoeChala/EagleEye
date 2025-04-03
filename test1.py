from customtkinter import*
from forgot_password_1 import forgot_pass
root=CTk()
root.geometry("500x500")
#set_appearance_mode("system")
set_appearance_mode("dark")
#set_default_color_theme("dark-blue")
root.configure(bg=("gray", "black"))
#frame =CTkFrame(root,width=200,height=50,corner_radius=20)
#b=CTkComboBox(frame,width=100,height=30,state="readonly").pack(pady=40)
#frame.pack(pady=20)
b=CTkButton(root,command=forgot_pass,width=50,height=30,text="press",text_font=("Times new roman",15),corner_radius=10,border_width=0).pack(pady=30)

root.mainloop()
