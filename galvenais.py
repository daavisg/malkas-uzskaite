import tkinter as tk
from tkinter import messagebox

piles = []

def update_display():
    
    listbox_piles.delete(0, tk.END)
    
    for pile in piles:
        listbox_piles.insert(tk.END, f"{pile['name']} - {pile['quantity']} logs")
    
    total_logs = sum(p['quantity'] for p in piles)
    label_total.config(text=f"kopā: {total_logs}")

def add_pile():
    
    name = entry_name.get().strip()     
    qty_str = entry_qty.get().strip()   

    if not name or not qty_str:
        messagebox.showwarning("Jāaizpilda abi lauki.")
        return

    try:
        qty = int(qty_str)
        if qty < 0:
            raise ValueError("Nevar bū negatīvs.")
    except ValueError:
        messagebox.showerror("Skaits nevar būt negatīvs.")
        return
    
    piles.append({"name": name, "quantity": qty})
    
    entry_name.delete(0, tk.END)
    entry_qty.delete(0, tk.END)
    
    update_display()

def remove_pile():
   
    selected_index = listbox_piles.curselection()
    
    if not selected_index:
        messagebox.showinfo("Izvēlies, kuru rindu izņemt")
        return
    
    piles.pop(selected_index[0])
    
    update_display()

def main():
    
    global root, listbox_piles, entry_name, entry_qty, label_total
    
    root = tk.Tk()
    root.title("Malkas uzskaite")

    frame_top = tk.Frame(root)
    frame_top.pack(pady=10)

    tk.Label(frame_top, text="Rinda:").grid(row=0, column=0, padx=5)
    entry_name = tk.Entry(frame_top, width=15)
    entry_name.grid(row=0, column=1, padx=5)

    tk.Label(frame_top, text="Daudzums:").grid(row=0, column=2, padx=5)
    entry_qty = tk.Entry(frame_top, width=8)
    entry_qty.grid(row=0, column=3, padx=5)

    btn_add = tk.Button(frame_top, text="Pievienot", command=add_pile)
    btn_add.grid(row=0, column=4, padx=5)

    btn_remove = tk.Button(frame_top, text="Noņemt", command=remove_pile)
    btn_remove.grid(row=0, column=5, padx=5)

    listbox_piles = tk.Listbox(root, width=50)
    listbox_piles.pack(pady=5)

    label_total = tk.Label(root, text="Kopā: 0", font=("Arial", 12, "bold"))
    label_total.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
