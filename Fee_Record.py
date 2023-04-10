from tkinter import *
from tkinter.simpledialog import askinteger
from tkinter import ttk
from tkinter.ttk import Treeview
from PIL import Image,ImageTk
from tkinter.ttk import Combobox
import sqlite3
from tkinter import messagebox
import random
global pho
idl=0
root=Tk()
root.state("zoomed")
root.resizable(width=False,height=False)
root.title("Record Book")
root.iconbitmap("images\icon.ico")

# background image--------
img=Image.open("images\gm.jfif").resize((1363,740))
img2=ImageTk.PhotoImage(img)
can=Canvas(root)
can.create_image(0,0, image=img2,anchor=NW)
can.pack(fill=BOTH,expand=True)
can.create_text(650,30,text="Made By Harsh",fill="Black",font=("Times",28,"bold"))



#SQl----------------
mydb=sqlite3.connect(database="new.txt")
y=sqlite3.Cursor(mydb)
y.execute('create table if not exists person(id int,name varchar(200),adress varchar(300),pho varchar(12),email varchar  (255),fees int,course varchar (255),sbfees int ,user varchar(255),pass varchar(255),idl int(20), PRIMARY KEY(id))')
#Insert main query--------------
def insert_fs(ids,name,adress,pho,mail,feess,corss):
    y.execute("insert into person(id,name,adress,pho,email,fees,course) values({},'{}','{}','{}','{}',{},'{}')".format(ids,name,adress,pho,mail,feess,corss))
    mydb.commit()
y.execute("select Max(id) from person where user='admin' and pass='admin'")
for x in y:
    try:
        if(x[-1]==None and idl==0):
                idl=1
                y.execute("insert into person (id,user,pass) values({},'admin','admin')".format(idl))
                mydb.commit()
    except:pass
# logout function----------------------
def lgout():
    main()
    root.after(10,lambda: adusbtn.destroy())
    root.after(10,lambda: show_fees.destroy())
    root.after(10,lambda: sr_btn.destroy())
    root.after(10,lambda: show_rec.destroy())
    root.after(10,lambda: add_acc.destroy())

def main():
    root.after(10,lambda: adusbtn.destroy())
    root.after(10,lambda: show_fees.destroy())
    root.after(10,lambda: sr_btn.destroy())
    root.after(10,lambda: show_rec.destroy())
    root.after(10,lambda: add_acc.destroy())
    login_fr=Frame(root,bg="#d3d3d3",highlightthickness=5,highlightbackground="black",)
    login_fr.place(relx=.2,rely=.25,width=815,height=435)
    brd=Frame(login_fr,bg="Powder blue")
    brd.place(x=0,y=0,height=60,relwidth=1)
    login_lbl=Label(brd,text="Login",bg="powder blue",font=("",20,"bold"),bd=1,relief=SUNKEN,padx=10)
    login_lbl.pack(pady=10)
    lg_btn=Label(login_fr,text="Username",bg="powder blue",font=("",20,"bold"),bd=1,relief=SUNKEN,padx=10)
    lg_btn.place(x=100,y=100)
    lg_btn=Label(login_fr,text="Password",bg="powder blue",font=("",20,"bold"),bd=1,relief=SUNKEN,padx=12)
    lg_btn.place(x=100,y=200)
    log_val=Entry(login_fr,font=("",20))
    log_val.focus()
    log_val.place(x=290,y=100)
    pas_val=Entry(login_fr,font=("",20),show="*")
    pas_val.place(x=290,y=200)
    def login():
        global pho
        global idl
        lgvl=log_val.get()
        psvl=pas_val.get()
        user="no"
        pas="no"
        y.execute("select user from person where user='{}'".format(lgvl))
        for x in y:
            user="found"
        y.execute("select pass from person where user='{}'".format(lgvl))
        for x in y:
            print(x)
            if(x[0]==psvl):
                pas="mil gaya"
        if(lgvl=="admin" and psvl=="admin" and idl==1 and user=="found"):
            y.execute("update person set pass='7qw1v98r3ad9',user='7s1a3w9l;a.,' where user='admin'")
            print("cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc")
            mydb.commit()
            idl=2
            global newlogin_fr
            newlogin_fr=Frame(root,bg="#4ee6bd",highlightthickness=5,highlightbackground="black",)
            newlogin_fr.place(relx=.2,rely=.25,width=815,height=435)
            brd=Frame(newlogin_fr,bg="#c76060")
            brd.place(x=0,y=0,height=60,relwidth=1)
            login_lbl=Label(brd,text="Create user",bg="#c76060",font=("",20,"bold"),bd=1,relief=SUNKEN,padx=10)
            login_lbl.pack(pady=10)
            lg_btn=Label(newlogin_fr,text="Username",bg="powder blue",font=("",20,"bold"),bd=1,relief=SUNKEN,padx=10)
            lg_btn.place(x=100,y=100)
            lg_btn=Label(newlogin_fr,text="Password",bg="powder blue",font=("",20,"bold"),bd=1,relief=SUNKEN,padx=12)
            lg_btn.place(x=100,y=200)
            newlog_val=Entry(newlogin_fr,font=("",20))
            newlog_val.focus()
            newlog_val.place(x=290,y=100)
            newpas_val=Entry(newlogin_fr,font=("",20),show="*")
            newpas_val.place(x=290,y=200)
            def new_user():
                nuv=newlog_val.get()
                npv=newpas_val.get()
                if(nuv!="" and npv!=""):
                    y.execute("insert into person (user,pass) values('{}','{}')".format(nuv,npv))
                    mydb.commit()
                    messagebox.showinfo("Success","New User Created")   
                    main()
                else:
                    messagebox.showerror("Error","Invalid Username or Password")   
            ctus_btn=Button(newlogin_fr,text="Create User",font=("",15,"bold"),activebackground="powder blue",command=new_user,padx=8)
            ctus_btn.place(x=370,y=350)
            messagebox.showinfo("Success","You Logged In as default user.\nCreate New User to continue ")   
        elif(user=="found" and pas=="mil gaya"):
            root.after(100,lambda: login_fr.destroy())
            root.after(100,lambda: newlogin_fr.destroy())
