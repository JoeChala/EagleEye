
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector as ms
mycon=ms.connect(host='localhost',user='root',password='root',database='cbse_compsci_proj')
mycursor=mycon.cursor()

class Update_id:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x780+0+0")
        self.root.title("Update id")
        #image1
        img = Image.open(r"C:\Users\Joe\Desktop\project_gallery\daaah.jpg")
        img = img.resize((460, 135),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x = 0, y = 0, width = 460, height = 135)
        
        #image2
        img1 = Image.open(r"C:\Users\Joe\Desktop\project_gallery\update.jpg")
        img1= img1.resize((480, 135),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root,image = self.photoimg1)
        f_lbl1.place(x = 460, y = 0, width = 480, height = 135)
        
        #image3
        img2 = Image.open(r"C:\Users\Joe\Desktop\project_gallery\up.png")
        img2 = img2.resize((460, 135),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl2 = Label(self.root,image = self.photoimg2)
        f_lbl2.place(x = 940, y = 0, width = 460, height = 135)

        #backround
        img3 = Image.open(r"C:\Users\Joe\Desktop\project_gallery\fac4.gif")
        img3 = img3.resize((1370, 655),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root,image = self.photoimg3)
        bg_img.place(x = 0, y = 135, width = 1370, height = 655) 
        
        title_lbl=Label(bg_img, text = "UDATE EPLOYEE INFO", font = ("Algerian", 29,'bold'), bg = "dark blue", fg = "white")
        title_lbl.place(x = 0, y = 5, width = 1370, height = 35 )

        m_frame = Frame(bg_img, bd = 2)
        m_frame.place(x = 20, y = 48, width = 1320, height = 550)

        #side_img1
        imag1 = Image.open(r"C:\Users\Joe\Desktop\project_gallery\sideimg1.jpg")
        imag1 = imag1.resize((255, 320), Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(imag1)
        pht_lbl1 = Label(root, image = self.photo1)
        pht_lbl1.place(x = 60, y = 368, width = 255, height = 320)

        # side_img2
        imag2 = Image.open(r"C:\Users\Joe\Desktop\project_gallery\sideimg2.jpg")
        imag2 = imag2.resize((255, 260), Image.ANTIALIAS)
        self.photo2 = ImageTk.PhotoImage(imag2)
        pht_lbl2 = Label(root, image=self.photo2)
        pht_lbl2.place(x=1045, y = 410, width=255, height = 260)
        
        l_frame = LabelFrame(m_frame, bd = 10, relief = RIDGE, text = "DETAILS OF EMPLOYEE SEARCHED:", font = ('Algerian', 18, "bold", "italic", "underline") )
        l_frame.place(x = 15, y = 15, width= 1280, height = 528)

        # Frame_bg
        fram_bg = Image.open(r"C:\Users\Joe\Desktop\project_gallery\facda.jpg")
        fram_bg = fram_bg.resize((1258, 518), Image.ANTIALIAS)
        self.pic = ImageTk.PhotoImage(fram_bg)
        bgimg_lbl = Label(l_frame, image=self.pic)
        bgimg_lbl.place(x=0, y=0)
        #to display old records
        def searching():
            q="select * from employee_details where employee_code='{}'".format(srch_entry.get())
            mycursor.execute(q)
            r=mycursor.fetchall()
            
            code_opts.delete(0, END)
            code_opts.insert(0,r[0][0])
            nam_opts.delete(0,END)
            nam_opts.insert(0,r[0][1])
            gen_opts.current(gen_opts["values"].index(r[0][2]))
            dep_opts.current(dep_opts["values"].index(r[0][3]))
            post_opts.current(post_opts["values"].index(r[0][4]))
            sal_opts.current(sal_opts["values"].index(r[0][5]))
            pho_opts.delete(0, END)                       
            pho_opts.insert(0,r[0][6])
            em_opts.delete(0,END)
            em_opts.insert(0,r[0][7])
            qual_opts.delete(0,END)
            qual_opts.insert(0,r[0][8])
            ach_opts.current(ach_opts["values"].index(r[0][9]))
            ex_opts.current(ex_opts["values"].index(r[0][10]))
            rat_opts.current(rat_opts["values"].index(r[0][11]))
                         
              
        #search_frame
        srch_frame = LabelFrame(l_frame, bg = "silver", relief = RIDGE, text = "SEARCH FOR AN EMPLOYEE HERE:", font = ('Algerian', 14, "italic", "underline"))
        srch_frame.place(x = 130, y = 20, width = 1000, height = 100)
        srch_header = Label(srch_frame, bg = "silver", text = "Search by employee code:", font = ('Times New Roman', 18, "bold"), fg = "dark blue")
        srch_header.grid( row = 0, column = 0, padx = 60, pady = 20)
        srch_entry = ttk.Entry(srch_frame, width = 50, font = ("times new roman", 10))
        srch_entry.grid(row = 0, column = 1, padx = 0)
        search_btn = Button(srch_frame,command=searching, bg = "blue", height = 1, width = 14, text = "Search", font = ("Times New Roman", 12, "bold"), fg = "white")
        search_btn.grid(row = 0, column = 2, padx = 45)

        inner_frame1 = LabelFrame(l_frame, bd = 3, bg= "silver", relief = RIDGE, text = "CURRENT STATUS", font = ('Algerian', 12, "bold", "italic", "underline") )
        inner_frame1.place(x = 280, y = 140, width = 700, height = 80)

        #Department
        dprtmnt_lbl = Label(inner_frame1, text = "Department", font = ("Ariel", 11, "bold"), bg = "silver", fg = "dark blue" )
        dprtmnt_lbl.grid(row = 0, column = 0, padx = 20, pady= 2)
        dep_opts = ttk.Combobox(inner_frame1, font = ("times new roman", 10), state = "readonly")
        dep_opts["values"] = ("Select department", "Sales", "IT", "Finance", "Marketing","HR","Tech Support")
        dep_opts.current(0)
        dep_opts.grid(row = 0, column = 1, padx = 3)

        #Post held
        post_lbl = Label(inner_frame1, text = "Post held", font = ("Ariel", 11, "bold"), bg = "silver", fg = "dark blue" )
        post_lbl.grid(row = 1, column = 0, padx = 3, pady= 2)
        post_opts = ttk.Combobox(inner_frame1, font = ("times new roman", 10), state = "readonly")
        post_opts["values"] = ("Select post", "Software Manager", "Software Developer", "Intern", "Project Manager","Team Lead","VP","CIO","CTO","CEO")
        post_opts.current(0)
        post_opts.grid(row = 1, column = 1, padx = 3)

        #Employee code
        code_lbl = Label(inner_frame1, text = "Emplyee code", font = ("Ariel", 11, "bold"), bg = "silver", fg = "dark blue" )
        code_lbl.grid(row = 0, column = 2, padx = 40, pady= 2)
        code_opts = ttk.Entry(inner_frame1, font = ("times new roman", 10))
        code_opts.grid(row = 0, column = 3, padx = 2)

        #Sallery
        sal_lbl = Label(inner_frame1, text = "Salary", font = ("Ariel", 11, "bold"), bg = "silver", fg = "dark blue" )
        sal_lbl.grid(row = 1, column = 2, padx = 19, pady= 2)
        sal_opts = ttk.Combobox(inner_frame1, font = ("times new roman", 10), state = "readonly")
        sal_opts["values"] = ("Select salary", "100,000","200,000","250,000","300,000", "400,000")
        sal_opts.current(0)
        sal_opts.grid(row = 1, column = 3, padx = 3)

        
        inner_frame2 = LabelFrame(l_frame, bd = 3, bg = "silver", relief = RIDGE, text = "PERSONAL DETAILS", font = ('Algerian', 12, "bold", "italic", "underline") )
        inner_frame2.place(x = 280, y = 230, width = 700, height = 260)

        #Name
        nam_lbl = Label(inner_frame2, text = "Name", font = ("Ariel", 11, "bold"), bg = "silver", fg = "dark blue" )
        nam_lbl.grid(row = 0, column = 0, padx = 10, pady = 10)
        nam_opts = ttk.Entry(inner_frame2, font = ("times new roman", 10))
        nam_opts.grid(row = 0, column = 1, padx = 3)

        #Gender
        gen_lbl = Label(inner_frame2, text = "Gender", font = ("Ariel", 11, "bold"), bg = "silver", fg = "dark blue" )
        gen_lbl.grid(row = 1, column = 0, padx = 10, pady= 3)
        gen_opts = ttk.Combobox(inner_frame2, font = ("times new roman", 10), state = "readonly")
        gen_opts["values"] =("Select gender", "Male", "Female","Transgender","Gender neutral")
        gen_opts.current(0)
        gen_opts.grid(row = 1, column = 1, padx = 3)

        #Phone
        pho_lbl = Label(inner_frame2, text = "Phone", font = ("Ariel", 11, "bold"), bg = "silver", fg = "dark blue" )
        pho_lbl.grid(row = 2, column = 0, padx = 10, pady= 3)
        pho_opts = ttk.Entry(inner_frame2, font = ("times new roman", 10))
        pho_opts.grid(row = 2, column = 1, padx = 3)

        #E-mail
        em_lbl = Label(inner_frame2, text = "E-mail", font = ("Ariel", 11, "bold"), bg = "silver", fg = "dark blue" )
        em_lbl.grid(row = 3, column = 0, padx = 10, pady= 3)
        em_opts = ttk.Entry(inner_frame2, font = ("times new roman", 10))
        em_opts.grid(row = 3, column = 1, padx = 3)

        #Qualifications
        qual_lbl = Label(inner_frame2, text = "Qualifications", font = ("Ariel", 11, "bold"), bg = "silver", fg = "dark blue" )
        qual_lbl.grid(row = 0, column = 2, padx = 70, pady= 3)
        qual_opts = ttk.Entry(inner_frame2, font = ("times new roman", 10))
        qual_opts.grid(row = 0, column = 3, padx = 3)

        #Achievements
        ach_lbl = Label(inner_frame2, text = "Achievements", font = ("Ariel", 11, "bold"), bg = "silver", fg = "dark blue" )
        ach_lbl.grid(row = 1, column = 2, padx = 10, pady= 3)
        ach_opts = ttk.Combobox(inner_frame2, font = ("times new roman", 10), state = "readonly")
        ach_opts["values"] = ("Select achivements", "Employee of the year award", "Management skills award", "Exeptional thinker award", "Award for punctuality")
        ach_opts.current(0)
        ach_opts.grid(row = 1, column = 3, padx = 0)

        #Experience
        ex_lbl = Label(inner_frame2, text = "Experience", font = ("Ariel", 11, "bold"), bg = "silver", fg = "dark blue" )
        ex_lbl.grid(row = 2, column = 2, padx = 10, pady= 3)
        ex_opts = ttk.Combobox(inner_frame2, font = ("times new roman", 10), state = "readonly")
        ex_opts["values"] = ("Select a year", "Less than a yr", "1 year", "2 years", "3 years", "4 years", "5 years", "More than 5 years")
        ex_opts.current(0)
        ex_opts.grid(row = 2, column = 3, padx = 0)

        #Ratings
        rat_lbl = Label(inner_frame2, text = "Ratings", font = ("Ariel", 11, "bold"), bg = "silver", fg = "dark blue" )
        rat_lbl.grid(row = 3, column = 2, padx = 10, pady= 3)
        rat_opts = ttk.Combobox(inner_frame2, font = ("times new roman", 10), state = "readonly")
        rat_opts["values"] = ("select ratings", "1 star", "2 star", "3 star", "4 star", "5 star")
        rat_opts.current(0)
        rat_opts.grid(row = 3, column = 3, padx = 0)

        inner_frame3 = LabelFrame(l_frame, bd = 3, bg = "silver", relief = RIDGE, font = ('Algerian', 12, "bold", "italic", "underline") )
        inner_frame3.place(x = 330, y = 410, width = 600, height = 80)
        #to make changes
        def sv():
            q=" update employee_details set  employee_code='{}',employee_name='{}',gender='{}',department='{}', post_held='{}',salary='{}',phone='{}', e_mail='{}',qualification='{}', achievements='{}',experience='{}',ratings='{}' where  employee_code='{}';".format(code_opts.get(),nam_opts.get(),gen_opts.get(),dep_opts.get(),post_opts.get(),sal_opts.get(),pho_opts.get(),em_opts.get(),qual_opts.get(),ach_opts.get(),ex_opts.get(),rat_opts.get(),code_opts.get())
            mycursor.execute(q)
            mycon.commit()
        def dsv():
            subroot=Tk()
            subroot.geometry("500x100")
            ler=Label(subroot,bg="black",text = "Successfully Updated", font = ("Algerian", 24,'bold'),fg="white")
            ler.pack(fil = BOTH,expand=True)
            root.destroy()
            
        #Change_button
        change_btn = Button(inner_frame3,command=sv, bg = "green", height = 2, width = 10, text = "Make changes", cursor = "hand2", font = ("Times New Roman", 15, "bold"), fg = "black")
        change_btn.grid(row = 2, column = 0, padx = 29, pady = 6)

        #Save_button
        save_btn = Button(inner_frame3,command=dsv, bg = "yellow", height = 2, width = 10, text = "Save", cursor = "hand2", font = ("Times New Roman", 15, "bold"), fg = "black")
        save_btn.grid(row = 2, column = 1, padx = 245, pady = 0)
        
        
       
if __name__ == "__main__":
    root = Tk()
    obj = Update_id(root)
    root.mainloop()
