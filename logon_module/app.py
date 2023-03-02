from tkinter import *


def main_menu():
    main_window = Tk()
    main_window.geometry("300x300")
    main_window.title("login system")

    Label1 = Label(main_window, text="choose an option", bg="gray", fg="blue")
    Label1.pack(fill=X, pady=20)

    #button definition
    login_btn = Button(main_window, text="Log in", width="30", height="2")
    #button placement
    login_btn.pack(pady=20)

    register_btn = Button(main_window, text="Sign up", width="30", height="2")
    register_btn.pack(pady=20)

    main_window.mainloop()

main_menu()