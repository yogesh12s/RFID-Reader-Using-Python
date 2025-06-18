# 🛰️ RFID Reader Dashboard (Tkinter + Sllurp)

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
git clone https://github.com/your-username/rfid-reader-dashboard.git
cd rfid-reader-dashboard
