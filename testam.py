import tkinter as tk

root = tk.Tk()
root.title("Malkas uzskaite šķūnī")

main_frame = tk.Frame(root, width=500, height=400)
main_frame.pack(fill="both", expand=True)

lbl_heading = tk.Label(main_frame, text="Pievieno vai noņem no uzskaites kurināmo malku")
lbl_heading.place(relx=0.5, rely=0.1, anchor="center")

bottom_frame = tk.Frame(main_frame)
bottom_frame.place(relx=0.5, rely=0.3, anchor="center")

#teksti, japadoma vai liniju vajadzetu, it ka man skuni ta ir uz papira saraktits
tk.Label(bottom_frame, text="Līnija:").grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(bottom_frame, width=15)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(bottom_frame, text="Pagaļu skaits:").grid(row=0, column=2, padx=5, pady=5)
entry_qty = tk.Entry(bottom_frame, width=8)
entry_qty.grid(row=0, column=3, padx=5, pady=5)

# pogas
btn_add = tk.Button(bottom_frame, text="Pievienot")
btn_add.grid(row=1, column=1, padx=5, pady=5)

btn_remove = tk.Button(bottom_frame, text="Noņemt")
btn_remove.grid(row=1, column=2, padx=5, pady=5)

#listbox, butu jauzskaita visi pievienotie
listbox_piles = tk.Listbox(main_frame, width=50, height=6)
listbox_piles.place(relx=0.5, rely=0.55, anchor="center")

# cik kopaa pagales
label_total = tk.Label(main_frame, text="Pagales kopā: 0")
label_total.place(relx=0.5, rely=0.8, anchor="center")

root.mainloop()