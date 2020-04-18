# Author Rohit kumar
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import sqlite3
root=Tk()
root.geometry("860x450")
root.title('LoginSystem')
root.wm_iconbitmap("user.ico")
regf=Frame(root,background="white")
loginf=Frame(root,background="white")
home=Frame(root,background="white")

root.wm_attributes("-transparentcolor", 'grey')
regf.place(x=0,y=0,width=860,height=450)
loginf.place(x=0,y=0,width=800,height=450)
home.place(x=0,y=0,width=860,height=450)

def show(frame):
    frame.tkraise()
for frame in (regf,loginf,home):
    frame.place(x=0,y=0)
style = ttk.Style()
style.map("C.TButton",
    foreground=[('pressed', 'red'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'black'), ('active', 'white')]
    )
Estyle = ttk.Style() 
Estyle.configure('TEntry', foreground = 'green') 

#-----------------------------------------------------------------------
db = sqlite3.connect('signUP_Login.db')  
my=db.cursor()
#-----------------------------------------------------------------------
#####_______Form____####################################################
mylist=''
def register():
    try:
        num=0
        my=db.cursor()
        pop=my.execute("select*from hifi")
        for i in my:
            num=num+1
        num=num+1
        namer="'"+str(e1r.get())+"'"
        passwordr=str(e2r.get())
        my.execute(f"""Insert into hifi Values({num},{namer},{passwordr})""")
        db.commit()
        num=num+1
    except:
        namesr.delete(0,END)
        pwr.delete(0,END)

def login():
    m=Label(root, text="incorrect username or password",font=('Comic Sans MS',20),fg='red',bg="#060b4e")
    name=e1l.get()
    password=e2l.get()
    my=db.cursor()
    my.execute("select*from hifi")
    for i in my:
       if str(i[1])==name and str(i[2])==password:
          show(home)
          break       
    else:
        root.after(100, lambda:m.pack())
        root.after(1000, lambda:m.pack_forget()) 
        namesr.delete(0,END)
        pwr.delete(0,END)
#-----------------------SignUP-----------------------------------------
canvas=Canvas(regf,width=1200,height=1200)
canvas.place(x=-10,y=0)
profile1=PhotoImage(file='bg2.png')
canvas.create_image(0,0,anchor=NW,image=profile1)

##photo=PhotoImage(file='test.png')
##Label(main,image=photo,bg='grey').pack()

adr=Label(regf,text="SignUp Page",font=('Comic Sans MS', 35),fg='#d76737',bg="#060b4e")
adr.place(x=260,y=10)
l1r=Label(regf,text="username",font="vardana 20",fg='orange',bg='#060b4e')
l1r.place(x=240,y=100)
l2r=Label(regf,text="password",font="vardana 20",fg='orange',bg='#060b4e')
l2r.place(x=240,y=200)

e1r=StringVar()
namesr=ttk.Entry(regf,textvariable=e1r,font = ('courier', 22, 'bold'))
namesr.focus_force()
namesr.place(x=240,y=155)

e2r=StringVar()
pwr=ttk.Entry(regf,textvariable=e2r,show='*',font = ('courier', 22, 'bold'))
pwr.focus_force()
pwr.place(x=240,y=240)

submitr=ttk.Button(regf,text="sign up",width=20,command=register,style='C.TButton')
submitr.place(x=250,y=300)
logr=ttk.Button(regf,text="log in",width=20,command=lambda:show(loginf),style='C.TButton')
logr.place(x=450,y=300)
#-------------------------------------------------------------------------------------
#-----------------------login---------------------------------------------------------
canvas=Canvas(loginf,width=1200,height=1200)
canvas.place(x=-10,y=0)
profile=PhotoImage(file='bg1.png')
canvas.create_image(0,0,anchor=NW,image=profile)

adl=Label(loginf,text="Login page",bg='#060b4e',font=('Comic Sans MS', 35),fg='#d76737')
adl.place(x=290,y=10)
l1l=Label(loginf,text="username",font="vardana 20",fg='orange',bg='#060b4e')
l1l.place(x=240,y=100)
l2l=Label(loginf,text="password",font="vardana 20",fg='orange',bg='#060b4e')
l2l.place(x=240,y=200)
e1l=StringVar()
namesl=ttk.Entry(loginf,textvariable=e1l,font = ('courier', 22, 'bold'))
namesl.place(x=240,y=155)
e2l=StringVar()
pwl=ttk.Entry(loginf,textvariable=e2l,show='*',font = ('courier', 22, 'bold'))
pwl.place(x=240,y=240)
submitl=ttk.Button(loginf,text="sign up",width=20,command=lambda:show(regf),style='C.TButton')
submitl.place(x=250,y=300)
logl=ttk.Button(loginf,text="log in",width=20,command=login ,style='C.TButton')
logl.place(x=450,y=300)
#-------------------------------------------------------------------------------------

#----home-----------------------------------------------------------------------------
hm=Label(home,text="welcome To home Page",bg="white",font=('Comic Sans MS', 35),fg='#d76737')
hm.pack()
# write your code here to add widget to home page

#--------------------------------------------------------------------------------------

show(regf)
root.mainloop()