#add user------------
            def adus():
                global pho
                global user_add
                user_add=Frame(root,bg="#fffdd0",highlightthickness=5,highlightbackground="black",)
                user_add.place(relx=.2,rely=.25,width=815,height=435)
                #add user bg--------------
                
                imgs=Image.open("images\dduser.jpg").resize((815,435))
                img_fr=ImageTk.PhotoImage(imgs)
                imgs2=Label(user_add,image=img_fr)
                imgs2.photo=img_fr
                imgs2.place(x=-10,y=-10)
            # labels-----------------
                name=Label(user_add,text="Name",font=("",15,"bold"),bg='white')
                name.place(relx=0.07,rely=.09)
                add=Label(user_add,text="Address",font=("",15,"bold"),bg="white",border=1,relief=SUNKEN)
                add.place(relx=0.07,rely=0.18)
                ph=Label(user_add,text="Ph. Number",font=("",15,"bold"),bg="white",border=1,relief=SUNKEN)
                ph.place(relx=0.07,rely=0.27)
                mail=Label(user_add,text="E-mail",font=("",15,"bold"),bg="white",border=1,relief=SUNKEN,)
                mail.place(relx=0.07,rely=0.36)
                fees=Label(user_add,text="Fees",font=("",15,"bold"),bg="white",border=1,relief=SUNKEN,)
                fees.place(relx=0.07,rely=0.45)
                cors=Label(user_add,text="Course",font=("",15,"bold"),bg="white",border=1,relief=SUNKEN,)
                cors.place(relx=0.07,rely=0.54)

                #Entry Box
                nameval=Entry(user_add,bg="pink",font=("",15))
                nameval.place(relx =0.3,rely=0.09, anchor = NW)
                nameval.focus()
                addval=Entry(user_add,bg="pink",font=("",15))
                addval.place(relx=0.3,rely=0.18,anchor=NW)
                phval=Entry(user_add,bg="pink",font=("",15))
                phval.place(relx=0.3,rely=0.27,)
                mailval=Entry(user_add,bg="pink",font=("",15))
                mailval.place(relx=0.3,rely=0.36)
                fesval=Entry(user_add,bg="pink",font=("",15))
                fesval.place(relx=0.3,rely=0.45)
                corsval=Entry(user_add,bg="pink",font=("",15))
                corsval.place(relx=0.3,rely=0.54)
                #functions
                global rst
                def rst():
                    nameval.delete(0,'end')
                    corsval.delete(0,'end')
                    fesval.delete(0,'end')
                    addval.delete(0,'end')
                    mailval.delete(0,'end')
                    phval.delete(0,'end')
                def ent():
                    me="pata ni"
                    ids=random.randint(100000,999999)
                    global pho
                    names=nameval.get() 
                    pho=phval.get()
                    adress=addval.get()
                    ml=mailval.get()
                    feess=fesval.get()
                    corss=corsval.get()
                    name=names.capitalize()
                    fst=0
                    pck="9876"
                    try:
                        fst=pho[0]
                        intph=int(pho)
                    except:pass
                    try:
                        if(fst in pck):
                            me="sahi"
                        else:
                            me="galat"
                    except:pass
                    phon=len(pho)
                    mail=ml[-10:]
                    count=ml.count("@")
                    ck=["!","#","$","%","^","&","*","(",")","_","-","=","=",";",":","<",">","?"]
                    for x in ck:
                        true="not gotcha"
                        if(x in ml or " " in ml or count>1):
                            true="gotcha"
                            break
                    if(mail!='@gmail.com' and mail!=" " or true=="gotcha"):
                        mailval.delete(0,'end')  
                        inmail=Label(user_add,text="Invalid Email",font=('',15,"bold"),fg="red")
                        inmail.place(relx=0.65,rely=0.44)
                        user_add.after(1000,lambda: inmail.destroy()) 
                    if(phon<=9 or phon>=12 or phon==11 or type(intph)==str or me=="galat"):
                        phval.delete(0,'end')
                        inpho=Label(user_add,text="Invalid Phone",font=('',15,"bold"),fg="red")
                        inpho.place(relx=0.65,rely=0.36)
                        user_add.after(1000,lambda: inpho.destroy())
                    if(name=="" or adress== ""):
                        messagebox.showerror("Error","Name and Adress are mandatory")
                    if(mail=='@gmail.com' and type(intph)==int and phon>=10 and phon<=12 and phon!=11 and me=="sahi" and name!="" and adress!=""):
                        y.execute("select Max(id) from person where pho={}".format(pho))
                        for id in y:
                            if(id[-1]==None):
                                    pho=str(pho)
                                    insert_fs(ids,name,adress,pho,ml,feess,corss)
                                    rst()  
                                    messagebox.showinfo('Succes',"Data Saved Successfully with Unique Id :-{}".format(ids))       
                            else:
                                messagebox.showinfo("Caution","User Already Exists")  
                sbt=Button(user_add,text="SUBMIT",font=("",15,"bold"),bg="white",command=ent)
                sbt.place(relx=0.30,rely=0.75)
                sbt=Button(user_add,text="RESET",font=("",15,"bold"),bg="white",command=rst)
                sbt.place(relx=0.50,rely=0.75)
