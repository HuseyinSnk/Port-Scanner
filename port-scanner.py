import tkinter as tk
from tkinter import messagebox
import socket
import threading

# Global variables
scanning = False
open_ports_label = None
open_ports_text = None
ip_address_text = None

# List of well-known ports to scan
well_known_ports = [21, 22, 23, 25, 53, 80, 110, 115, 119, 123, 143, 161, 194, 443, 445, 993, 995, 1080, 3306, 3389]

def get_ip_address(url):
    try:
        ip_address = socket.gethostbyname(url)
        return ip_address
    except socket.gaierror as e:
        messagebox.showerror("Error", f"{e}")
        return None

def port_scan(url):
    ip_address = get_ip_address(url)
    if ip_address:
        open_ports = []
        for port in well_known_ports:
            if not scanning:
                messagebox.showinfo("Scan Canceled", "The scan has been canceled by the user.")
                return None
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(2)
                result = s.connect_ex((ip_address, port))
                if result == 0:
                    open_ports.append(port)
                    update_status(f"Port {port} is open", "green")
                else:
                    update_status(f"Port {port} is closed", "red")
                s.close()
            except KeyboardInterrupt:
                messagebox.showinfo("Scan Canceled", "The scan has been canceled by the user.")
                return None
            except socket.error:
                messagebox.showerror("Error", "Connection error.")
                return None
        return ip_address, open_ports

def update_status(message, color):
    status_text.config(text=message, fg=color)
    status_text.update()

def update_open_ports(ip_address, open_ports):
    global open_ports_text
    ip_address_text.config(text=f"IP Address: {ip_address}", fg="white")
    open_ports_text = ", ".join(map(str, open_ports))
    open_ports_label.config(text=f"Open Ports: {open_ports_text}", fg="white")

def start_scan():
    global scanning
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Warning", "Please enter a URL.")
        return
    
    scanning = True
    scan_label.config(text="Scanning...", fg="white")
    
    # Clear previous feedback
    result_label.config(text="")
    status_text.config(text="")
    
    threading.Thread(target=perform_scan, args=(url,), daemon=True).start()

def perform_scan(url):
    global scanning
    ip_address, open_ports = port_scan(url)
    if open_ports:
        update_open_ports(ip_address, open_ports)
        result_label.config(text="Scan completed.", fg="white")
    elif not scanning:
        result_label.config(text="Scan terminated.", fg="white")
    
    # Clear scanning message
    scan_label.config(text="")
    
    scanning = False

def cancel_scan():
    global scanning
    scanning = False
    messagebox.showinfo("Canceled", "The scan has been canceled by the user.")

# Create the main window
root = tk.Tk()
root.title("Port Scanning Tool")
root.geometry("700x300")  # Adjusted width and height
root.configure(bg="#303030")

# Font settings
font_style = ("Helvetica", 12)

# URL entry
url_label = tk.Label(root, text="URL:", font=font_style, bg="#303030", fg="white")
url_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
url_entry = tk.Entry(root, font=font_style, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10, columnspan=2, sticky="w")  # Adjusted sticky

# URL IP address label
ip_address_text = tk.Label(root, text="", font=font_style, bg="#303030", fg="white")
ip_address_text.grid(row=1, column=0, padx=10, pady=0, columnspan=3, sticky="w")  # Adjusted columnspan and sticky

# Open ports label
open_ports_label = tk.Label(root, text="Open Ports: ", font=font_style, bg="#303030", fg="white")
open_ports_label.grid(row=2, column=0, padx=10, pady=10, columnspan=2, sticky="w")

# Scan button
scan_button = tk.Button(root, text="Start Scan", command=start_scan, font=font_style, bg="#00b0f0", fg="white", relief="raised", borderwidth=2)
scan_button.grid(row=0, column=3, padx=10, pady=10)

# Scan results label
result_label = tk.Label(root, text="", font=font_style, wraplength=600, bg="#303030", fg="white")
result_label.grid(row=4, column=0, columnspan=4, padx=10, pady=(10, 20), sticky="w")  # Adjusted columnspan and sticky

# Scanning message
scan_label = tk.Label(root, text="", font=font_style, bg="#303030", fg="white")
scan_label.grid(row=1, column=3, padx=10, pady=10, sticky="w")  # Adjusted sticky

# Scan status label
status_text = tk.Label(root, text="", font=font_style, bg="#303030")
status_text.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

# Cancel button
cancel_button = tk.Button(root, text="Cancel", command=cancel_scan, font=font_style, bg="#d7191c", fg="white", relief="raised", borderwidth=2, width=15)
cancel_button.grid(row=6, column=0, padx=10, pady=10, columnspan=4)

# Center the interface window
root.update_idletasks()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - root.winfo_reqwidth()) // 2
y_coordinate = (screen_height - root.winfo_reqheight()) // 2
root.geometry("+{}+{}".format(x_coordinate, y_coordinate))

# Start the window
root.mainloop()
