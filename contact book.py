import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

CONTACTS_FILE = "contacts.json"


def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return []


def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact():
    name = simpledialog.askstring("Input", "Enter Name:")
    phone = simpledialog.askstring("Input", "Enter Phone Number:")
    email = simpledialog.askstring("Input", "Enter Email:")
    address = simpledialog.askstring("Input", "Enter Address:")

    if not name or not phone:
        messagebox.showwarning("Warning", "Name and Phone are required!")
        return

    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    save_contacts(contacts)
    messagebox.showinfo("Success", "Contact added successfully!")
    view_contacts()


def view_contacts():
    contacts = load_contacts()
    listbox.delete(0, tk.END)
    for contact in contacts:
        listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")


def search_contact():
    term = simpledialog.askstring("Search", "Enter Name or Phone Number:")
    contacts = load_contacts()
    results = [c for c in contacts if term in c['name'] or term in c['phone']]
    listbox.delete(0, tk.END)
    for contact in results:
        listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")


def update_contact():
    name = simpledialog.askstring("Update", "Enter the Name of the Contact to Update:")
    contacts = load_contacts()

    for contact in contacts:
        if contact['name'] == name:
            contact['phone'] = simpledialog.askstring("Update", "Enter New Phone Number:",
                                                      initialvalue=contact['phone']) or contact['phone']
            contact['email'] = simpledialog.askstring("Update", "Enter New Email:", initialvalue=contact['email']) or \
                               contact['email']
            contact['address'] = simpledialog.askstring("Update", "Enter New Address:",
                                                        initialvalue=contact['address']) or contact['address']
            save_contacts(contacts)
            messagebox.showinfo("Success", "Contact updated successfully!")
            view_contacts()
            return
    messagebox.showwarning("Error", "Contact not found!")


def delete_contact():
    name = simpledialog.askstring("Delete", "Enter the Name of the Contact to Delete:")
    contacts = load_contacts()

    new_contacts = [c for c in contacts if c['name'] != name]
    if len(new_contacts) == len(contacts):
        messagebox.showwarning("Error", "Contact not found!")
    else:
        save_contacts(new_contacts)
        messagebox.showinfo("Success", "Contact deleted successfully!")
        view_contacts()


def exit_app():
    root.destroy()


root = tk.Tk()
root.title("CONTACT BOOK")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=50, height=10)
listbox.pack()

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Contact", command=add_contact, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="View Contacts", command=view_contacts, bg="#2196F3", fg="white").grid(row=0, column=1,
                                                                                                 padx=5)
tk.Button(btn_frame, text="Search Contact", command=search_contact, bg="#FF9800", fg="white").grid(row=0, column=2,
                                                                                                   padx=5)
tk.Button(btn_frame, text="Update Contact", command=update_contact, bg="#FFC107", fg="black").grid(row=1, column=0,
                                                                                                   padx=5)
tk.Button(btn_frame, text="Delete Contact", command=delete_contact, bg="#F44336", fg="white").grid(row=1, column=1,
                                                                                                   padx=5)
tk.Button(btn_frame, text="Exit", command=exit_app, bg="#9E9E9E", fg="white").grid(row=1, column=2, padx=5)

view_contacts()
root.mainloop()