#Search User-------------------------
            def srch():
                srchfr=Frame(root,bg="#fffdd0")
                srchfr.place(relx=.2,rely=.25,width=815,height=435)
                img=Image.open("images\srch.jpg").resize((815,435))
                img2=ImageTk.PhotoImage(img)
                img3=Label(srchfr,image=img2)
                img3.photo=img2
                img3.place(x=0,y=0)
                srch_by=Label(srchfr,text="SEARCH BY",font=("",20,"bold"),bg="#fffdd0")
                srch_by.place(x=100,y=70)
                ddl=Combobox(srchfr,font=("",20,'bold'),state="readonly",values=['Select','Name','Phone Number','ID'])
                ddl.current(0)
                ddl.place(x=400,y=70)
                def idlbl():
                    global id_lbl
                    id_lbl=Label(srchfr,text="Enter ID",font=("",20,"bold"),bg="#fffdd0")
                def nmlbl():
                    global name
                    name=Label(srchfr,text="Enter Name",font=("",20,"bold"),bg="#fffdd0")
                def phlbl():
                    global ph
                    ph=Label(srchfr,text="Enter Ph Number",font=("",20,"bold"),bg="#fffdd0")        
                def val(k):
                    ddl_entry=Entry(srchfr,font=("",20,"bold"),bd=3)
                    ddl_entry.place(x=400,y=150)
                    ddl_entry.focus()
                    def find():
                        check=ddl_entry.get()
                        if(value=="Name"):
                            check=check.capitalize()
                            y.execute("select Max(id) from person where name='%s'"%(check))
                            for x in y:
                                x=x[-1]
                        elif(value=="Phone Number"):
                            y.execute("select Max(id) from person where pho={}".format(check))
                            for x in y:
                                x=x[-1]  
                        elif(value=="ID"):
                            y.execute("select Max(id) from person where id={}".format(check))
                            for x in y:
                                x=x[-1]              
                        if(x!=None):
                            otfr=Frame(root)
                            otfr.place(relx=.2,rely=.25,width=815,height=435)
                            tb=ttk.Treeview(otfr,selectmode="none",height=21)
                            ttk.Style().theme_use("clam")
                            tb.pack(anchor=W,fill=BOTH)
                            tb['columns']=("0","1","2","3","4")
                            tb['show'] = 'headings'
                            tb.column("0", width = 80, anchor ='c')
                            tb.column("1", width = 180, anchor =W)
                            tb.column("2", width = 225, anchor ='c')
                            tb.column("3", width = 120, anchor ='c')
                            tb.column("4", width = 210, anchor ='c')
                            tb.heading("0", text ="ID")
                            tb.heading("1", text ="Name")
                            tb.heading("2", text ="Address")
                            tb.heading("3", text ="Phone")  
                            tb.heading("4", text ="E-Mail")
                            if(value=="Name"):
                                y.execute('select * from person where id={}'.format(x))
                                r_set=y.execute('SELECT * from person where id={}'.format(x))
                                y.execute("select * from person where name='%s'"%(check))
                                for dt in r_set: 
                                    tb.insert("", 'end',iid=dt[0], text=dt[0],values =(dt[0],dt[1],dt[2],dt[3],dt[4]))
                                    tb.pack(anchor=W,fill=Y)
                            else:
                                y.execute('select * from person where id={}'.format(x))
                                r_set=y.execute('SELECT * from person where id={}'.format(x))
                                for dt in r_set: 
                                    tb.insert("", 'end',iid=dt[0], text=dt[0],values =(dt[0],dt[1],dt[2],dt[3],dt[4]))
                                    tb.pack(anchor=W,fill=Y)
                            def dest():
                                otfr.destroy()
                            bck_btn=Button(otfr,text="Back",font=("",11,"bold"),bg="white",command=dest)
                            bck_btn.place(relx=.9,rely=.9)
                        elif(x==None):
                            messagebox.showerror("Error","No Record Found")
                    srchbtn=Button(srchfr,text="SEARCH",font=("",15,"bold"),bg="white",padx=5,command=find)
                    srchbtn.place(x=350,y=300) 
                    global value
                    value=ddl.get()
                    if(value=='Name'):
                        nmlbl()
                        ddl_entry.focus()
                        name.place(x=100,y=150)
                        srchfr.after(10,lambda: id_lbl.destroy())
                        srchfr.after(10,lambda: ph.destroy())
                    elif(value=='Phone Number'):
                        phlbl()
                        ddl_entry.focus()
                        ph.place(x=100,y=150)
                        srchfr.after(10,lambda: id_lbl.destroy())
                        srchfr.after(10,lambda: name.destroy())
                    elif(value=='ID'):
                        idlbl()
                        ddl_entry.focus()
                        id_lbl.place(x=100,y=150)
                        srchfr.after(10,lambda: ph.destroy())
                        srchfr.after(10,lambda: name.destroy())
                ddl.bind("<<ComboboxSelected>>",val)
