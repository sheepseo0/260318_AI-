import tkinter as tk

def say_hello():
    name = entry.get()
    label.config(text = "Hello!{}".format(name)) #00의 텍스트를 바꿔라?
    
root = tk.Tk()

entry = tk.Entry(root) #글자 입
entry.pack()

button = tk.Button(root, text = "Click Me", command = say_hello)
button.pack() #pack():위치시키는 것
label = tk.Label(root, text = "NO input")
label.pack()


root.mainloop()
