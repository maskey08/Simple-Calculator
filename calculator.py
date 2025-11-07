import tkinter as tk

button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    [".", "0", "x²", "="]
]

right_symbols = {"/" : "÷", "*" : "×", "-" : "-", "+" : "+", "=" : "="}
top_symbols = ["AC", "+/-", "%"]
special_symbols = ["AC", "+/-", "="]


LARGE_FONT_STYLE = ("Arial", 30, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "white"

window = tk.Tk()
window.title("Calculator")
window.resizable(False, False)

frame = tk.Frame(window)

e_label = tk.Label(frame, text="", anchor=tk.E, bg=color_black, fg=color_white, padx=20, font=SMALL_FONT_STYLE , width = 10)
e_label.grid(row=0, column=0, columnspan=4, sticky="nsew")

label = tk.Label(frame, text="", anchor=tk.E, bg=color_black, fg=color_white, padx=20, font=LARGE_FONT_STYLE, width = 10)
label.grid(row=1, column=0, columnspan=4, sticky="nsew")

for row in range(5):
    for col in range(4):
        val = button_values[row][col]
        button = tk.Button(frame, text=val , font=("Arial", 30),   width=3, height=1, command=lambda v=val: add_to_exp(v))
        button.grid(row = row + 2, column = col)
        if val in top_symbols:
            button.config(background=color_light_gray)
        elif val in right_symbols.values():
            button.config(foreground=color_white, background=color_orange)
        else: 
            button.config(foreground=color_white, background=color_dark_gray)
frame.pack()

current = ""
expression = ""
isDeci = False

def add_to_exp(val):
    global current, expression, isDeci

    if val not in special_symbols:
        if (val in right_symbols.values() or val in top_symbols):
            append_operator(val)

        else:
            if isDeci and val == ".":
                return
            if val == ".":
                isDeci = True
            if val == "x²":
                current = current[-1]
                val = "**2"

            current += str(val)
            print(current)
        update_label()
    else:
        match val:
            case "=":
                calculate()
            case "AC":
                all_clear()
            case "+/-":
                negate()
            case _:
                return

def sqrt():
        global current
        current = str(eval(f"{current}**0.5"))
        update_label()         

def append_operator(operator):
    global current, expression, isDeci
    if operator == "÷":
        operator = "/"
    elif operator == "×":
        operator = "*"
    elif operator == "%":
        operator = "/100"

    if current:
        current += operator
        expression += current # Append number + operator        
    elif not current:
        if expression:
            expression = expression[:-1]  # Replace last operator
            expression += operator
    current = ""
    isDeci = False
    update_e_label()
    update_label()

def calculate():
    global expression, current
    expression += current
    update_e_label()
    current = str(eval(expression))
    expression = ""
    update_label()

def all_clear():
    global expression, current
    expression = ""
    current = ""
    update_e_label()
    update_label()

def negate():
    global expression, current
    current = "(" + str(eval(str(current) + "* -1")) + ")"
    update_label()

    
def update_label():
    global current
    label.config(text=current)

def update_e_label():
    global expression
    e_label.config(text=expression)

window.mainloop()