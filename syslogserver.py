import socketserver
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from threading import Thread
import datetime

# Global variable for the GUI
log_messages = []

# Syslog Server Implementation
class SyslogUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        message = data.decode('utf-8')
        log_entry = f"{datetime.datetime.now()} - {self.client_address[0]}: {message}"
        log_messages.append(log_entry)
        update_gui(log_entry)
        log_to_file(log_entry)

# Function to log messages to a file
def log_to_file(message):
    with open("syslog.log", "a") as file:
        file.write(message + "\n")

# Function to update the GUI
def update_gui(message):
    text_area.insert(tk.END, message + "\n")
    text_area.yview(tk.END)

# GUI Implementation
def start_gui():
    global text_area
    root = tk.Tk()
    root.title("Syslog Viewer")
    text_area = ScrolledText(root, wrap=tk.WORD, width=250, height=50)
    text_area.pack(pady=10, padx=10)
    root.mainloop()

# Start Syslog Server
def start_syslog_server():
    server = socketserver.UDPServer(("0.0.0.0", 514), SyslogUDPHandler)
    server.serve_forever()

# Start GUI and Server in separate threads
if __name__ == "__main__":
    Thread(target=start_syslog_server, daemon=True).start()
    start_gui()