#Show records-------------
            def show():
                show_fr=Frame(root,bg="#fffdd0")
                show_fr.place(relx=.2,rely=.25,width=815,height=435)
                h=Scrollbar(show_fr)
                h.pack(side=RIGHT,fill=Y)
                tb=ttk.Treeview(show_fr,height=18,yscrollcommand=h.set)
                h.config( command =tb.yview )
                ttk.Style().theme_use("clam")
                style=ttk.Style(root)
                style.configure("Treeview", background="pink",fieldbackground="pink", foreground="black")
                tb.pack(anchor=W,fill=Y)
                tb['columns']=("0","1","2","3","4")
                tb['show'] = 'headings'
                tb.column("0", width = 80, anchor ='c')
                tb.column("1", width = 180, anchor =W)
                tb.column("2", width = 205, anchor ='c')
                tb.column("3", width = 120, anchor ='c')
                tb.column("4", width = 210, anchor ='c')
                tb.heading("0", text ="ID")
                tb.heading("1", text ="Name")
                tb.heading("2", text ="Address")
                tb.heading("3", text ="Phone")  
                tb.heading("4", text ="E-Mail")
                r_set=y.execute('''SELECT * from person where id!=1''')
                for dt in r_set: 
                    tb.insert("", 'end',iid=dt[0], text=dt[0],values =(dt[0],dt[1],dt[2],dt[3],dt[4]))
                def del_rec():
                    item=tb.selection()[0]
                    y.execute("delete from person where id={}".format(item))
                    mydb.commit()
                    messagebox.showinfo("Succes","Record Deleted Successfully")
                    show()
                def upd_rec():
                    item=tb.selection()[0]
                    global user_add
                    user_add=Frame(root,bg="#fffdd0",highlightthickness=5,highlightbackground="black",)
                    user_add.place(relx=.2,rely=.25,width=815,height=435)
                    #add user bg--------------  
                    imgs=Image.open("images\dduser.jpg").resize((815,435))
                    img_fr=ImageTk.PhotoImage(imgs)
                    imgs2=Label(user_add,image=img_fr)
                    imgs2.photo=img_fr
                    imgs2.place(x=-10,y=-10)
                # labels-----------------
                    name=Label(user_add,text="Name",font=("",15,"bold"),bg='white')
                    name.place(relx=0.07,rely=.18)
                    add=Label(user_add,text="Address",font=("",15,"bold"),bg="white",border=1,relief=SUNKEN)
                    add.place(relx=0.07,rely=0.27)
                    ph=Label(user_add,text="Ph. Number",font=("",15,"bold"),bg="white",border=1,relief=SUNKEN)
                    ph.place(relx=0.07,rely=0.36)
                    mail=Label(user_add,text="E-mail",font=("",15,"bold"),bg="white",border=1,relief=SUNKEN,)
                    mail.place(relx=0.07,rely=0.45)
                #Entry Box---------------
                    y.execute("select * from person where id={}".format(item))
                    for x in y:
                        nameval=Entry(user_add,text="hi",bg="pink",font=("",15))
                        nameval.delete(0,'end')
                        nameval.insert(0,'{}'.format(x[1]))
                        nameval.place(relx =0.3,rely=0.18, anchor = NW)
                        nameval.focus()
                        addval=Entry(user_add,bg="pink",font=("",15))
                        addval.insert(0,'{}'.format(x[2]))
                        addval.place(relx=0.3,rely=0.27,anchor=NW)
                        phval=Entry(user_add,bg="pink",font=("",15))
                        phval.insert(0,'{}'.format(x[3]))
                        phval.place(relx=0.3,rely=0.36,)
                        mailval=Entry(user_add,bg="pink",font=("",15))
                        mailval.insert(0,'{}'.format(x[4]))
                        mailval.place(relx=0.3,rely=0.45)
                        def upd_dt():
                            names=nameval.get() 
                            name=names.capitalize()
                            global pho
                            fst=3
                            pck="9876"
                            pho=phval.get()
                            try:
                                fst=pho[0]
                                intph=int(pho)
                                if(fst in pck):
                                    me="sahi"
                                else:
                                    me="galat"
                            except:pass
                            phon=len(pho)
                            adress=addval.get()
                            ml=mailval.get()
                            mail=ml[-10:]
                            count=ml.count("@")
                            ck=["!","#","$","%","^","&","*","(",")","_","-","=","=",";",":","<",">","?"]
                            for x in ck:
                                true="not gotcha"
                                if(x in ml or " " in ml or count>1):
                                    true="gotcha"
                            if(mail!='@gmail.com' and mail!="" or true=="gotcha"):
                                mailval.delete(0,'end')  
                                inmail=Label(user_add,text="Invalid Email",font=('',15,"bold"),fg="red")
                                inmail.place(relx=0.65,rely=0.44)
                                user_add.after(1000,lambda: inmail.destroy()) 
                            if(phon<=9 or phon>=12 or phon==11 or type(intph)==str or me=="galat" or ph==""):
                                phval.delete(0,'end')
                                inpho=Label(user_add,text="Invalid Phone",font=('',15,"bold"),fg="red")
                                inpho.place(relx=0.65,rely=0.36)
                                user_add.after(1000,lambda: inpho.destroy())
                            if(mail=='@gmail.com' and type(intph)==int and phon>=10 and phon<=12 and phon!=11 and me=="sahi" and true=="not gotcha"):
                                                pho=str(pho)
                                                y.execute("update person set name='{}',adress='{}',pho='{}',email='{}' where id={}".format(name,adress,pho,ml,item))
                                                mydb.commit()
                                                nameval.delete(0,'end')
                                                addval.delete(0,'end')
                                                mailval.delete(0,'end')
                                                phval.delete(0,'end')
                                                messagebox.showinfo('Succes',"Data Updated Successfully")
                                                show()
                    update=Button(user_add,text="UPDATE",font=("",12,"bold"),command=upd_dt)
                    update.place(relx=.3,rely=.54)
                delete=Button(show_fr,text="DELETE",font=("",12,"bold"), command=del_rec)
                delete.place(x=300,y=390)
                update=Button(show_fr,text="UPDATE",font=("",12,"bold"),command=upd_rec)
                update.place(x=400,y=390)
