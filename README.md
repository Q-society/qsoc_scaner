# Q-Society Scanner

An advanced, high-performance open-source OSINT framework designed for rapid digital footprint mapping. It utilizes an optimized multithreading engine to concurrently scan 200+ global platforms and social media networks within seconds.

---

![](https://img.shields.io/badge/Kali%20Linux-Supported-blue?style=for-the-badge&logo=kali-linux&logoColor=white)
![](https://img.shields.io/badge/Termux-Supported-black?style=for-the-badge&logo=android&logoColor=3DDC84)
![](https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python&logoColor=white)

---

## ⚡ Core Features & Intelligence Gathering

Unlike traditional single-threaded lookup tools, this engine deploys a parallel asynchronous request matrix. It queries multiple digital vectors to identify active account profiles across diverse sectors:

* **Social Networks:** Deconstructs profiles across core networks (Instagram, X/Twitter, TikTok, YouTube, Reddit, Pinterest).
* **Developer & Tech Hubs:** Scans technical ecosystems including GitHub, GitLab, Bitbucket, DockerHub, PyPI, and npm.
* **Professional & Creative Portfolios:** Maps footprints on Medium, Behance, Dribbble, Vimeo, and Freelancing nodes.
* **Gaming & Community Forums:** Queries active profiles on Steam, Twitch, Discord, and specialized gaming infrastructures.

---

## 🚀 Installation & Deployment

### 💻 1. Kali Linux / Parrot OS Environment
```bash
sudo apt update && sudo apt install git python3 python3-pip -y
git clone [https://github.com/Q-society/qsoc_scaner.git](https://github.com/Q-society/qsoc_scaner.git)
cd qsoc_scaner
pip3 install requests colorama
python3 qsoc_scanner.py

📱 2. Termux Architecture (Android Emulator)
Bash

pkg update && pkg upgrade -y
pkg install git python -y
git clone [https://github.com/Q-society/qsoc_scaner.git](https://github.com/Q-society/qsoc_scaner.git)
cd qsoc_scaner
pip install requests colorama
python3 qsoc_scanner.py

🛡️ Disclaimer

This framework is strictly engineered for educational research, legal OSINT investigations, and authorized security audits. The development collective assumes no responsibility for unauthorized or malicious utilization.
