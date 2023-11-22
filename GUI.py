from curses.ascii import isdigit
import tkinter as tk
from bank_account import bankAccount
from Result import Ok, Error

ATM = tk.Tk()
ATM.title("ATM")
ATM.iconbitmap("C:\\projects\\Bank_account\\atm.ico")
window_height = 700
window_width = 600
ATM.geometry(f"{window_height}x{window_width}")


#buttons:
#positionAndFormatNumbers
horizontal_spacing = 60
vertical_spacing = 60
starting_x = 260
starting_y = 350
#buttons_list
buttons_text = [
    "1", "2", "3", 
    "4", "5", "6", 
    "7", "8", "9", 
    "Ok", "0", "Cancel"
]
buttons = []

def click_Ok_button():
    input_text = transaction_entry.get()
    if input_text.isdigit():
        deposit(int(input_text))
    else:
        print("Error")
        
for text in buttons_text:
    if text in ["1", "2", "3", 
    "4", "5", "6", 
    "7", "8", "9", 
    "0"
    ]:
        button = tk.Button(ATM, text=text, width=5, height=2, bg="lightgrey", fg="navy", font=("Arial",13), relief=tk.RAISED, command=lambda value=text: handle_button_click(value))
        buttons.append(button)
    elif text=="Ok" or text=="Cancel":
           button = tk.Button(ATM, text=text, width=5, height=2, bg="lightgrey", fg="navy", font=("Arial",13), relief=tk.RAISED, command= click_Ok_button)
           buttons.append(button)

        

def handle_button_click(value):
    current_text = transaction_entry.get()
    transaction_entry.delete(0, tk.END)
    transaction_entry.insert(0, current_text + value)
x, y = starting_x, starting_y
for button in buttons:
    button.place(x=x, y=y)
    x += horizontal_spacing
    if x > starting_x + horizontal_spacing * 2:
        x = starting_x
        y += vertical_spacing
myBalance = 0 

#screen_output:

def deposit():
    deposit_amount = int(transaction_entry.get())
    result = account.deposit(deposit_amount)
    if result.is_ok():
        balance_label.config(text=f"Balance: {account.get_balance()}$ ")
    else:
        balance_label.config(text=result.message)
    transaction_entry.delete(0,tk.END)

account = bankAccount()

balance_label = tk.Label(ATM, text="Balance: 0$" )
balance_label.pack()

transaction_entry = tk.Entry(ATM)
transaction_entry.pack()

def try_withdrawal():
    try_withdrawal_amount = int(transaction_entry.get())
    result = account.try_withdrawal(try_withdrawal_amount)
    if result.is_ok():
        balance_label.config(text=f"Balance: {account.get_balance()}$")
    else:
        balance_label.config(text=result.message)
    transaction_entry.delete(0, tk.END)

def exit():
    ATM.quit()

menu_frame = tk.Frame(ATM)
menu_frame.pack(pady=50)

menu = tk.Menu(ATM)
menu.add_command(label="Deposit", command=deposit)
menu.add_command(label="Withdrawal", command=try_withdrawal)
menu.add_command(label="Exit", command=exit)

deposit_button = tk.Button(menu_frame, text="Deposit", command=deposit, width=7, height=1, bg="lightgrey", fg="navy", font=("Arial",9), relief=tk.RAISED)
deposit_button.grid(row=0, column=0, padx=10)

withdrawal_button = tk.Button(menu_frame, text="Withdrawal", command=try_withdrawal, width=9, height=1, bg="lightgrey", fg="navy", font=("Arial",9), relief=tk.RAISED)
withdrawal_button.grid(row=0, column=1, padx=10)

exit_button = tk.Button(menu_frame, text="Exit", command=exit, width=7, height=1, bg="lightgrey", fg="navy", font=("Arial",9), relief=tk.RAISED)
exit_button.grid(row=0, column=2, padx=10)

ATM.resizable(width=False, height=False)
ATM.mainloop()