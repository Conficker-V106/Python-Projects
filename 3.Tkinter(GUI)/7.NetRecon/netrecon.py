import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk
import scapy.all as scapy
import nmap
import ipaddress
import re
from io import StringIO
import sys
from time import sleep


# Create the main application window
root = ttk.Window(themename='superhero')
root.title("Network Recon")
root.geometry("900x560+150+180")
root.resizable(False, False)


#Lanscan
def lanscan(ipaddr):
    ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

    while True:
        ip_add_range_entered = ipaddr
        if ip_add_range_pattern.search(ip_add_range_entered):
            valid = f"{ip_add_range_entered} is a valid ip address range \n"
            break
    

    tmp = sys.stdout 
    my_result = StringIO()
    sys.stdout = my_result
    
    result = scapy.arping(ip_add_range_entered)

    sys.stdout = tmp

    text1.delete(1.0, END)
    text1.insert(END, valid + my_result.getvalue())
    

def portscan(ipaddr , ports):
    port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
    port_min = 0
    port_max = 65535

    while True:
        ip_add_entered = ipaddr
        try:
            ip_address_obj = ipaddress.ip_address(ip_add_entered)
            text1.delete(1.0, END)
            text1.insert(END, "You entered a valid ip address.")
            break
        except:
            text1.delete(1.0, END)
            text1.insert(END, "You entered a invalid ip address.")
            return

    while True:
        port_range = ports
        port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
        if port_range_valid:
            port_min = int(port_range_valid.group(1))
            port_max = int(port_range_valid.group(2))
            break
    
    nm = nmap.PortScanner()
    resultstr = ""
    for port in range(port_min, port_max + 1):
        
        try:
            result = nm.scan(ip_add_entered, str(port))
            port_status = (result['scan'][ip_add_entered]['tcp'][port]['state'])
            resultstr += f"\nPort {port} is {port_status}"
            text1.delete(1.0, END)
            text1.insert(END, resultstr)

        except:
            resultstr += f"\nCannot scan port {port}."
            text1.delete(1.0, END)
            text1.insert(END, resultstr)





#first frame
f=Frame(root,bd=3,bg="black",width=450,height=280,relief=GROOVE)
f.place(x=0,y=0)
ip_var1 = tk.StringVar()
Label(f,text="Lan-Scan",font="Times 25 bold").place(x=155,y=10)
ip_label = ttk.Label(f, text="IP Address: ").place(x=95,y=100)
ip_entry = ttk.Entry(f,textvariable=ip_var1)
ip_entry.insert(0 , "192.168.1.0/24")
ip_entry.place(x=180,y=95)
ttk.Button(f,text="Scan",bootstyle="success",command=lambda: lanscan( ip_var1.get() )).place(x=205,y=165)

#second frame
f2=Frame(root,bd=3,bg="black",width=450,height=280,relief=GROOVE)
f2.place(x=450,y=0)
ip_var2 = tk.StringVar()
ports = tk.StringVar()
Label(f2,text="PortScan",font="Times 25 bold").place(x=155,y=10)
ip_label = ttk.Label(f2, text="IP Address: ").place(x=95,y=90)
ip_entry = ttk.Entry(f2,textvariable=ip_var2)
ip_entry.insert(0 , "192.168.1.0/24")
ip_entry.place(x=180,y=85)
port_label = ttk.Label(f2, text="Ports: ").place(x=95,y=140)
port_entry = ttk.Entry(f2,textvariable=ports)
port_entry.insert(0 , "<int>-<int>")
port_entry.place(x=180,y=135)
ttk.Button(f2,text="Scan",bootstyle="success",command=lambda: portscan( ip_var2.get(), ports.get())).place(x=205,y=205)



#forth frame
f4=Frame(root,bd=3,bg="black",width=900,height=280,relief=GROOVE)
f4.place(x=0,y=280)

text1=Text(f4,font="Robote 20",bg="white",fg="black",relief=GROOVE,wrap = WORD)
text1.place(x=0,y=0,width=885,height=275)

scrollbar1=ttk.Scrollbar(f4)
scrollbar1.place(x=885,y=0,height=275)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)


root.mainloop()