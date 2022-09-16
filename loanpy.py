# TODO: better styling
from loanpy import home, car, welcome

import tensorflow as tf
import tkinter as tk

root = tk.Tk()
root.geometry(f"800x500")
root.title("Loan Py")

main_frame = tk.Frame(root)

homepage = home.HomeLoan(main_frame)
carpage = car.CarLoan(main_frame)

main_frame.pack(expand=True)

welcomepage = welcome.Welcome(main_frame)
welcomepage.frame.pack()

outputpage = tk.Frame(main_frame, bg="#11121d")
tk.Label(outputpage, text="here is the output!").pack()

pages = [carpage.frame, homepage.frame]

def set_page(f: tk.Frame):
    # if f.winfo_id() != homepage.frame.winfo_id():
    submit_button.forget()
    welcomepage.frame.forget()
    for p in pages: p.forget()
    f.pack()
    submit_button.pack(side=tk.BOTTOM)

def submit():
    set_page(outputpage)
    nice = homepage.get_data()
    model = tf.keras.models.load_model('newmodel.h5')
    model.predict([nice])
    print("Y" if model > 0.5 else "N")

bottom = tk.Frame(root)
submit_button = tk.Button(bottom, text="Submit", command=submit, fg="green")
car_button = tk.Button(bottom, text="Car Loan", command=lambda: set_page(carpage.frame))
car_button.pack(side=tk.LEFT, padx=10)
home_button = tk.Button(bottom, text="Home Loan", command=lambda: set_page(homepage.frame))
home_button.pack(side=tk.RIGHT, padx=10)
bottom.pack(side=tk.BOTTOM)

root.mainloop()
