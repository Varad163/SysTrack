# ⏱️ App Time Tracker (Ubuntu)

A lightweight **Ubuntu background app usage tracker** written in Python.
It tracks how much time you spend in applications like **VS Code, Browser, Terminal**, etc.,
using **1-second polling**, and **starts automatically after login**.

---

## ✨ Features

- 🖥️ Tracks active application usage
- ⏱️ 1-second polling
- 📊 Day-wise usage stored in JSON
- 🔄 Runs silently in background
- 🚀 Auto-starts after every login (systemd)
- 🐍 Uses Python virtual environment

---

## 🖥️ Requirements

- Ubuntu (20.04+ recommended)
- Python 3.9+
- systemd (default on Ubuntu)

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/app_time_tracker.git
cd app_time_tracker
```

⚠️ Do not move or rename the folder after setup.

---

### 2️⃣ Install Python Tools

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv -y
```

---

### 3️⃣ Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Manually (Test First)

```bash
python3 main.py track
```

Press **Ctrl + C** to stop.

---

## 🔥 Enable Auto-Start After Login

### 5️⃣ Make Script Executable

```bash
chmod +x main.py
```

Ensure first line of `main.py`:

```python
#!/usr/bin/env python3
```

---

### 6️⃣ Create systemd User Service

```bash
mkdir -p ~/.config/systemd/user
nano ~/.config/systemd/user/app-time-tracker.service
```

Paste:

```ini
[Unit]
Description=App Time Tracker (1s polling)
After=graphical-session.target

[Service]
Type=simple
ExecStart=%h/app_time_tracker/venv/bin/python %h/app_time_tracker/main.py track
WorkingDirectory=%h/app_time_tracker
Restart=always
RestartSec=5
Environment=DISPLAY=:0
Environment=XAUTHORITY=%h/.Xauthority

[Install]
WantedBy=default.target
```

---

### 7️⃣ Enable Service

```bash
systemctl --user daemon-reexec
systemctl --user daemon-reload
systemctl --user enable app-time-tracker.service
systemctl --user start app-time-tracker.service
```

---

## 🔁 Reboot Test

```bash
reboot
```

After login:

```bash
systemctl --user status app-time-tracker.service
```

---

## 📊 Data Location

```
data/usage.json
```

---

## 🛑 Stop / Disable

```bash
systemctl --user stop app-time-tracker.service
systemctl --user disable app-time-tracker.service
```

---

## 🧨 Ubuntu Fix (If Needed)

```bash
sudo loginctl enable-linger $USER
```

---

## 👨‍💻 Author

Built for learning Linux system services and Python automation.
