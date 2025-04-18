import tkinter as tk
import webbrowser

BG_COLOR = "#1e1e1e"
ENTRY_BG = "#333333"
ENTRY_FG = "#ffffff"
BTN_BG = "#444444"
BTN_FG = "#ffffff"

def open_link(event=None):
    webbrowser.open_new("https://github.com/cr0sis")  

def on_entry_change(entry, *args):
    value = entry.get()
    if len(value) > 1 or not value.isalpha():
        entry.delete(0, tk.END)

def create_grid(parent):
    entries = []
    for row in range(10):
        for col in range(5):
            entry = tk.Entry(
                parent,
                width=2,
                justify='center',
                font=('Consolas', 16),
                bg=ENTRY_BG,
                fg=ENTRY_FG,
                insertbackground=ENTRY_FG,
                relief='flat'
            )
            entry.grid(row=row, column=col, padx=5, pady=5)
            entry_var = tk.StringVar()
            entry['textvariable'] = entry_var
            entry_var.trace_add("write", lambda *args, e=entry: on_entry_change(e))
            entries.append(entry)
    return entries

def reset_entries(entries):
    for entry in entries:
        entry.delete(0, tk.END)

root = tk.Tk()
root.configure(bg=BG_COLOR)
root.title("Blue Prince Journal")

max_title_width = 500
title_label = tk.Label(
    root,
    text="Blue Prince Painting Puzzle journal by cr0sis",
    fg="#66b2ff",
    bg=BG_COLOR,
    font=("Arial", 16, "bold"),
    cursor="hand2",
    wraplength=max_title_width,
    justify="center"
)
title_label.pack(pady=(15, 5))
title_label.bind("<Button-1>", open_link)


root.update_idletasks()
label_width = title_label.winfo_reqwidth()
window_width = max(label_width, 400)  # Add some padding

root.geometry(f"{window_width}x500")
root.minsize(400, 500)

main_frame = tk.Frame(root, bg=BG_COLOR)
main_frame.pack(expand=True)

entries = create_grid(main_frame)

reset_btn = tk.Button(
    main_frame,
    text="Reset Board",
    command=lambda: reset_entries(entries),
    bg=BTN_BG,
    fg=BTN_FG,
    font=('Arial', 12),
    relief='flat',
    activebackground="#555555",
    activeforeground="#ffffff"
)
reset_btn.grid(row=11, column=0, columnspan=5, pady=(10, 20))

root.mainloop()
