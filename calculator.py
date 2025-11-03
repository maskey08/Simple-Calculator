# Simple Calculator 
# This program is a simple calculator made using Tkinter library. 
# Error Library => [Error 101 : Empty or null value or NaN.] [Error 102 : Problem with operator.]

import tkinter as tk

# Setup window
root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)

# Global variables
val1=None;
val2=None;
operator=None;
isDecimal=False;

# number function to input multi digit number
def number(n):
    val = TXT.get("1.0", tk.END).strip()
    if isDecimal:
        new_val= val+str(n)
    else:
        if not val:
            new_val = str(n)
        else:
            try:
                new_val = str(int(val) * 10 + n)
            except ValueError:
                new_val = str(n)  # fallback if val isn't a number
    TXT.delete("1.0", tk.END)
    TXT.insert(tk.END, new_val)

# decimal function to include point value calculations
def decimal():
    global isDecimal;
    isDecimal=True
    val = TXT.get("1.0", tk.END).strip()
    if not val:
        return
    else:
        try:
            new_val = val+'.'
        except ValueError:
            new_val = val+'.0' # fallback if val isn't a number
    TXT.delete("1.0", tk.END)
    TXT.insert(tk.END, new_val)    

# on_operator_click function to store first value and operation type.
def on_operator_click(op):
    global val1, operator, isDecimal
    operator = op
    operator_buttons = {
    "add": add_btn,
    "sub": sub_btn,
    "multi": multi_btn,
    "div": div_btn
}
    try:
        val1 = float(TXT.get("1.0", tk.END))
        TXT.delete('1.0', tk.END)
        isDecimal=False
        operator_buttons[op].config(bg="yellow")
    except Exception:
        TXT.insert(tk.END,"Error 101!")

    

# answer function to store second value.
def answer():
    global val2, isDecimal
    try:
        val2 = float(TXT.get("1.0", tk.END))
        TXT.delete('1.0', tk.END)
        isDecimal=False
        calculate()
    except Exception:
        TXT.insert(tk.END,"Error 101!")

# calculate function to calculate according to the operation type and displays the answer. Resets the button highlight after calculation.
def calculate():
    match operator:
        case 'add':
            TXT.insert(tk.END,val1+val2)
            add_btn.config(bg="SystemButtonFace")
        case 'sub':
            TXT.insert(tk.END,val1-val2)
            sub_btn.config(bg="SystemButtonFace")
        case 'multi':
            TXT.insert(tk.END,val1*val2)
            multi_btn.config(bg="SystemButtonFace")
        case 'div':
            TXT.insert(tk.END,val1/val2)
            div_btn.config(bg="SystemButtonFace")
        case _:
            TXT.insert(tk.END,"Error 102!")

# clear function deletes the last entered digit.
def clear():
    val = TXT.get("1.0", tk.END).strip()
    new_val= val[:-1]    
    TXT.delete('1.0', tk.END)
    TXT.insert(tk.END,new_val)

# all_clear function deletes everything and starts fresh.
def all_clear(): 
    global val1, val2, operator
    val1=None;
    val2=None;
    operator=None;
    TXT.delete('1.0', tk.END)


# Creating Text field and buttons of calculator.
TXT = tk.Text(root,height="3", width= "30", font=("Arial", 16))

clear_btn = tk.Button(root, text="C", width=3, command=clear)
all_clear_btn = tk.Button(root, text="AC", width=3, command=all_clear)

add_btn = tk.Button(root, text='+', width=3, command=lambda: on_operator_click('add'))
sub_btn = tk.Button(root, text='–', width=3, command=lambda: on_operator_click('sub'))
multi_btn = tk.Button(root, text='x', width=3, command=lambda: on_operator_click('multi'))
div_btn = tk.Button(root, text='÷', width=3, command=lambda: on_operator_click('div'))

one_btn = tk.Button(root, text='1', width=5, command=lambda: number(1))
two_btn = tk.Button(root, text='2', width=5, command=lambda: number(2))
three_btn = tk.Button(root, text='3', width=5, command=lambda: number(3))
four_btn = tk.Button(root, text='4', width=5, command=lambda: number(4))
five_btn = tk.Button(root, text='5', width=5, command=lambda: number(5))
six_btn = tk.Button(root, text='6', width=5, command=lambda: number(6))
seven_btn = tk.Button(root, text='7', width=5, command=lambda: number(7))
eight_btn = tk.Button(root, text='8', width=5, command=lambda: number(8))
nine_btn = tk.Button(root, text='9', width=5, command=lambda: number(9))
zero_btn = tk.Button(root, text='0', width=5, command=lambda: number(0))

ans_btn = tk.Button(root, text='=', width=5, command=answer)
decimal_btn = tk.Button(root, text='.', width=5, command=decimal)

# bind_keys function to bind keyboard numbers to the buttons on screen.
def bind_keys():
    for i in range(10):
        root.bind(str(i), lambda event, n=i: number(n))
    root.bind('+', lambda event, op = 'add' : on_operator_click(op))
    root.bind('-', lambda event, op = 'sub' : on_operator_click(op))
    root.bind('*', lambda event, op = 'multi' : on_operator_click(op))
    root.bind('/', lambda event, op = 'div' : on_operator_click(op))
    root.bind('<Return>', lambda event : answer())
bind_keys()

# style for buttons.
btn_opts = {'padx': 4, 'pady': 5, 'sticky': 'nsew'}

# adding buttons and text field to the window.
add_btn.grid(row=3, column=4, **btn_opts)
sub_btn.grid(row=4, column=4, **btn_opts)
multi_btn.grid(row=5, column=4, **btn_opts)
div_btn.grid(row=6, column=4, **btn_opts)

one_btn.grid(row=5, column=1, **btn_opts)
two_btn.grid(row=5, column=2, **btn_opts)
three_btn.grid(row=5, column=3, **btn_opts) 

four_btn.grid(row=4, column=1, **btn_opts)
five_btn.grid(row=4, column=2, **btn_opts)
six_btn.grid(row=4, column=3, **btn_opts) 

seven_btn.grid(row=3, column=1, **btn_opts)
eight_btn.grid(row=3, column=2, **btn_opts)
nine_btn.grid(row=3, column=3, **btn_opts)

zero_btn.grid(row=6, column=2, **btn_opts)
ans_btn.grid(row=6, column=3, **btn_opts)
decimal_btn.grid(row=6, column=1, **btn_opts)

TXT.grid(row=1, column=1, rowspan=2, columnspan=3, padx=10, pady=20)
all_clear_btn.grid(row=1, column=4, padx=(5, 10), pady=(15, 5))
clear_btn.grid(row=2, column=4, padx=(5, 10), pady=(5,15))

# loops the window to show changes.
root.mainloop()
