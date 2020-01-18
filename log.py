# импорт
from tkinter import *
from tkinter import messagebox
import pickle

# размер и название окна
root = Tk()
root.geometry("300x500")
root.title("Войти в систему")


# создание надписей, полей ввода и кнопки регистрация
def registration():
    text = Label(text="Для входа в систему - зарегистрируйтесь")
    text_log = Label(text="Введите логин:")
    registr_login = Entry()
    text_passwod1 = Label(text="Введите ваш пароль:")
    registr_password1 = Entry()
    text_passwod2 = Label(text="Подтвердите пароль:")
    registr_password2 = Entry(show="*")
    button_register = Button(text="зарегистрироваться", command=lambda: save())
    text.pack()
    text_log.pack()
    registr_login.pack()
    text_passwod1.pack()
    registr_password1.pack()
    text_passwod2.pack()
    registr_password2.pack()
    button_register.pack()

    def save():
        login_pass_save = {}
        login_pass_save[registr_login.get()] = registr_password1.get()
        f = open("login.txt", "wb")
        pickle.dump(login_pass_save, f)
        f.close()
        login()


def login():
    text_log = Label(text="Поздравляем! Теперь Вы можете войти в систему!")
    text_enter_login = Label(text="Введите ваш логин:")
    enter_login = Entry()
    text_enter_pass = Label(text="Введите ваш пароль:")
    enter_password = Entry(show="*")
    button_enter = Button(text="Войти", command=lambda: log_pass())
    text_log.pack()
    text_enter_login.pack()
    enter_login.pack()
    text_enter_pass.pack()
    enter_password.pack()
    button_enter.pack()

    def log_pass():
        f = open("login.txt", "rb")
        a = pickle.load(f)
        f.close
        if enter_login.get() in a:
            if enter_password.get() == a[enter_login.get()]:
                messagebox.showinfo("Вход выполнен!", "Привет, у тебя 5 новых сообщений!")
            else:
                messagebox.showerror("Ошибка вы ввели неверный логин или пароль!")
        else:
            messagebox.showerror("Ошибка!", "Неверный логин!")


registration()

root.mainloop()

