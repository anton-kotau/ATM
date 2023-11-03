import tkinter
import tkinter as tk
from tkinter import ttk
from unittest import result


ATM = tkinter.Tk()
ATM.title("ATM")
ATM.geometry('800x600')


#buttons:
#positionAndFormatNumbers
horizontal_spacing = 60
vertical_spacing = 60
starting_x = 450
starting_y = 350
#buttons_list
buttons_text = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "Ok", "Cancel"]
buttons = []

for text in buttons_text:
    button = tk.Button(ATM, text=text, width=5, height=2, bg="lightgrey", fg="navy", font=("Arial",13), relief=tk.RAISED)
    buttons.append(button)
"""button1 = tk.Button(ATM, text="1",width=4, height=2)
button2 = tk.Button(ATM, text="2",width=4, height=2)
button3 = tk.Button(ATM, text="3",width=4, height=2)
button4 = tk.Button(ATM, text="4",width=4, height=2)
button5 = tk.Button(ATM, text="5",width=4, height=2)
button6 = tk.Button(ATM, text="6",width=4, height=2)
button7 = tk.Button(ATM, text="7",width=4, height=2)
button8 = tk.Button(ATM, text="8",width=4, height=2)
button9 = tk.Button(ATM, text="9",width=4, height=2)
button0 = tk.Button(ATM, text="0",width=4, height=2)
buttonOk = tk.Button(ATM, text='Ok', width=7, height=2)
buttonCancel = tk.Button(ATM, text='Cancel', width=7, height=2)"""
x, y = starting_x, starting_y
for button in buttons:
    button.place(x=x, y=y)
    x += horizontal_spacing
    if x > starting_x + horizontal_spacing * 2:
        x = starting_x
        y += vertical_spacing

#screen:
def funkcja_deposit_z_innego_pliku(button_number):
    if button_number in [1,2]:
        entry.config(state=tk.NORMAL)
        entry.delete(0, tk.END)
    else:
        entry.config(state=tk.DISABLED)

def OkButton_click():
    if entry.get().isdigit():
        result_label.config(text=f"Deposit: {entry.get()}")
    else:
        result_label.config(text="Now your deposit:")

OkButton_index = buttons_text.index("Ok")
OkButton = buttons[OkButton_index]
OkButton.config(command=OkButton_click)

screen_output = tk.Text(ATM, height=1 , width=10)
screen_output.pack()

entry = tk.Entry(ATM, state=tk.DISABLED)
entry.pack()

result_label = tk.Label(ATM, text="")
result_label.pack()

ATM.mainloop()