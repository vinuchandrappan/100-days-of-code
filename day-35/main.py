from tkinter import *

window=Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
#label
my_label=Label(text="I am a label")
my_label.pack()

my_label["text"]="New text"
my_label.config(text="New text")

#button

def button_clicked():
  print("Welcome")
  new_text=input.get()
  my_label.config(text=new_text)

button=Button(text="click here", command=button_clicked)
button.pack()

#Entry
input=Entry(width=10)
input.pack()
print(input.get())

window.mainloop()