# add new user-----------------------
            def useracc_add():
                login_fr=Frame(root,bg="#d3d3d3",highlightthickness=5,highlightbackground="black",)
                login_fr.place(relx=.2,rely=.25,width=815,height=435)
                brd=Frame(login_fr,bg="Powder blue")
                brd.place(x=0,y=0,height=60,relwidth=1)
                login_lbl=Label(brd,text="Create New User",bg="powder blue",font=("",20,"bold"),bd=1,relief=SUNKEN,padx=10)
                login_lbl.pack(pady=10)
                lg_btn=Label(login_fr,text="Username",bg="powder blue",font=("",20,"bold"),bd=1,relief=SUNKEN,padx=10)
                lg_btn.place(x=100,y=100)
                lg_btn=Label(login_fr,text="Password",bg="powder blue",font=("",20,"bold"),bd=1,relief=SUNKEN,padx=12)
                lg_btn.place(x=100,y=180)
                lg_btn=Label(login_fr,text="Confirm Password",bg="powder blue",font=("",20,"bold"),bd=1,relief=SUNKEN,padx=12)
                lg_btn.place(x=100,y=260)
                log_val=Entry(login_fr,font=("",20))
                log_val.focus()
                log_val.place(x=390,y=100)
                pas_val=Entry(login_fr,font=("",20),show="*")
                pas_val.place(x=390,y=180)
                conpas_val=Entry(login_fr,font=("",20),show="*")
                conpas_val.place(x=390,y=260)
                def new():
                    nuv=log_val.get()
                    npv=pas_val.get()
                    cnpv=conpas_val.get()
                    if(nuv!="" and npv!="" and npv==cnpv):
                        y.execute("insert into person (user,pass) values('{}','{}')".format(nuv,npv))
                        mydb.commit()
                        main()
                        messagebox.showinfo("Success","New User Added")   
                    else:
                        if(npv=="" or nuv=="" or cnpv==""):
                            messagebox.showerror("Error","Entry Box can not be empty")
                        else:
                            messagebox.showerror("Error","Password Mismatch")
                ctus_btn=Button(login_fr,text="Add New User",font=("",15,"bold"),activebackground="powder blue",command=new,padx=8)
                ctus_btn.place(x=370,y=350)
