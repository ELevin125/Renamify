import tkinter as tk

def select_folder():
    pass

def rename_files():
    pass

root = tk.Tk()
root.title("Renamify")
root.resizable(False, False)

root.configure(bg="#333")
style = {"bg": "#333", "fg": "#CCC"}

# Variables
folder_path = tk.StringVar()
mode_var = tk.StringVar(value="entire")

# Widgets for folder selection
lbl_select_folder = tk.Label(root, text="Select Folder:", **style)
lbl_select_folder.grid(row=0, column=0, padx=10, pady=10)

ent_folder_path = tk.Entry(root, textvariable=folder_path, state="disabled", **style)
ent_folder_path.grid(row=1, columnspan=4, column=0, sticky="ew", padx=10, pady=0)

btn_browse_folder = tk.Button(root, text="Browse", command=select_folder, bg="#555", fg="#CCC")
btn_browse_folder.grid(row=0, column=1, padx=10, pady=10)
# Empty row
root.grid_rowconfigure(2, minsize=20)

# Option for renaming mode
lbl_mode = tk.Label(root, text="Rename Mode:", **style)
lbl_mode.grid(row=3, column=0, padx=10, pady=10)

btn_add_prefix = tk.Radiobutton(root, text="Add Prefix", variable=mode_var, value="prefix", **style)
btn_add_prefix.grid(row=4, column=0, sticky="w", padx=0)

btn_add_suffix = tk.Radiobutton(root, text="Add Suffix", variable=mode_var, value="suffix", **style)
btn_add_suffix.grid(row=4, column=1, sticky="w", padx=0)

btn_whole = tk.Radiobutton(root, text="Replace Whole Name", variable=mode_var, value="whole", **style)
btn_whole.grid(row=4, column=2, sticky="w", padx=0)

# Rename button
btn_rename = tk.Button(root, text="Rename Files", command=rename_files, bg="#555", fg="#CCC")
btn_rename.grid(row=5, column=1, pady=20)

# Start the GUI event loop
root.mainloop()
