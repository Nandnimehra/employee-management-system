from customtkinter import *
from PIL import Image
from tkinter import messagebox


def login():
    print('Nandini mehra')
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
    elif usernameEntry.get()=='Nandini' and passwordEntry.get()=='1234':
        messagebox.showinfo('Success','Login is successful')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error','wrong credentials')

root = CTk()
root.geometry('950x478')
root.resizable(0,0)
root.title('login page')
image = CTkImage(Image.open('img_2.png'),size=(930,478))
#size=(930,478)
imageLabel =CTkLabel(root,image=image)
imageLabel.place(x=0,y=0)
# headingLabel= CTkLabel(root,text ='Employee management system',bg_color='#FAFAFA',font=('Goudy Old Style',17,'bold'),text_color='dark blue')
# headingLabel.place(x=20,y=100)
headingLabel= CTkLabel(root,text ='  Employee management system  ',font=('Goudy Old Style',25,'bold'),text_color='white')
headingLabel.place(x=300,y=20)

usernameEntry=CTkEntry(root,placeholder_text='Enter your Username',width=180)
usernameEntry.place(x=50,y=150)

passwordEntry = CTkEntry(root,placeholder_text='Enter your Password',width=180,show='*')
passwordEntry.place(x=50,y=200)

loginButton=CTkButton(root,text='Login', cursor='hand2',command=login)
loginButton.place(x=70,y=250)

root.mainloop()

