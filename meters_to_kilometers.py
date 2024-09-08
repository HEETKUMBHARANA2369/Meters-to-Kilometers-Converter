from customtkinter import *
window = CTk()
#defining convert function for the conversion
def convert():
    try:
        km = float(entry.get())
        meters = km * 1000 #formula to convert meters into kilometers
        output.configure(text = f"Meters: {meters}")
    except ValueError:
        output.configure(text = "Enter a valid number!!!!")

def clear():
    output.configure(text = "")
    print("Cleared !")

def exit():
    window.destroy()

title = CTkLabel(window, text="Kilometers to Meters Converter", font=("Calibri", 25 ))
title.pack(padx = 10)
window.title("Kilometers to Meters Converter")
# setting a frame for the input label and the button
frame = CTkFrame(window,fg_color="transparent",border_color="white",border_width=1)
entry = CTkEntry(frame)
entry.pack(pady = 12)
btn = CTkButton(frame,text="Convert",width=20,command=convert)
btn.pack(side = "left",padx = 12,pady = 12)
clr = CTkButton(frame,command = clear,width=20,text = "Clear")
clr.pack(side = "left",padx = 12,pady = 12)
frame.pack(pady = 40)
exit_button = CTkButton(window,text = "Exit",command = exit)
exit_button.pack()
#output label
output = CTkLabel(window, text="Output", font=("Calibri",25))
output.pack()
window.mainloop()