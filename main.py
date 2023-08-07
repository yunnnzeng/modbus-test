import tkinter as tk
from pyModbusTCP.client import ModbusClient

import tkinter as tk
from tkinter import messagebox


def modbus_write():
    modbus_ip = ent_ip.get()
    modbus_port = int(ent_port.get())
    c1 = ModbusClient(host=modbus_ip, port=modbus_port)
    _loc = int(write_loc.get())
    _value = int(write_val.get())
    c1.write_multiple_registers(_loc, [_value])
    messagebox.showinfo('write', '完成!')


def modbus_read():
    modbus_ip = ent_ip.get()
    modbus_port = int(ent_port.get())
    c1 = ModbusClient(host=modbus_ip, port=modbus_port)
    _loc = int(read_loc.get())
    _value = int(read_val.get())
    output = c1.read_holding_registers(_loc, _value)
    lbl_value["text"] = output


window = tk.Tk()
window.title("ModbusTest")
window.resizable(width=True, height=True)

# 1
frm_entry = tk.Frame(master=window)
lbl_ip = tk.Label(master=frm_entry, text="ip", width=8)
ent_ip = tk.Entry(master=frm_entry, width=20)
ent_port = tk.Entry(master=frm_entry, width=10)

lbl_ip.grid(row=0, column=0, sticky="w")
ent_ip.grid(row=0, column=1, sticky="e", columnspan=2)
ent_port.grid(row=0, column=3, sticky="e")

# 2
lbl_write = tk.Label(master=frm_entry, text="write", width=8)
write_loc = tk.Entry(master=frm_entry, width=8)
write_val = tk.Entry(master=frm_entry, width=11)

btn_write = tk.Button(
    master=frm_entry,
    text="write",
    command=modbus_write
)

lbl_write.grid(row=1, column=0, sticky="w")
write_loc.grid(row=1, column=1, sticky="e")
write_val.grid(row=1, column=2, sticky="e")
btn_write.grid(row=1, column=3, sticky="w")


# 3
lbl_read = tk.Label(master=frm_entry, text="read", width=8)
read_loc = tk.Entry(master=frm_entry, width=8)
read_val = tk.Entry(master=frm_entry, width=11)
btn_read = tk.Button(
    master=frm_entry,
    text="read",
    command=modbus_read
)

lbl_read.grid(row=2, column=0, sticky="w")
read_loc.grid(row=2, column=1, sticky="e")
read_val.grid(row=2, column=2, sticky="e")
btn_read.grid(row=2, column=3, sticky="w")


# 4
lbl_value = tk.Label(master=frm_entry, text="")
lbl_value.grid(row=3, column=1, sticky="w", columnspan=2)

frm_entry.grid(row=0, column=0, padx=10, pady=20, ipadx=10, ipady=10)
window.mainloop()
