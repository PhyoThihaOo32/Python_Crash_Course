import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_contacts():
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact_gui():
    name = simpledialog.askstring("Add Contact", "Enter contact name:")
    if not name:
        return
    name = name.strip().title()
    if name in contacts:
        messagebox.showwarning("Warning", f"Contact '{name}' already exists!")
        return
    phone = simpledialog.askstring("Phone", "Enter phone number:")
    email = simpledialog.askstring("Email", "Enter email address:")
    group = simpledialog.askstring("Group", "Enter contact group (Family, Work, Friends):")
    contacts[name] = {"Phone": phone, "Email": email, "Group": group}
    save_contacts()
    messagebox.showinfo("Success", f"Contact '{name}' added!")

def view_contacts_gui():
    if not contacts:
        messagebox.showinfo("Contacts", "No contacts found.")
        return
    display = ""
    groups = {}
    for name, info in contacts.items():
        group = info.get("Group", "Ungrouped")
        groups.setdefault(group, []).append((name, info))
    for group, members in groups.items():
        display += f"\n=== {group} ===\n"
        for name, info in members:
            display += f"{name}\n"
            for key, value in info.items():
                if key != "Group":
                    display += f"   {key}: {value}\n"
    messagebox.showinfo("Contacts", display)

def delete_contact_gui():
    name = simpledialog.askstring("Delete Contact", "Enter contact name to delete:")
    if not name:
        return
    name = name.strip().title()
    if name in contacts:
        del contacts[name]
        save_contacts()
        messagebox.showinfo("Deleted", f"Contact '{name}' has been deleted.")
    else:
        messagebox.showwarning("Warning", f"Contact '{name}' not found.")

def exit_app():
    root.destroy()

contacts = load_contacts()

root = tk.Tk()
root.title("Contact Book")
root.geometry("300x250")

# Buttons
tk.Button(root, text="Add Contact", command=add_contact_gui, width=25).pack(pady=10)
tk.Button(root, text="View Contacts", command=view_contacts_gui, width=25).pack(pady=10)
tk.Button(root, text="Delete Contact", command=delete_contact_gui, width=25).pack(pady=10)
tk.Button(root, text="Exit", command=exit_app, width=25, bg="gray", fg="white").pack(pady=10)

root.mainloop()