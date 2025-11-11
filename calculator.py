# Calculator - v2.3

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

color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "white"

window = tk.Tk()
window.title("Calculator")
window.resizable(False, False)

frame = tk.Frame(window)

e_label = tk.Label(frame, text="", anchor=tk.E, justify="right", bg=color_black, fg=color_white, padx=10, font=SMALL_FONT_STYLE , width = 10, wraplength=300)
e_label.grid(row=0, column=0, columnspan=4, sticky="nsew")

label = tk.Label(frame, text="", anchor=tk.E, justify="right", bg=color_black, fg=color_white, padx=10, font=LARGE_FONT_STYLE, width = 10, wraplength=300)
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

# Bind Keys
for i in range(10):
    window.bind(str(i), lambda event, n=i: add_to_exp(str(n)))

window.bind('+', lambda event : add_to_exp('+'))
window.bind('-', lambda event : add_to_exp("-"))
window.bind('*', lambda event : add_to_exp("×"))
window.bind('/', lambda event : add_to_exp("÷"))
window.bind('.', lambda event : add_to_exp("."))
window.bind('%', lambda event : add_to_exp("%"))
window.bind('<Return>', lambda event : add_to_exp("="))
window.bind('<Escape>', lambda event : add_to_exp("AC"))
window.bind('<BackSpace>', lambda event : clear())



current = ""
expression = ""
isDeci = False

def add_to_exp(val):
    global current, expression, isDeci

    if current == "Error":
        current = ""
        update_label()

    if val not in special_symbols:
        if (val in right_symbols.values() or val in top_symbols):
            
            if current and current[-1] == ".":
                current += "0"
            append_operator(val)

        else:
            if isDeci and val == ".":
                return
            if val == ".":
                isDeci = True
            if val == "x²":
                try:
                    sqr(val)
                    return
                except Exception:
                    return
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
                print("Value not Recognized: " + str(val))
                return


def append_operator(operator):
    global current, expression, isDeci

    if operator == "÷":
        operator = "/"
    elif operator == "×":
        operator = "*"
    elif operator == "%":
        percent()
        return

    if current:   
        current += operator
        expression += current # Append number + operator

    elif not current:     
        if expression:
            expression = expression[:-1]  # Replace last operator
            expression += operator
        elif not expression:
            print("[Expression = Null] :: No Value Detected.")
            return
        
    current = ""
    isDeci = False
    update_e_label()
    update_label()

def calculate():
    try: 
        global expression, current
        expression += current
        update_e_label()
        if not expression:
            print("[Expression = Null] :: No Value Detected.")
            return
        current = str(eval(expression))
        expression = ""
        update_label()
    except Exception as e:
        current = "Error"
        update_label()
        print("Expression Error..")
        print("Exception found: " , e)
        return

def clear():
    global expression, current, isDeci
    if current:
        current = current[:-1]
        if '.' not in current:
            isDeci = False  
        update_label()
    else:
        print("[Value = Null] :: Nothing to clear.")
        return


def all_clear():
    global expression, current, isDeci
    expression = ""
    current = ""
    isDeci = False
    update_e_label()
    update_label()

def negate():
    global expression, current
    if current:
        try:
            current = "(" + str(eval(str(current) + "* -1")) + ")"
            update_label()
        except Exception as e:
            print("SYS Error: Negation not working..")
            print("Exception found: " , e)
    else:
        return

def percent():
    global current
    if current:
        try:
            current = str(eval("(" + str(current) + "/100)"))
            update_label()
        except Exception as e:
            print("SYS Error: Percent not working..")
            print("Exception found: " , e)
    else:
        print("No Value Detected.")
        return

def sqr(val):
    global current
    val = "**2"
    if current:
        current = "(" + current + val + ")"
        update_label()
    else:
        print("No Value Detected.")
        return
    
def update_label():
    global current
    label.config(text=current)

def update_e_label():
    global expression
    e_label.config(text=expression)

window.mainloop()