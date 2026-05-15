import tkinter as tk

root = tk.Tk()

def show_fruit(event):
    selection = listbox.get(listbox.curselection())
    label.config(text=f"Selected: {selection}")

listbox = tk.Listbox(root)
for fruit in ["Apple", "Banana", "Cherry"]:
    listbox.insert(tk.END, fruit)
listbox.pack()
listbox.bind("<<ListboxSelect>>", show_fruit)
label = tk.Label(root, text="")
label.pack()
root.mainloop()
