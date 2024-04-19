import tkinter as tk

def select_folder():
    pass

def rename_files():
    pass

root = tk.Tk()
root.title("Renamify")
root.resizable(False, False)


# Variables
var_folder_path = tk.StringVar()
mode_options = {
    "Add Prefix": "prefix", 
    "Add Suffix": "suffix", 
    "Replace Existing": "replace"
}
var_mode = tk.StringVar(value="Add Prefix")
var_new_name = tk.StringVar(value="New Name")

def update_mode(*args):
    mode = mode_options[var_mode.get()]
    print("Selected mode:", mode)


# Widgets for folder selection
lbl_select_folder = tk.Label(root, text="Select Folder:")
lbl_select_folder.grid(row=0, column=0, padx=10, pady=10)

ent_folder_path = tk.Entry(root, textvariable=var_folder_path, state="disabled")
ent_folder_path.grid(row=1, columnspan=2, column=0, sticky="ew", padx=10, pady=0)

btn_browse_folder = tk.Button(root, text="Browse", command=select_folder)
btn_browse_folder.grid(row=0, column=1, padx=10, pady=10)
# Empty row
root.grid_rowconfigure(2, minsize=20)

# Options for renaming
lbl_mode = tk.Label(root, text="Rename Mode:")
lbl_mode.grid(row=3, column=0, padx=10, pady=10)

optmen_mode = tk.OptionMenu(root, var_mode, *mode_options.keys(), command=update_mode)
optmen_mode.grid(row=3, column=1, padx=10, pady=10)

lbl_new_name = tk.Label(root, text="Rename Mode:")
lbl_new_name.grid(row=4, column=0, padx=10, pady=10)

ent_new_name = tk.Entry(root, textvariable=var_new_name)
ent_new_name.grid(row=4, column=1, sticky="ew", padx=10, pady=0)

# Rename button
btn_rename = tk.Button(root, text="Rename Files", command=rename_files)
btn_rename.grid(row=5, columnspan=2, pady=20)

# Start the GUI event loop
root.mainloop()
