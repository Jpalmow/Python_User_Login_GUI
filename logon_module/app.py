from tkinter import *


def main_menu():
    global main_window #applied global range for other functions
    main_window = Tk()
    main_window.geometry("300x300")
    main_window.title("login system")

    Label1 = Label(main_window, text="choose an option", bg="gray", fg="blue")
    Label1.pack(fill=X, pady=20)

    #button definition
    login_btn = Button(main_window, text="Log in", width="30", height="2")
    #button placement
    login_btn.pack(pady=20)

    register_btn = Button(main_window, text="Sign up", width="30", height="2"  command=new_user)
    register_btn.pack(pady=20)

    main_window.mainloop()
    
def new_user():
    
    new_user_window = Toplevel(main_window)
    new_user_window.title("Sign in as new user")
    new_user_window.geometry("300x250")
    
    username = StringVar()
    password = StringVar()
    fullname = StringVar()

    label2 = Label(new_user_window, text="Please fill below requirements", bg="gray", fg="blue")
    label2.pack(fill=X, pady=20)

    user_info_panel = Frame(new_user_window)
    user_info_panel.pack(pady=20)



    username_label = Label(user_info_panel, text="Username: ")
    username_label.grid(row=0, column=0)
    username_entry = Entry(user_info_panel, textvariable=username)
    username_entry.grid(row=0, column=1)

    Label(user_info_panel, text="").grid(row=1)



    password_label = Label(user_info_panel, text="Password: ")
    password_label.grid(row=2, column=0)
    password_entry = Entry(user_info_panel, textvariable=password)
    password_entry.grid(row=2, column=1)

    Label(user_info_panel, text="").grid(row=3)


    fullname_label = Label(user_info_panel, text="Fullname: ")
    fullname_label.grid(row=4, column=0)
    fullname_entry = Entry(user_info_panel, textvariable=fullname)
    fullname_entry.grid(row=4, column=1)


    register_btn = Button(new_user_window, text="Register")
    register_btn.pack()

main_menu()
