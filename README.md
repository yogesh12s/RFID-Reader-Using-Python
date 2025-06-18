# 🛰️ RFID Reader Dashboard (Tkinter + Sllurp) SDK (Software Development Kit)

A Python-based desktop application that connects to **UHF RFID readers** (e.g., Zebra FX7500) via the **LLRP protocol** using the `sllurp` library. The app uses a user-friendly **Tkinter GUI** to scan, count, and display live EPC tag data in a real-time table.

---

## ✅ Features

- Connect to RFID reader via IP (LLRP protocol)
- Live EPC scanning and monitoring
- Display of:
  - EPC ID (not hex encoded)
  - Antenna ID
  - RSSI (Signal strength)
  - Tag seen count
  - Last seen timestamp
- Avoid duplicate EPC entries — updates tag counts instead
- Realtime **total unique EPCs**
- Stylish Treeview with bold headers
- Start and Stop reader with a button
- Clear results after stop

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/RFID-Reader-Using-Python.git
cd RFID-Reader-Using-Python
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix/macOS
source venv/bin/activate
pip install sllurp
```
##▶️ Usage
Ensure the RFID reader is powered on and accessible in the same network.

Run the Python app:
```bash
python reader.py
```
Enter your RFID reader IP (e.g., 192.168.55.161) in the input box.

Click ▶ Start Reader to begin scanning.

EPCs will appear in the grid with counts and RSSI.

Click ⏹ Stop Reader to stop scanning and clear the screen.
![image](https://github.com/user-attachments/assets/5ad9ecd4-e4e0-4a11-a282-4fe2b86a7bad)

**🔍 Use Cases -----------------------------------------------**

This tool can be used in various industries and environments:

✅ Warehouse Inventory Tracking

✅ Retail Backroom Tag Counting

✅ Asset Management

✅ Manufacturing Production Line Scanning

✅ Library Book/Media Tracking

✅ Live RFID Testing and Monitoring

✅ Field RFID Reader Debugging

**📈 Future Improvements -----------------------------------------------------------------**

You can build more advanced features on top of this app, such as:

💾 Data Persistence
Export scanned data to CSV / Excel

Save to SQL Server / SQLite databases for audit history

📊 Reporting & Filtering
Filter tags by Antenna, EPC prefix, or time range

Generate summary reports (total tags by antenna, etc.)

🌐 Web & API
Create a web-based version using Flask or FastAPI

Serve scanned data over an API or web dashboard

📲 Mobile / Cross-Platform
Build mobile app with Flutter or Kivy

Communicate with reader via socket or HTTP

📶 Reader Management
Support for multiple readers

Reader status monitor and alerts for disconnects

🛠️ Admin Tools
User login & access levels

Role-based views (e.g., Operator vs Admin)

🔄 Sync & Cloud
Sync scanned tags to a cloud server

View dashboards remotely

**Contact:------------------------------------**

**+918524011354
yogeshgokul372@gmail.com**