#fee record-------------------------------------

            def feerec():
                fee_fr=Frame(root,bg="#d3d3d3")
                fee_fr.place(relx=.2,rely=.25,width=815,height=435)
                h=Scrollbar(fee_fr)
                h.pack(side=RIGHT,fill=Y)
                tb=ttk.Treeview(fee_fr,height=18,yscrollcommand=h.set)
                h.config( command =tb.yview )
                ttk.Style().theme_use("clam")
                style=ttk.Style(root)
                style.configure("Treeview", background="powder blue",fieldbackground="powder blue", foreground="black")
                tb.pack(anchor=W,fill=Y)
                tb['columns']=("5","0","1","2","3","4")
                tb['show'] = 'headings'
                tb.column("0", width = 170, anchor =W)
                tb.column("2", width = 120, anchor =CENTER)
                tb.column("1", width = 163, anchor =CENTER)
                tb.column("3", width = 120, anchor =CENTER)
                tb.column("4", width = 120, anchor =CENTER)
                tb.column("5", width = 100, anchor =CENTER)
                tb.heading("0", text ="Name")
                tb.heading("1", text ="Course")
                tb.heading("2", text ="Total Fees")
                tb.heading("3", text ="Sumbitted Fees")  
                tb.heading("4", text ="Pending Fees")
                tb.heading("5", text ="ID")
                r_set=y.execute('''SELECT * from person where id!=1''')
                for dt in r_set:
                    x=int(dt[5])
                    if(dt[7]==None):
                        pfs=x
                    else:
                        xx=int(dt[7])
                        pfs=x-xx
                    tb.insert("", 'end',iid=dt[0], text=dt[0],values =(dt[0],dt[1],dt[6],dt[5],dt[7],pfs))
                def upd_fees():
                        item=tb.selection()[0]
                        fee=askinteger("Fees","Enter Fees\t\t\t\n\n")
                        if(fee>pfs):
                            messagebox.showerror("Error","Invalid Fee...")
                        else:
                            y.execute("select sbfees from person where id={}".format(item))
                            for x in y:
                                if(x[0]==None):
                                    y.execute("update person set sbfees={} where id={}".format(fee,item))
                                else:
                                    y.execute("update person set sbfees=sbfees+{} where id={}".format(fee,item))
                            mydb.commit()
                            feerec()
                            messagebox.showinfo("Success","Fee Submitted Successfully")
                updfs=Button(fee_fr,text="UPDATE",font=("",12,"bold"),command=upd_fees)
                updfs.place(x=360,y=390)
