import tkinter as tk
from tkinter import ttk, messagebox
from sllurp.llrp import LLRPReaderClient, LLRPReaderConfig, LLRP_DEFAULT_PORT
import threading


class RFIDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RFID Reader")
        self.root.geometry("850x550")
        self.root.configure(bg="#f0f0f0")

        self.tag_data = {}
        self.reader = None

        self.create_widgets()

    def create_widgets(self):
        # Top Frame for Controls
        top_frame = tk.Frame(self.root, bg="#f0f0f0")
        top_frame.pack(pady=10)

        tk.Label(top_frame, text="Reader IP:", bg="#f0f0f0", font=("Segoe UI", 10)).pack(side=tk.LEFT)
        self.ip_entry = tk.Entry(top_frame, width=20, font=("Segoe UI", 10))
        self.ip_entry.pack(side=tk.LEFT, padx=5)
        self.ip_entry.insert(0, "192.168.55.161")

        self.start_btn = tk.Button(top_frame, text="▶ Start Reader", command=self.start_reader,
                                   bg="#0078D7", fg="white", font=("Segoe UI", 10), relief=tk.FLAT)
        self.start_btn.pack(side=tk.LEFT, padx=10)

        self.stop_btn = tk.Button(top_frame, text="⏹ Stop Reader", command=self.stop_reader,
                                  bg="#D70022", fg="white", font=("Segoe UI", 10), relief=tk.FLAT, state=tk.DISABLED)
        self.stop_btn.pack(side=tk.LEFT)

        # Distinct EPC count label
        self.epc_count_label = tk.Label(self.root, text="Total Unique EPCs: 0",
                                        bg="#f0f0f0", font=("Segoe UI", 11, "bold"), fg="#333")
        self.epc_count_label.pack(pady=(0, 5))

        # Table Frame
        table_frame = tk.Frame(self.root)
        table_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))  # Bold header

        columns = ("EPC", "SeenCount", "Antenna", "RSSI", "LastSeen")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=20)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=150)

        vsb = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")

        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)

    def start_reader(self):
        ip = self.ip_entry.get().strip()
        if not ip:
            messagebox.showwarning("Warning", "Please enter reader IP.")
            return
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        threading.Thread(target=self.connect_reader, args=(ip,), daemon=True).start()

    def stop_reader(self):
        if self.reader:
            self.reader.disconnect()
            self.reader = None
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)

        # ✅ Clear TreeView and internal tag data
        self.tree.delete(*self.tree.get_children())
        self.tag_data.clear()
        self.epc_count_label.config(text="Total Unique EPCs: 0")

        messagebox.showinfo("Stopped", "Reader has been stopped and data cleared.")

    def connect_reader(self, ip):
        config = LLRPReaderConfig()
        config.report_every_n_tags = 1
        config.antennas = [1, 2]
        config.tx_power = {1: 200, 2: 200}
        config.keepalive_interval = 60
        config.session = 0
        config.start_inventory = True
        config.reconnect = True
        config.reconnect_retries = 3
        config.disconnect_when_done = False
        config.tag_content_selector = {
            'EnableAntennaID': True,
            'EnablePeakRSSI': True,
            'EnableLastSeenTimestamp': True,
            'EnableTagSeenCount': True,
            'C1G2EPCMemorySelector': {
                'EnableCRC': False,
                'EnablePCBits': False,
            }
        }

        try:
            self.reader = LLRPReaderClient(ip, LLRP_DEFAULT_PORT, config)
            self.reader.add_tag_report_callback(self.tag_report_callback)
            self.reader.connect()
        except Exception as e:
            self.start_btn.config(state=tk.NORMAL)
            self.stop_btn.config(state=tk.DISABLED)
            messagebox.showerror("Connection Failed", str(e))

    def tag_report_callback(self, reader, tag_reports):
        for tag in tag_reports:
            try:
                epc = tag['EPC'].decode(errors="ignore").strip()
            except:
                epc = str(tag['EPC']).strip()

            seen = tag.get('TagSeenCount', 1)
            antenna = tag.get('AntennaID', '-')
            rssi = tag.get('PeakRSSI', '-')
            last_seen = tag.get('LastSeenTimestampUTC', '')

            if epc in self.tag_data:
                self.tag_data[epc]['SeenCount'] += seen
                self.tag_data[epc]['Antenna'] = antenna
                self.tag_data[epc]['RSSI'] = rssi
                self.tag_data[epc]['LastSeen'] = last_seen
            else:
                self.tag_data[epc] = {
                    'SeenCount': seen,
                    'Antenna': antenna,
                    'RSSI': rssi,
                    'LastSeen': last_seen
                }

        self.root.after(0, self.update_treeview)

    def update_treeview(self):
        current_epcs = {self.tree.item(iid)["values"][0]: iid for iid in self.tree.get_children()}

        for epc, data in self.tag_data.items():
            row = (epc, data['SeenCount'], data['Antenna'], data['RSSI'], data['LastSeen'])
            if epc in current_epcs:
                self.tree.item(current_epcs[epc], values=row)
            else:
                self.tree.insert("", tk.END, values=row)

        self.epc_count_label.config(text=f"Total Unique EPCs: {len(self.tag_data)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = RFIDApp(root)
    root.mainloop()
