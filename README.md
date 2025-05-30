# Server Uptime Notifier 🖥️🔍

A lightweight Python monitoring and notifier tool that tracks server availability, logs and send notification of uptime/downtime status. Mainly designed for local or unstable server.

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---
## 🚀 Features

- Automated periodic ping to server (IPv4 only)  
- Configurable monitoring intervals  
- Simple, easy-to-understand scripts  
- Clear and concise uptime/downtime logging  
- Email notifications on status changes  
- Minimal resource usage 

---
## 🛠️ Installation (Local)

1. Clone the repository:
```shell
git clone https://github.com/wall-e-08/server-uptime-notifier.git
cd server-uptime-notifier
```

2. Set up virtual environment:
```shell
python -m venv env
source env/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows
```

3. Install dependencies:
```shell
pip install -r requirements.txt
```

4. Copy `.env.example` to `.env` file and update as required
5. Run it
```shell
python main.py
```
Log file location is inside project directory: `/project/path/notification.log`

## ![](https://img.shields.io/badge/-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white&style=flat) Docker
```shell
docker run -d --env-file .env --name container_name imag_name
```
### View logs
```shell
docker exec container_name tail -f /app/notifications.log
```

## 🖥️ Server Setup Manually

1. Repeat `1` to `4` from `Installation (Local)` in your server
2. Create a Systemd Service:
Create file `/etc/systemd/system/monitoring.service` and edit:
```ini
[Unit]
Description=Server Uptime Watcher
After=network.target

[Service]
User=youruser
Group=yourgroup
WorkingDirectory=/path/to/your/project
ExecStart=/path/to/your/project/env/bin/python main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```
3. Add permission:
```shell
sudo chown -R youruser:yourgroup /path/to/your/project
```
3. Enable the system and start:
```shell
sudo systemctl daemon-reload
sudo systemctl enable monitoring.service
sudo systemctl start monitoring.service
```

## 🔮 Upcoming features:
- ~~Dockerize~~
- ![](https://img.shields.io/badge/-%230087CC.svg?logo=telegram&logoColor=white) Telegram
, ![](https://img.shields.io/badge/-%237A42F4.svg?logo=slack&logoColor=white) Slack
 etc. notification

## ⚠️ Important Note
This is a **personal project** I created for my own needs. While it works well for me, it's 
- 🚫 Not an enterprise-grade software
- ⚙️ Configuration/usage is your responsibility

## 🤝 Contributing
PRs welcome! For major changes, please open an issue first to discuss.

## 📄 License
Distributed under the MIT License. See [LICENSE](https://github.com/wall-e-08/server-uptime-notifier/blob/master/LICENSE) for more information.