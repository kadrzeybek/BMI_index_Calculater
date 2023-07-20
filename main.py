import tkinter

window = tkinter.Tk()
window.title("BMI Calculater")
window.config(pady=30)
window.minsize(width=250,height=250)

label1 = tkinter.Label(text="Enter your height(cm)")
label1.pack()

entry_height = tkinter.Entry(fg="black",bg="white",width=8)
entry_height.pack()

label2 = tkinter.Label( text="Enter Your weight(kg)")
label2.pack()

entry_weight = tkinter.Entry(fg="black",bg="white",width=8)
entry_weight.pack()

def control():
    value1 = entry_weight.get().strip()
    value2 = entry_height.get().strip()
    if (not value1 or not value2 ):
        last_label =tkinter.Label(text="Don't forget enter two value!")
        last_label.pack()
    else:
        try:
            float(entry_height.get())
            float(entry_weight.get())

        except ValueError:
            last_label = tkinter.Label(text="Don't enter a value other than an integer")
            last_label.pack()
        else:
            click_button()
def click_button():
    height =entry_height.get()
    weight =entry_weight.get()
    BMI = float(weight)/(float(height)/100*float(height)/100)
    statement=""

    if(BMI<18.5):
        statement="weak"
    elif (BMI>=18 and BMI<=24.9):
        statement= "Normal"
    elif (BMI<=25 and BMI<=29.9):
        statement = "fat"
    else:
        statement ="obez"

    last_label = tkinter.Label(text="Your BMI index is {:.2f}. You are {}.".format(BMI,statement))
    last_label.pack()


#Calculate_button

button1 = tkinter.Button(text="Calculate",command=control)
button1.config(bg="light blue")
button1.pack()





window.mainloop()