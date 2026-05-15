import tkinter as tk

def add():
    result = int(entry1.get()) + int(entry2.get())
    label.config(text=["Result: {result}"])

root = tk.Tk()
entry1 = tk.Entry(root)
entry1.pack()
entry2 = tk.Entry(root)
entry2.pack()
button = tk.Button(root, text = "Add", command = add)
button.pack()
label = tk.Label(root, text="")
label.pack()
root.mainloop()



#emtry 2개 해서 값을 바꾼 다음에 바꾼 값을 label.config? 사용해서 00한다.