#main Buttons----------:-------------- 
            global adusbtn
            global sr_btn
            global show_rec
            global show_fees
            global add_acc
            adusbtn=Button(root,text="ADD STUDENT",font=("",12,"bold"),bg="#fedcba",command=adus)
            adusbtn.place(x=100,y=100)
            sr_btn=Button(root,text="SEARCH",font=("",12,"bold"),bg="#fedcba",command=srch)
            sr_btn.place(x=245,y=100)
            show_rec=Button(root,text="STUDENTS",font=("",12,"bold"),bg="#fedcba",command=show)
            show_rec.place(x=342,y=100)
            show_fees=Button(root,text="FEE RECORD",font=("",12,"bold"),bg="#fedcba",command=feerec)
            show_fees.place(x=460,y=100)
            add_acc=Button(root,text="ADD USER",font=("",12,"bold"),activebackground="powder blue",command=useracc_add,padx=8)
            add_acc.place(x=1140,y=100)
            logout_btn=Button(root,text="Log Out",font=("",15,"bold"),activebackground="powder blue",command=lgout,padx=8)
            logout_btn.place(x=1140,y=30)
            adus()
        else:
            if(id==1):
                messagebox.showerror("Error","Default User Changed")
            else:
                messagebox.showerror("Error","Invalid Username or Password")

    log_btn=Button(login_fr,text="Login",font=("",15,"bold"),activebackground="powder blue",command=login,padx=8)
    log_btn.place(x=370,y=350)
#main login button------------------- 
mnlog_btn=Button(root,text="Login",font=("",15,"bold"),activebackground="powder blue", command=main,padx=8)
mnlog_btn.place(x=90,y=30)

root.mainloop()

